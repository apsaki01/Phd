# PhD — Emergent behaviour in Hide-and-Seek: ADA (PPO) vs Graph-as-Policy (GaP)

Both methods train **2 hiders vs 2 seekers** in OpenAI's unchanged *quadrant* hide-and-seek environment (MuJoCo 1.50).

| Folder | What it is |
|---|---|
| `ada/` | PPO + self-play opponent pool + adaptive task curriculum (neural policy). Finished 43.4M-episode run; milestone checkpoints in `ada/checkpoints/` (Git LFS). |
| `gap/` | Graph-as-Policy: one computation graph per team, updated **only by an LLM**, scored by parallel MuJoCo rehearsals. Results of past runs in `gap/results/`. |
| `paper/` | LaTeX paper (`main.tex`, ICLR 2027 style), GaP vs ADA slides, figure script. |
| `envs/` | HPC setup (`hpc_setup.sh`, `hpc_env.sh`, pinned `requirements-gap38.txt`). |
| `mujoco-worldgen/`, `multi-agent-emergence-environments/` | Vendored OpenAI code, shared by `ada/` and `gap/`. Do not modify (the environment must stay identical for both methods). |

**New agent/session: read [AGENT_HANDOFF.md](AGENT_HANDOFF.md) first.** It has the full development history, design decisions and open issues.

## Quick start on the UCY HPC (turing2)

```bash
ssh ucy-hpc                                   # from the Mac
git lfs install
git clone https://github.com/apsaki01/Phd.git ~/Phd
cd ~/Phd && git lfs pull
bash envs/hpc_setup.sh                        # once; re-running is safe
```

`~/.mujoco/mjkey.txt` must exist (it is **never** committed). Upload it from the Mac if missing:
`scp ~/Downloads/mjkey.txt ucy-hpc:~/.mujoco/mjkey.txt`.

Scripts in `ada/` and `gap/` add the two vendored folders to `sys.path` themselves; nothing needs `pip install -e`.

### Render ADA video (Slurm, CPU)

```bash
cd ~/Phd && sbatch ada/render_ada_turing.slurm
# options: ADA_CHECKPOINT=~/Phd/ada/checkpoints/rampuse.npz RENDER_EPISODES=5 sbatch ada/render_ada_turing.slurm
# output: ~/ada_hide_and_seek_10episodes.mp4, log: ada-render-<jobid>.out
```

### GaP training (Slurm, 48 CPUs + Bifrost LLM)

```bash
cd ~/Phd
read -s GAP_LLM_API_KEY && export GAP_LLM_API_KEY    # Bifrost virtual key, never write it to a file
sbatch --export=ALL gap/run_gap_turing.slurm
# output: ~/training_output_gap_turing/ (learning_curve.png, history.csv, train.log, best_*_graph.json)
```

Everything that computes runs through Slurm, never directly on the login node (admins' rule). Quick tests use a short `srun` session; see `AGENT_HANDOFF.md` §9.8.

### Render GaP graphs (inside `srun -p COMPUTE -c 4 --mem=8G -t 00:30:00 --pty bash`)

```bash
source envs/hpc_env.sh && export TMPDIR=/tmp/${USER}_render && mkdir -p $TMPDIR && cd gap
$PY render_gap.py results/llm_only_2M_fast/best_hider_graph.json results/llm_only_2M_fast/best_seeker_graph.json
rm -rf $TMPDIR
```

### ADA training

On the HPC this needs a Slurm GPU job script (not written yet; one V100 is enough). On a private machine (Vast.ai): `ada/setup_vastai.sh`, then `bash ada/run_train.sh`. Set `OUTPUT_DIR` for the output folder.
To continue the finished run, copy `ada/checkpoints/final_policy.npz` to `<OUTPUT_DIR>/checkpoints/resume_latest.npz`.

### Paper

`paper/main.tex` (paper), `paper/gap_vs_ada_slides.tex` (Beamer, 4 slides), `python3 paper/make_figures.py` regenerates `paper/images/`.
The slides also need `paper/mujoco images/` (chasing, door blocking, ramp hide, ramp use PNGs).

## Not in git

- `mjkey.txt`, any LLM key (`GAP_LLM_API_KEY`).
- Training outputs (`training_output*/`), MP4 videos, Slurm `*.out` logs.
- The 82 intermediate ADA checkpoints (only the 5 named milestones are kept).

## License

The environment and worldgen code come from OpenAI's Multi-Agent Emergence Environments and MuJoCo worldgen projects; their license files are kept in the vendored folders.
