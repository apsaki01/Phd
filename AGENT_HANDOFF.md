# Agent handoff: development history and current state

This file is for the next agent (or person) working on this repo. It covers what was built, why, where things are, what is broken or pending, and how the user wants to work. Last updated 2026-11-07, when work moved from a Vast.ai machine (now destroyed) to the UCY HPC.

---

## 1. The user and how to work with them

- PhD student, **not a programmer**. Always give **exact copy-paste commands** and say **which terminal** to use:
  - Mac: prompt `studentone@cs11572acstudio ~ %` (SSH alias `ucy-hpc` points to turing2).
  - HPC login node: prompt `apsaki01@turing2:~$`.
- Keep answers **short**. Explain concepts plainly when asked (they often ask "what exactly does X do?").
- Messages to the HPC admins: short, in **Greek**, keep English technical terms in English.
- **Never ask for or print** the Bifrost key. The user exports it themselves with `read -s GAP_LLM_API_KEY`.
- **Never commit** `mjkey.txt` or any key. The old `hide-and-seek-ada` repo had `mjkey.txt` committed; that repo is being archived.

## 2. Research goal

Compare two ways of getting **emergent multi-agent behaviour** in OpenAI's hide-and-seek **quadrant** game, with the **environment unchanged**:

1. **ADA** (`ada/`): neural policy trained with PPO, a self-play opponent pool and an adaptive task curriculum. This reproduces OpenAI's emergence (chasing → door blocking → ramp use → ramp defense).
2. **GaP — Graph-as-Policy** (`gap/`): re-implementation of Chen et al., arXiv:2607.05369 (the PDF was `2607.05369v1-2.pdf` on Vast; not in the repo). Each team's policy is a **directed graph of primitive skills**. An **LLM** rewrites the graph and parallel MuJoCo rehearsals score each proposal. There is **no gradient training**.

The four emergent behaviours tracked in both are: `chasing`, `door_blocking`, `ramp_use` (seekers), `ramp_defense` (hiders).

## 3. Repo layout (after the 2026-11-07 restructure)

```
Phd/
├── README.md                 usage / quick start
├── AGENT_HANDOFF.md          this file
├── envs/                     hpc_setup.sh (one-time), hpc_env.sh (source before running), requirements-gap38.txt
├── mujoco-worldgen/          vendored OpenAI, shared, DO NOT MODIFY
├── multi-agent-emergence-environments/   vendored OpenAI (+ small fixes already inside, see §4.3), shared
├── ada/
│   ├── train_ada.py          PPO+self-play+PLR curriculum trainer (≈85 KB, single file)
│   ├── render_ada.py         renders an .npz checkpoint to MP4 (CPU, osmesa)
│   ├── render_ada_turing.slurm   Slurm job: render on HPC COMPUTE partition
│   ├── render_quadrant.py    renders OpenAI's own pretrained quadrant policy (needs TF/baselines, not installed on HPC)
│   ├── run_train.sh          restart-on-hang launcher for train_ada.py
│   ├── monitor.sh            tail training progress
│   ├── setup_vastai.sh       full install for a root Ubuntu GPU box (Vast.ai)
│   ├── validate_ramp_fix.py  checks the ramp never spawns inside the hider quadrant
│   ├── learning_curve_run4.png
│   └── checkpoints/          Git LFS, ≈80 MB each (see §4.2)
├── gap/
│   ├── train_gap.py          the GaP harness (≈89 KB, single file)
│   ├── render_gap.py         render two graph JSONs to MP4
│   ├── run_gap.sh            restart launcher (non-Slurm)
│   ├── run_gap_turing.slurm  Slurm job: 48 CPUs, Bifrost LLM
│   └── results/              4 past runs (see §5.5)
└── paper/
    ├── main.tex, references.bib, iclr2027/   ICLR-2027-style paper (ADA paper draft)
    ├── make_figures.py       regenerates images/fig_*.png (synthetic/illustrative figures)
    ├── images/               9 figures used by main.tex
    ├── gap_vs_ada_slides.tex 4-slide Beamer deck GaP vs ADA (user edited it in Overleaf style)
    ├── gap_training_program.tex, gap_methodology_explanation.tex   GaP write-ups
    └── mujoco images/        4 screenshots used by the slides (added from the user's Mac)
```

**Path convention:** every script in `ada/` and `gap/` sets `ROOT_DIR = parent of its own folder` and puts `ROOT_DIR/mujoco-worldgen` and `ROOT_DIR/multi-agent-emergence-environments` on `sys.path`. MuJoCo defaults to `~/.mujoco/mjpro150` and `~/.mujoco/mjkey.txt`, and the env vars `MUJOCO_PY_MJPRO_PATH` / `MUJOCO_PY_MJKEY_PATH` override them. No `/workspace` or `/root` paths remain except in `ada/setup_vastai.sh`, which is Vast-specific on purpose.

## 4. ADA (finished)

### 4.1 Method (`ada/train_ada.py`)
- Network architecture identical to OpenAI's pretrained policy: entity embeddings 128, self-attention with 4 heads, LSTM 256, dense 256, circular-conv lidar.
- PPO with OpenAI Table S.1 hyper-parameters: γ 0.998, λ 0.95, clip 0.2, lr 5e-4 with linear decay, 4 epochs, full batch. Entropy coefficient 0.012.
- 128 envs, horizon 80 (40 % prep phase), 2v2.
- Self-play **opponent pool**: 10 snapshots, saved every 100k episodes. After 100k episodes, opponents are sampled from the pool with probability 0.3.
- **Adaptive curriculum (PLR)** over `TASK_SPACE` = `p_door_dropout` ∈ {1.0, 0.75, 0.5, 0.25, 0.0} (1 vs 2 doors).
  - Each task is scored by an EMA of mean |GAE advantage|.
  - 2M-episode warm-up on the 1-door task, with a probability floor of 0.15.
- `lock_ramp=False`: hiders defend the ramp by dragging it inside their quadrant. Box locking stays on.
- Env fix: `ramp_outside_quadrant=True`, so the ramp always spawns outside the hider quadrant.
- Resume logic picks the newer of the newest `checkpoint_*.npz` and `checkpoints/resume_latest.npz`.

### 4.2 Run 4 (the final run) and checkpoints
- 43,400,064 episodes on a Vast.ai RTX 4090. The log `train.log` (30 MB) was not kept.
- All four behaviours emerged. Kept checkpoints (`ada/checkpoints/`, LFS), with the episode number stored in each file:

| file | episode | shows |
|---|---|---|
| `door.npz` | 8,001,536 | door blocking |
| `chaising.npz` (sic) | 15,002,880 | chasing |
| `rampuse.npz` | 17,003,264 | seekers use ramp |
| `rampdefense.npz` | 21,509,504 | hiders defend ramp |
| `final_policy.npz` | 43,400,064 | final |

- The other 82 milestone checkpoints (6.5 GB) were **deliberately dropped** (user decision). `resume_latest.npz` was dropped too, because `final_policy.npz` holds the same state including the opponent pool.

### 4.3 Environment edits
The vendored env includes the project's edits to `mae_envs/envs/hide_and_seek.py` (for example `ramp_outside_quadrant`, quadrant hider placement) and to `mae_envs/wrappers/multi_agent.py`. ADA and GaP use the **same** env kwargs (`BASE_ENV_KWARGS` / `ENV_KWARGS`). Do not change the env, because the comparison depends on it.

### 4.4 Rendering on the HPC: done
- Job 41698 rendered `final_policy.npz`: 10 episodes, 827 KB, saved to `~/ada_hide_and_seek_10episodes.mp4` on turing2. It used the old bundle in `~/ada_render_retry`.
- The new repo command is `sbatch ada/render_ada_turing.slurm`.

## 5. GaP (main ongoing work)

### 5.1 Concept
- **Policy:** one graph per team (hiders, seekers).
  - A graph has `assign` (`fixed` or `nearest_object`), `params` (`gain`, `damp`, `tol`, `offset`, `seg_timeout`) and, per role (2 agents), a `prep` and a `play` list of **segments**.
  - A segment has:
    - `behaviour`: `stay`, `flee`, `chase`, `search`, `go`, `segments`;
    - an optional `acquire` (`box` or `ramp`) and a `target`, for example `door_block`, `door_inside`, `quadrant_interior`, `quadrant_corner`, `ramp_inside`, `outside_wall`;
    - `face` (`target`, `align`, `yaw0..3`) and `route` (`door`, `direct`);
    - an optional `gate`: `teammate_inside`, `ramp_inside`, `opponent_visible`, `doors_sealed`, `door`;
    - `lock` / `release`.
- **Primitive skills only.** No skill encodes "block door" or "hide ramp", so those must be **composed**. This is what makes them count as emergent.
- A `TeamController` executes the graph every step and outputs the env's discrete actions (movement bins, grab, lock). The executor is deterministic; the graph itself is the policy.
- **Self-learning loop**, the paper's Algorithm 1 adapted to two teams:
  1. Sample task instances (door configuration + seed).
  2. Rehearse the candidate graph against the opponent's current graph, or a pool graph with probability 0.3, in N worker processes.
  3. Failure analysis produces per-episode diagnostics, and the result is written as markdown feedback.
  4. **The LLM proposes new graphs.**
  5. Re-rehearse with **100 paired episodes per candidate** (same seeds for incumbent and candidate).
  6. Accept a candidate only if J improves by more than `GAP_ACCEPT_MARGIN` (0.05).
  7. **Both teams update every round.**
- **Objective J:** a team score in [0, 1] built from the env's zero-sum rewards. `J_hider` is roughly the hider win rate. The CSV logs `J_hider`, `hider_winrate` and per-behaviour rates. The onset of a behaviour is recorded when its rate exceeds `ONSET_THRESHOLD` (chasing 0.3, door 0.5, ramp_use 0.3, ramp_defense 0.5).

### 5.2 LLM-only updates (user requirement)
- The user required that **graph updates come only from the LLM**. `GAP_LLM_ONLY=1` disables the structural-mutation search.
- 5 **persistent writer threads per team** call the LLM continuously and drop proposals into an inbox. Each round rehearses what arrived within `GAP_ROUND_WINDOW` (45 s).
- Structured output: a JSON schema from `graph_json_schema()` is sent as `response_format`. If the endpoint rejects it, the code falls back to plain JSON.
- `/no_think` is added for qwen3 models.
- If validation fails, there is 1 repair retry that includes the validator error. The validator also rejects **self-blocking gates**.
- The endpoint is any OpenAI-compatible `/chat/completions`. Auth header is configurable:
  - `GAP_LLM_API_KEY_HEADER=Authorization` → `Bearer <key>`;
  - `GAP_LLM_API_KEY_HEADER=x-bf-vk` → raw key, used by Bifrost.

### 5.3 Speed work
- Target from the user: **at least 10 episodes per second**.
- Implemented:
  - an asynchronous `RehearsalPool` (worker processes with pipes, `submit()` returns futures);
  - 1 BLAS thread per worker;
  - LLM calls that overlap rehearsals.
- Measured on Vast (container capped at about 15 CPUs, 14 workers): about 9–10 eps/s.
- On HPC COMPUTE nodes (48 CPUs, 44 workers) it should comfortably exceed 10 eps/s. **Not yet measured**, see §6.

### 5.4 Environment variables (`train_gap.py`)
| var | default | meaning |
|---|---|---|
| `GAP_LLM_API_KEY` | – | key (export only, never in files) |
| `GAP_LLM_API_KEY_HEADER` | `Authorization` | `x-bf-vk` for Bifrost |
| `GAP_LLM_BASE_URL` | `https://api.openai.com/v1` | Bifrost: `https://turing2.ucy.ac.cy/v1` |
| `GAP_LLM_MODEL` | `gpt-4o-mini` | Bifrost: `qwen3.5:9b` or `qwen3:8b` |
| `GAP_LLM_ONLY` | 0 | 1 = LLM is the only update source |
| `GAP_LLM_PROPOSALS` | 5 if LLM-only | writers per team |
| `GAP_LLM_TEMPERATURE` | 0.7 | |
| `GAP_LLM_REPAIRS` | 1 | |
| `GAP_ROUND_WINDOW` | 45 | seconds |
| `GAP_ACCEPT_MARGIN` | 0.05 | |
| `GAP_REHEARSALS` | 100 if LLM-only else 40 | episodes per candidate |
| `GAP_WORKERS` | 14 | 44 on HPC |
| `GAP_TOTAL_EPISODES` | 43.4M | 2M was used for runs |
| `GAP_OUTPUT_DIR` | `~/training_output_gap` | resumes from `gap_state.json` |
| `SMOKE_TEST=1` | | tiny end-to-end test |
| `GAP_ORACLE_TEST=1` | | hand-written graphs validate skills and detectors |

### 5.5 Past runs (`gap/results/`, all on Vast, qwen3:8b via local Ollama, 14 workers)
| run | setup | episodes | outcome |
|---|---|---|---|
| `pilot_neutral` | LLM + structural search (not LLM-only), 40 rehearsals | 100k, 10.3 eps/s | onsets: chasing at 25.8k, ramp_defense at 27.7k, door_blocking at 60.2k. Best J: hider 0.73, seeker 0.89. |
| `llm_only_2M` | LLM-only v1, synchronous | 1.7k (crashed: worker EOFError) | 1.7 eps/s, too slow; led to the async redesign |
| `llm_only_2M_v2` | LLM-only, 2 repairs | 7.1k (crashed: connection reset) | 2.6 eps/s |
| `llm_only_2M_fast` | **current design**: 5 writers per team, both teams every round, 100 paired rehearsals, 45 s window | **2.0M, 9.2 eps/s, 4611 iterations** | door_blocking onset at 527k episodes (rate 0.57). At the end, door blocking 0.44 and ramp_defense 0.19; ramp_use never appeared. Best J: hider 0.48, seeker 0.94. Its `feedback/` folder (37 MB, 9k files) was not committed. |

The final graphs are in `best_hider_graph.json` / `best_seeker_graph.json`. They can be rendered with `render_gap.py`.

## 6. HPC (UCY turing2): state and open issues

- Login: `ssh ucy-hpc` (turing2.ucy.ac.cy; **not** turing1). Scheduler: Slurm. Partitions:
  - `COMPUTE`: 48 CPUs per node, 7-day limit.
  - `GPU`: `--gres=gpu:tesla_v100-sxm2-32gb:N` or `gpu:tesla_t4:1`.
  - `INFERENCE`: admins only.
- Modules need `module use /opt/ohpc/pub/software/modules/all`. `envs/hpc_env.sh` does this and loads Anaconda3/2025.06-1, GCCcore/12.3.0, Mesa/23.1.4 and glew/2.2.0-osmesa.
- **Already installed on turing2** (it survives the Vast shutdown):
  - the conda env `~/conda_envs/gap38` (Python 3.8.20) with the pinned packages, `torch` 2.0.1 (CPU build) and `mujoco-py` 1.50.1.68 (compiled);
  - `~/.mujoco/mjpro150` and `~/.mujoco/mjkey.txt` (chmod 600).
- Problems solved on the way:
  - Conda's default channel needs a ToS accept → use `--override-channels -c conda-forge`.
  - Packages were missing one at a time (cffi, lockfile, xmltodict).
  - Slurm `$(dirname $0)` points to the spool directory → scripts now `cd "${PHD_DIR:-$HOME/Phd}/ada|gap"`.
  - `scp` from turing2 to turing1 is denied.
  - A truncated tarball upload was caught by checking the SHA-256.
- Old directories on turing2 from before this repo (`~/gap_turing`, `~/ada_render_retry`) can be deleted after the repo works.
- **Bifrost LLM** (OpenAI-compatible, `https://turing2.ucy.ac.cy/v1`, header `x-bf-vk`):
  - From the login node it works, about 9 s per reply.
  - From a COMPUTE node (job 41697), all requests **timed out after 180 s** with 10 parallel writers. **The GaP benchmark on the HPC is blocked by this.**
- **Email sent to the admins (reply pending)**, asking:
  1. whether Bifrost has concurrency or rate limits, or is unreachable from compute nodes;
  2. whether running Ollama inside a GPU job is allowed (`export OLLAMA_MODELS=/opt/share/ollama; module load ollama`);
  3. for V100 access.
- Fallbacks to try:
  - fewer writers (`GAP_LLM_PROPOSALS=2`) and a longer `GAP_ROUND_WINDOW`;
  - or a GPU job running `ollama serve` plus `train_gap.py` on the same node, with `GAP_LLM_BASE_URL=http://127.0.0.1:11434/v1` and `GAP_LLM_API_KEY_HEADER=Authorization` and a dummy key.

## 7. Next steps (in order)
1. On turing2, clone this repo and run `bash envs/hpc_setup.sh` to verify.
2. Run a smoke test with `SMOKE_TEST=1`, then `sbatch ada/render_ada_turing.slurm` to confirm the new paths.
3. Act on the admins' reply, then run the GaP benchmark `gap/run_gap_turing.slurm`.
   - Report eps/s; the target is ≥ 10.
   - Then do a full LLM-only run and check whether `ramp_use` emerges, which it did not by 2M on Vast.
4. Render GaP behaviour videos to compare with ADA's. Update the slides and the paper with the HPC numbers.

## 8. Things that are NOT in this repo
- The 82 intermediate ADA checkpoints, ADA `train.log` (30 MB), and several MP4 renders (each 1–3 MB).
- Big ZIP backups and `ollama.log`.
- The GaP paper PDF (arXiv 2607.05369).
- The `feedback/` folder of `llm_only_2M_fast`.

All of these lived only on the Vast machine and are gone.

## 9. Command cheat sheet (what we actually use)

Always tell the user **which terminal** a command goes in:
- **[Mac]** `studentone@cs11572acstudio ~ %`
- **[HPC]** `apsaki01@turing2:~$`

Unless noted otherwise, commands run on the HPC from `~/Phd`.

### 9.1 Connecting and moving files
```bash
# [Mac] log in to the HPC (alias defined in ~/.ssh/config)
ssh ucy-hpc
# [Mac] upload a file / download a result (run on the Mac, NOT inside the ssh session)
scp ~/Downloads/mjkey.txt ucy-hpc:~/.mujoco/mjkey.txt
scp ucy-hpc:~/ada_hide_and_seek_10episodes.mp4 ~/Desktop/
scp -r ucy-hpc:~/training_output_gap_turing ~/Desktop/
# [Mac] verify a big transfer was not truncated (compare with the same command on the HPC)
shasum -a 256 file.tar.gz          # Mac
sha256sum file.tar.gz              # HPC
```

### 9.2 Environment (every new HPC shell)
```bash
source ~/Phd/envs/hpc_env.sh       # modules + MuJoCo paths; sets $PY to the gap38 python
$PY -c "import mujoco_py; print('ok')"
```
Use `$PY` (= `~/conda_envs/gap38/bin/python`), not `python3`. The system python lacks the packages.

### 9.3 Code updates
```bash
cd ~/Phd && git pull && git lfs pull      # get the latest code + checkpoints
git status; git add -A; git commit -m "msg"; git push   # push results/code from the HPC
```
Never `git add` keys, `training_output*/` or videos (`.gitignore` already blocks them; still check `git status` first).

### 9.4 Slurm (the normal way to run on the HPC)
Do not run heavy jobs on the login node.
```bash
sbatch ada/render_ada_turing.slurm               # submit; prints "Submitted batch job <ID>"
ADA_CHECKPOINT=~/Phd/ada/checkpoints/rampuse.npz RENDER_EPISODES=5 sbatch ada/render_ada_turing.slurm
read -s GAP_LLM_API_KEY && export GAP_LLM_API_KEY   # user types the key; nothing is shown
sbatch --export=ALL gap/run_gap_turing.slurm
squeue -u apsaki01                               # my jobs: R = running, PD = pending (reason in last column)
scancel <ID>                                     # stop a job
sacct -j <ID> --format=JobID,State,Elapsed,MaxRSS,ExitCode   # after it finished
sinfo -p COMPUTE,GPU                             # free/busy nodes
tail -f gap-bench-<ID>.out                       # follow the job's log live (Ctrl+C stops watching, not the job)
srun -p COMPUTE -c 4 --mem=8G -t 00:30:00 --pty bash   # interactive shell on a compute node (for debugging)
```
Slurm logs (`ada-render-<ID>.out`, `gap-bench-<ID>.out`) are written to the folder you ran `sbatch` from, which is `~/Phd`.

### 9.5 Background runs without Slurm (the Vast.ai style)
Use this only on a machine you own. On the HPC, use Slurm.
```bash
# start in the background, survive logout, keep a log
cd ~/Phd/gap && mkdir -p ~/training_output_gap
nohup bash run_gap.sh > ~/training_output_gap/wrapper.log 2>&1 & disown
cd ~/Phd/ada && nohup bash run_train.sh > training_output/wrapper.log 2>&1 & disown
#   nohup   = keep running after the terminal closes
#   > f 2>&1 = stdout and stderr into the log file
#   &       = run in background;  disown = detach from this shell
ps aux | grep -E 'train_gap|train_ada' | grep -v grep    # is it running?
pkill -f train_gap.py                                    # stop it (the run_gap.sh loop also exits on rc 130/0)
```

### 9.6 Watching training progress
```bash
tail -f ~/training_output_gap_turing/train.log           # live log (Ctrl+C to stop watching)
tail -n 30 ~/training_output_gap_turing/train.log        # last 30 lines
grep 'eps/s' ~/training_output_gap_turing/train.log | tail -1   # current speed + J + behaviour rates
tail -3 ~/training_output_gap_turing/history.csv         # per-iteration metrics
grep -i -E 'error|traceback|timed out' ~/training_output_gap_turing/train.log | tail
bash ~/Phd/ada/monitor.sh                                # ADA progress (uses OUTPUT_DIR)
```
A GaP log line looks like:
`[it 4611 | 2.000M eps | 9.2 eps/s | 216643s] J_h=0.271 WR_h=0.28 beh={'chase':..,'door':..,'r_use':..,'r_def':..} stale(h/s)=768/602`.
- `it`, `eps`: iteration and episode counters.
- `eps/s`: throughput; the target is ≥ 10.
- `J_h`, `WR_h`: hider objective and hider win rate.
- `beh`: behaviour rates.
- `stale`: rounds since each team last improved.

To get `learning_curve.png` onto the Mac, use `scp` (§9.1).

### 9.7 Quick tests
```bash
source ~/Phd/envs/hpc_env.sh
cd ~/Phd/gap && SMOKE_TEST=1 GAP_OUTPUT_DIR=/tmp/gap_smoke_$USER $PY train_gap.py   # ~1 min, no LLM needed
cd ~/Phd/gap && GAP_ORACLE_TEST=1 $PY train_gap.py                                  # hand-written graphs: skills + detectors
cd ~/Phd/ada && RENDER_EPISODES=1 RENDER_OUTPUT=/tmp/t.mp4 $PY render_ada.py        # 1-episode render
# Bifrost reachability (login node). The key comes from the exported variable, never typed into files
curl -s -m 60 https://turing2.ucy.ac.cy/v1/models -H "x-bf-vk: $GAP_LLM_API_KEY" | head -c 300
```

### 9.8 Disk and housekeeping
```bash
du -sh ~/* | sort -h | tail        # what uses space
quota -s 2>/dev/null || df -h ~    # home quota
find /tmp -maxdepth 1 -user $USER -name 'tmp*.xml' -delete   # MuJoCo leaks temp XMLs on every reset
```

### 9.9 Agent tool quirk (VS Code terminal)
In the Vast workspace, terminal commands often only returned "opened the alternate buffer" instead of their output. The workaround was:
1. Redirect the output to a file, `{ cmd1; cmd2; } > /tmp/out.txt 2>&1`.
2. Read that file.

Long commands keep running after the tool returns. Re-read the file until the output is complete.
