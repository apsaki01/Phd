#!/usr/bin/env python3
"""
Generate realistic placeholder figures for the hide-and-seek paper.

The curves are hand-tuned to match the shape and the measured phase-onset
episodes of the real run4 reference run (learning_curve.png): chasing 0-1.74M,
door blocking 1.74-7.86M, seeker ramp use 7.86-11.29M, hider ramp defense
11.29-43.4M. The protected quadrant is the BOTTOM-RIGHT room, matching the
rendered environment. The "[FAKE DATA]" marker is intentionally NOT drawn on the
plots; it lives in the LaTeX figure captions so it can be removed from a single
place once the real numbers are dropped in.

Output: /workspace/paper/images/*.png
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)

TOTAL = 43.4e6                      # total training episodes (target)
PREP, PLAY = 32, 48                 # per-episode horizon (prep + play)
HORIZON = PREP + PLAY

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "figure.dpi": 150,
    "savefig.dpi": 150,
    "axes.grid": True,
    "grid.alpha": 0.25,
})

MFMT = FuncFormatter(lambda x, _pos: f"{x/1e6:.0f}M")
FAKE = ""  # FAKE marker now lives in the LaTeX captions, not on the plots


# ----------------------------------------------------------------------------- helpers
def smooth(y, w=41):
    """Odd-window moving average with edge padding."""
    w = int(w)
    if w % 2 == 0:
        w += 1
    pad = w // 2
    yp = np.pad(np.asarray(y, float), pad, mode="edge")
    k = np.ones(w) / w
    return np.convolve(yp, k, mode="valid")


def wr_from_points(cps, t, noise=0.035, corr=7, seed=0):
    """Interpolate control points (episode, winrate) onto grid t + correlated noise."""
    r = np.random.default_rng(seed)
    xs = np.array([c[0] for c in cps])
    ys = np.array([c[1] for c in cps])
    base = np.interp(t, xs, ys)
    e = smooth(r.normal(0, noise, t.size), corr)
    return np.clip(base + e, 0.0, 1.0)


def style_episodes(ax, ylab="Hider win rate"):
    ax.set_xlim(0, TOTAL)
    ax.xaxis.set_major_formatter(MFMT)
    ax.set_xlabel("Episodes")
    ax.set_ylabel(ylab)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print("wrote", path)


# ----------------------------------------------------------------------------- reference curve
# Control points tuned to the real run4 curve:
#   trough 0.17 @1M -> plateau ~0.90 (4-8M) -> dip 0.60 @11.29M -> recover and
#   climb back to ~0.90 by the end of training (hiders master ramp defense).
REF_CPS = [
    (0.0, 0.27), (0.6e6, 0.19), (1.0e6, 0.17), (1.74e6, 0.25), (2.6e6, 0.45),
    (3.6e6, 0.72), (4.8e6, 0.87), (6.0e6, 0.90), (7.0e6, 0.91), (7.86e6, 0.90),
    (8.8e6, 0.82), (9.8e6, 0.71), (10.6e6, 0.63), (11.29e6, 0.60), (12.2e6, 0.64),
    (13.4e6, 0.70), (15.0e6, 0.76), (18.0e6, 0.82), (22.0e6, 0.86), (28.0e6, 0.885),
    (35.0e6, 0.895), (TOTAL, 0.90),
]

# measured behavioural phase onsets (episodes) from run4:
#   door blocking 1.74M, seeker ramp use 7.86M, hider ramp defense 11.29M
PH2, PH3, PH4 = 1.74e6, 7.86e6, 11.29e6


def fig_curve():
    t = np.linspace(0, TOTAL, 2200)
    raw = wr_from_points(REF_CPS, t, noise=0.045, seed=3)
    ma = smooth(raw, 55)

    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    ax.plot(t, raw, color="#2e7d32", alpha=0.22, lw=1)
    ax.plot(t, ma, color="#1b5e20", lw=2.2, label="Hider win rate (moving avg.)")
    ax.axhline(0.5, ls="--", color="gray", lw=1)

    for x, lab in [(PH2, "door\nblocking"), (PH3, "seeker\nramp use"),
                   (PH4, "hider ramp\ndefense")]:
        ax.axvline(x, ls=":", color="#555", lw=1.2)
        ax.text(x, 0.045, lab, rotation=0, ha="center", va="bottom",
                fontsize=8.5, color="#333")

    ax.set_ylim(0, 1)
    style_episodes(ax)
    ax.set_title(FAKE + "Hider Win Rate over Training")
    ax.legend(loc="lower right")
    save(fig, "fig_curve.png")


# ----------------------------------------------------------------------------- ablation
ADAPT_SEEDS = [  # tight band, phase-4 (ramp defense) ~10.5/11.3/12.5M, ends ~0.90
    [(0, .27), (1e6, .17), (1.74e6, .26), (3e6, .60), (4.5e6, .87), (6e6, .90),
     (7.86e6, .89), (8.8e6, .79), (9.8e6, .66), (10.5e6, .62), (11e6, .66),
     (12.5e6, .72), (16e6, .80), (24e6, .87), (34e6, .895), (TOTAL, .90)],
    [(0, .27), (1e6, .18), (2.0e6, .27), (3.3e6, .58), (5e6, .86), (6.5e6, .905),
     (7.9e6, .88), (9e6, .78), (10.2e6, .64), (11.29e6, .60), (12e6, .65),
     (13.5e6, .72), (18e6, .80), (26e6, .87), (35e6, .89), (TOTAL, .895)],
    [(0, .27), (1e6, .16), (2.2e6, .25), (3.6e6, .56), (5.5e6, .85), (7e6, .90),
     (8.3e6, .87), (9.3e6, .77), (10.8e6, .63), (12e6, .60), (13e6, .66),
     (14.5e6, .72), (20e6, .79), (28e6, .86), (36e6, .885), (TOTAL, .89)],
]
UNIF_SEEDS = [  # wide band, phase-4 ~22/28/never
    [(0, .27), (1e6, .18), (4e6, .40), (9e6, .70), (13e6, .82), (16e6, .80),
     (18e6, .70), (21e6, .62), (23e6, .66), (27e6, .71), (33e6, .72),
     (TOTAL, .72)],
    [(0, .27), (1e6, .19), (5e6, .36), (11e6, .62), (15e6, .80), (20e6, .82),
     (23e6, .71), (27e6, .61), (30e6, .65), (35e6, .69), (TOTAL, .70)],
    [(0, .27), (1e6, .17), (5e6, .33), (12e6, .55), (17e6, .78), (21e6, .80),
     (24e6, .70), (28e6, .60), (34e6, .585), (39e6, .60), (TOTAL, .60)],
]


def _band(seed_cps, noise, seed0):
    t = np.linspace(0, TOTAL, 2200)
    runs = np.stack([wr_from_points(cps, t, noise=noise, seed=seed0 + k)
                     for k, cps in enumerate(seed_cps)])
    m = smooth(runs.mean(0), 55)
    s = smooth(runs.std(0), 55)
    return t, m, s


def fig_ablation():
    t, ma, sa = _band(ADAPT_SEEDS, 0.03, 10)
    _, mu, su = _band(UNIF_SEEDS, 0.05, 40)

    fig, ax = plt.subplots(figsize=(8.2, 4.3))
    ax.plot(t, ma, color="#1565c0", lw=2.2, label="Adaptive curriculum (on), 3 seeds")
    ax.fill_between(t, ma - sa, ma + sa, color="#1565c0", alpha=0.20)
    ax.plot(t, mu, color="#c62828", lw=2.2, label="Uniform sampling (off), 3 seeds")
    ax.fill_between(t, mu - su, mu + su, color="#c62828", alpha=0.18)
    ax.axhline(0.5, ls="--", color="gray", lw=1)

    bb = dict(facecolor="white", alpha=0.7, edgecolor="none", pad=1)
    ax.axvline(11.29e6, ls=":", color="#1565c0", lw=1.4)
    ax.text(11.29e6, 0.965, "phase 4\n(adaptive)", ha="center", va="top",
            fontsize=8, color="#1565c0", bbox=bb)
    ax.axvline(26e6, ls=":", color="#c62828", lw=1.4)
    ax.text(26e6, 0.965, "phase 4\n(uniform)", ha="center", va="top",
            fontsize=8, color="#c62828", bbox=bb)

    ax.set_ylim(0, 1)
    style_episodes(ax)
    ax.set_title(FAKE + "Curriculum Ablation: Adaptive vs. Uniform Door Sampling")
    ax.legend(loc="lower right")
    save(fig, "fig_ablation.png")


# ----------------------------------------------------------------------------- movement
def fig_movement():
    r = np.random.default_rng(11)
    steps = np.arange(HORIZON)

    def obj_speed(t0, t1, peak, seed):
        rr = np.random.default_rng(seed)
        s = np.zeros(HORIZON)
        act = (steps >= t0) & (steps <= t1)
        ramp = np.clip((steps - t0) / 3.0, 0, 1) * np.clip((t1 - steps) / 4.0, 0, 1)
        s[act] = peak * ramp[act] + rr.normal(0, 0.015, act.sum())
        return np.clip(s, 0, None)

    box1 = obj_speed(4, 27, 0.34, 1)
    box2 = obj_speed(7, 30, 0.31, 2)
    ramp = obj_speed(6, 24, 0.29, 3)
    ag1 = np.clip(0.14 + 0.08 * np.sin(steps / 5.0) + r.normal(0, 0.03, HORIZON), 0, None)
    ag2 = np.clip(0.16 + 0.07 * np.cos(steps / 4.0 + 1) + r.normal(0, 0.03, HORIZON), 0, None)

    fig, (a0, a1) = plt.subplots(2, 1, figsize=(8.2, 6.0), sharex=True)
    for y, c, l in [(ag1, "#1565c0", "Hider 1"), (ag2, "#42a5f5", "Hider 2"),
                    (box1, "#ef6c00", "Box 1"), (box2, "#f9a825", "Box 2"),
                    (ramp, "#6a1b9a", "Ramp")]:
        a0.plot(steps, y, color=c, lw=1.8, label=l)
    a0.axvline(PREP, ls="--", color="gray", lw=1.2)
    a0.text(PREP + 0.5, a0.get_ylim()[1] * 0.86, "prep | play", fontsize=9, color="gray")
    a0.set_ylabel("Per-step speed\n(sim units / step)")
    a0.set_title(FAKE + "Agent and Box Displacement over a Representative Episode")
    a0.legend(ncol=5, loc="upper right", fontsize=8.5)

    for y, c, l in [(ag1, "#1565c0", "Hider 1"), (ag2, "#42a5f5", "Hider 2"),
                    (box1, "#ef6c00", "Box 1"), (box2, "#f9a825", "Box 2"),
                    (ramp, "#6a1b9a", "Ramp")]:
        a1.plot(steps, np.cumsum(y), color=c, lw=1.8, label=l)
    a1.axvline(PREP, ls="--", color="gray", lw=1.2)
    a1.set_ylabel("Cumulative distance\n(sim units)")
    a1.set_xlabel("Episode step")
    a1.set_xlim(0, HORIZON - 1)
    save(fig, "fig_movement.png")


# ----------------------------------------------------------------------------- arena helpers
# The protected quadrant is the BOTTOM-RIGHT room: x in [QX, 6], y in [0, QY].
# Its interior walls are the vertical wall at x=QX (with the door gap) and the
# horizontal wall at y=QY; the room's other two sides are the arena boundary.
DOOR_Y = (1.05, 1.60)
QX = 3.4          # interior vertical wall (left wall of the room)
QY = 2.6          # interior horizontal wall (top wall of the room)
RAMP_IN = (4.10, 0.72)
BOX_DOOR = (3.45, 1.33)
BOX_IN = (4.85, 2.05)


def draw_arena(ax, wall_color="black", fill=True):
    ax.add_patch(Rectangle((0, 0), 6, 6, fill=False, lw=2, ec=wall_color))
    ax.plot([QX, QX], [0, DOOR_Y[0]], color=wall_color, lw=3)
    ax.plot([QX, QX], [DOOR_Y[1], QY], color=wall_color, lw=3)
    ax.plot([QX, 6], [QY, QY], color=wall_color, lw=3)
    if fill:
        ax.add_patch(Rectangle((QX, 0), 6 - QX, QY, color="#e8f0fe", zorder=0))
    ax.set_xlim(-0.2, 6.2)
    ax.set_ylim(-0.2, 6.2)
    ax.set_aspect("equal")
    ax.set_xlabel("x (sim units)")
    ax.set_ylabel("y (sim units)")


def in_room(p):
    return (p[:, 0] > QX) & (p[:, 1] < QY)


def walk(anchor, n, scale, seed):
    rr = np.random.default_rng(seed)
    step = rr.normal(0, scale, (n, 2))
    xy = anchor + np.cumsum(step, axis=0) * 0.35
    xy = 0.7 * xy + 0.3 * (anchor + rr.normal(0, scale, (n, 2)))  # pull to anchor
    return xy


def fig_position():
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    draw_arena(ax)

    h1 = walk(np.array([3.75, 1.30]), 260, 0.26, 21)   # guards the door
    h2 = walk(np.array([4.20, 0.85]), 260, 0.26, 22)   # guards the ramp
    ax.scatter(h1[:, 0], h1[:, 1], s=8, color="#1565c0", alpha=0.35, label="Hider 1 (door)")
    ax.scatter(h2[:, 0], h2[:, 1], s=8, color="#00897b", alpha=0.35, label="Hider 2 (ramp)")

    rs = np.random.default_rng(25)

    def seekers(mx, my, sx, sy, n):
        p = np.column_stack([rs.normal(mx, sx, n), rs.normal(my, sy, n)])
        ok = ~in_room(p) & (p[:, 0] > 0.1) & (p[:, 0] < 5.9) & (p[:, 1] > 0.1) & (p[:, 1] < 5.9)
        return p[ok]
    s1 = seekers(2.0, 3.4, 0.80, 0.90, 340)   # seekers massed outside, in the open area
    s2 = seekers(3.0, 4.6, 0.75, 0.70, 340)
    ax.scatter(s1[:, 0], s1[:, 1], s=7, color="#c62828", alpha=0.28, label="Seeker 1")
    ax.scatter(s2[:, 0], s2[:, 1], s=7, color="#ef6c00", alpha=0.28, label="Seeker 2")

    ax.scatter(*BOX_DOOR, marker="s", s=170, color="#5d4037", ec="k", zorder=5, label="Box")
    ax.scatter(*BOX_IN, marker="s", s=170, color="#5d4037", ec="k", zorder=5)
    ax.scatter(*RAMP_IN, marker="^", s=200, color="#6a1b9a", ec="k", zorder=5, label="Ramp")

    ax.set_title(FAKE + "Hider Position Tracking over a Representative Episode")
    ax.legend(loc="lower left", fontsize=8, framealpha=0.9)
    save(fig, "fig_position.png")


# ----------------------------------------------------------------------------- sensitivity
def fig_sensitivity():
    t = np.linspace(0, TOTAL, 2000)

    def curve(dip, rec, final, seed, noise=0.03):
        mid = 0.62 + 0.7 * (final - 0.62)   # gradual recovery toward the final level
        cps = [(0, .27), (1e6, .18), (1.74e6, .30), (3.6e6, .78),
               (dip - 1.5e6, .90), (dip, .88), (dip + 1.5e6, .70),
               (rec - 0.8e6, .62), (rec, .64), (rec + 5e6, mid),
               (rec + 14e6, final), (TOTAL, final)]
        return smooth(wr_from_points(cps, t, noise=noise, seed=seed), 55)

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.5, 4.4), sharey=True)

    # opponent pool
    osc = 0.60 + 0.16 * np.sin(t / 3.2e6) + smooth(np.random.default_rng(1).normal(0, 0.05, t.size), 9)
    axL.plot(t, np.clip(osc, 0, 1), color="#9e9e9e", lw=1.6, label=r"$N=0$ (oscillates)")
    axL.plot(t, curve(9e6, 18e6, 0.83, 5), color="#90caf9", lw=1.6, label=r"$N=5$ ($\approx$18M)")
    axL.plot(t, curve(7.86e6, 11.29e6, 0.90, 6), color="#1565c0", lw=2.6, label=r"$N=10$ ($\approx$11M)")
    axL.plot(t, curve(8.2e6, 13e6, 0.87, 7), color="#7e57c2", lw=1.6, label=r"$N=20$ ($\approx$13M)")
    axL.axhline(0.5, ls="--", color="gray", lw=1)
    axL.set_ylim(0, 1)
    style_episodes(axL)
    axL.set_title("Opponent-pool size " + r"$N_{\mathrm{pool}}$")
    axL.legend(loc="lower right", fontsize=8.5)

    # learning rate
    axR.plot(t, curve(16e6, 24e6, 0.80, 8), color="#a5d6a7", lw=1.6, label=r"$1\times10^{-4}$ ($\approx$24M)")
    axR.plot(t, curve(10e6, 15e6, 0.87, 9), color="#66bb6a", lw=1.6, label=r"$3\times10^{-4}$ ($\approx$15M)")
    axR.plot(t, curve(7.86e6, 11.29e6, 0.90, 6), color="#1565c0", lw=2.6, label=r"$5\times10^{-4}$ ($\approx$11M)")
    div = 0.55 - 0.22 * np.tanh((t - 10e6) / 6e6) + smooth(np.random.default_rng(2).normal(0, 0.07, t.size), 7)
    axR.plot(t, np.clip(div, 0, 1), color="#e53935", lw=1.6, label=r"$1\times10^{-3}$ (diverges)")
    axR.axhline(0.5, ls="--", color="gray", lw=1)
    axR.set_ylim(0, 1)
    style_episodes(axR, ylab="")
    axR.set_title("Learning rate")
    axR.legend(loc="lower right", fontsize=8.5)

    fig.suptitle(FAKE + "Sensitivity to Opponent-Pool Size and Learning Rate", y=1.02)
    save(fig, "fig_sensitivity.png")


# ----------------------------------------------------------------------------- curriculum dynamics
def fig_curriculum():
    t = np.linspace(0, TOTAL, 1600)
    warm = 2.0e6

    def bump(center, width, height):
        return height * np.exp(-0.5 * ((t - center) / width) ** 2)

    # unnormalized mass per config
    p10 = np.where(t < warm, 0.85, 0.15) + bump(0, 1e6, 0.0)          # spine, floor 0.15
    p075 = 0.05 + bump(4e6, 2.4e6, 0.30) + 0.10 * (t > warm)
    p050 = 0.04 + bump(8e6, 3e6, 0.42) + 0.08 * (t > warm)
    p025 = 0.03 + bump(11.3e6, 3.5e6, 0.40) + 0.06 * (t > warm)
    p000 = 0.02 + bump(18e6, 7e6, 0.22) + 0.05 * (t > 8e6)

    M = np.vstack([p10, p075, p050, p025, p000])
    M = np.clip(M, 1e-3, None)
    M = M / M.sum(0, keepdims=True)
    # enforce spine floor 0.15
    deficit = np.clip(0.15 - M[0], 0, None)
    M[0] += deficit
    M[1:] *= (1 - M[0]) / M[1:].sum(0, keepdims=True)
    M = np.array([smooth(row, 31) for row in M])
    M = M / M.sum(0, keepdims=True)

    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    labels = [r"$p_{\mathrm{door}}=1.00$ (spine)", r"$0.75$", r"$0.50$", r"$0.25$", r"$0.00$"]
    colors = ["#08306b", "#2171b5", "#4292c6", "#9ecae1", "#deebf7"]
    ax.stackplot(t, M, labels=labels, colors=colors, alpha=0.95)
    bb = dict(facecolor="white", alpha=0.75, edgecolor="none", pad=1)
    ax.axvline(warm, ls="--", color="k", lw=1.2)
    ax.text(warm, 0.5, "warm-up", ha="center", va="center", rotation=90,
            fontsize=8.5, bbox=bb)
    for x, lab in [(PH3, "ramp use"), (PH4, "ramp defense")]:
        ax.axvline(x, ls=":", color="k", lw=1)
        ax.text(x, 0.5, lab, ha="center", va="center", rotation=90,
                fontsize=8, bbox=bb)

    ax.set_ylim(0, 1)
    style_episodes(ax, ylab="Sampling probability")
    ax.set_title(FAKE + "Auto-Curriculum Sampling Probability per Door Configuration",
                 pad=12)
    ax.legend(loc="center right", fontsize=8.5, framealpha=0.9)
    save(fig, "fig_curriculum.png")


# ----------------------------------------------------------------------------- trajectory + heatmap
def fig_traj_paths():
    fig, ax = plt.subplots(figsize=(7.2, 6.8))
    draw_arena(ax)
    ax.grid(False)

    # Every outside way-point keeps x<QX (or y>QY); the ONLY wall crossing for
    # each path is the door gap at x=QX with y in DOOR_Y, so nothing clips a wall.
    door = np.array([QX, 1.33])
    h1_start = np.array([5.15, 1.85])     # hiders spawn inside the quadrant
    h2_start = np.array([5.15, 0.95])
    ramp_in = np.array([4.55, 0.72])      # object final positions (inside)
    boxA_in = np.array([3.52, 1.22])      # seals lower half of the doorway
    boxB_in = np.array([3.52, 1.52])      # seals upper half of the doorway
    ramp_spawn = np.array([1.80, 0.95])   # object spawns (outside)
    boxA_spawn = np.array([2.30, 1.75])
    boxB_spawn = np.array([1.50, 3.70])
    handoff = np.array([2.55, 2.35])

    def poly(p, n=240):
        p = np.asarray(p, float)
        d = np.linspace(0, 1, len(p))
        dd = np.linspace(0, 1, n)
        return np.column_stack([np.interp(dd, d, p[:, 0]), np.interp(dd, d, p[:, 1])])

    def arrow(path, frac, color, size=15):
        i = int(np.clip(frac, 0.0, 0.98) * (len(path) - 2))
        ax.annotate("", xy=path[i + 1], xytext=path[i], zorder=9,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=2.0,
                                    mutation_scale=size))

    teal, blue = "#00897b", "#1565c0"
    purple, brown, tan = "#6a1b9a", "#5d4037", "#a1887f"

    # Hider trajectories: spawn -> out through the door -> object to fetch. Each
    # object's own inbound (relocation) path is drawn separately and lighter.
    h2 = poly([h2_start, [4.30, 1.05], door, [2.55, 1.12], ramp_spawn])
    h1 = poly([h1_start, [4.30, 1.55], [QX, 1.42], [2.75, 1.55], boxA_spawn])
    ax.plot(h2[:, 0], h2[:, 1], color=teal, lw=2.7, label="Hider 2 (ramp fetcher)", zorder=6)
    ax.plot(h1[:, 0], h1[:, 1], color=blue, lw=2.7, label="Hider 1 (door sealer)", zorder=6)
    for pth, c in [(h2, teal), (h1, blue)]:
        arrow(pth, 0.45, c)
        arrow(pth, 0.82, c)

    # Object relocations through the door (de-emphasized).
    rp = poly([ramp_spawn, [2.60, 1.02], [QX, 1.12], [4.10, 0.88], ramp_in])
    ba = poly([boxA_spawn, [2.80, 1.58], [QX, 1.48], boxA_in])
    bb = poly([boxB_spawn, handoff, [3.05, 1.82], [QX, 1.52], boxB_in])
    ax.plot(rp[:, 0], rp[:, 1], ls="--", color=purple, lw=1.7, alpha=0.85, label="Ramp path", zorder=4)
    ax.plot(ba[:, 0], ba[:, 1], ls="--", color=brown, lw=1.7, alpha=0.85, label="Box path", zorder=4)
    ax.plot(bb[:, 0], bb[:, 1], ls=":", color=tan, lw=2.0, alpha=0.9, label="Relayed box", zorder=4)
    for pth, c in [(rp, purple), (ba, brown), (bb, tan)]:
        arrow(pth, 0.72, c, size=13)

    # Door label pointing at the gap.
    ax.annotate("door", xy=(QX, 1.42), xytext=(3.72, 2.15), fontsize=9.5, color="#2e7d32",
                arrowprops=dict(arrowstyle="->", color="#2e7d32", lw=1.2))

    # Markers: hollow = spawn/start, filled = final position.
    ax.scatter(*h1_start, marker="o", s=70, facecolors="white", edgecolors="k", zorder=7)
    ax.scatter(*h2_start, marker="o", s=70, facecolors="white", edgecolors="k", zorder=7)
    ax.text(h1_start[0] + 0.14, h1_start[1], "H1", fontsize=8.5, va="center", zorder=8)
    ax.text(h2_start[0] + 0.14, h2_start[1], "H2", fontsize=8.5, va="center", zorder=8)
    ax.scatter(*ramp_spawn, marker="^", s=150, facecolors="none", edgecolors=purple, linewidths=1.8, zorder=7)
    ax.scatter(*ramp_in, marker="^", s=200, facecolors=purple, edgecolors="k", zorder=7)
    ax.scatter(*boxA_spawn, marker="s", s=140, facecolors="none", edgecolors=brown, linewidths=1.8, zorder=7)
    ax.scatter(*boxA_in, marker="s", s=170, facecolors=brown, edgecolors="k", zorder=7)
    ax.scatter(*boxB_spawn, marker="s", s=140, facecolors="none", edgecolors=tan, linewidths=1.8, zorder=7)
    ax.scatter(*boxB_in, marker="s", s=170, facecolors=tan, edgecolors="k", zorder=7)

    # Hand-off marker + annotation.
    ax.scatter(*handoff, marker="*", s=320, color="#ffca28", ec="k", zorder=9)
    ax.annotate("box hand-off", xy=handoff, xytext=(0.30, 2.95), fontsize=9, color="#333",
                arrowprops=dict(arrowstyle="->", color="#333", lw=1.2))

    ax.set_title(FAKE + "Preparation-Phase Trajectories and Role Assignment")
    ax.legend(loc="upper right", fontsize=8.5, framealpha=0.95)
    save(fig, "fig_traj_paths.png")


def fig_traj_heatmap():
    r = np.random.default_rng(31)
    door = np.array([3.4, 1.33])

    def corridor(segs, weights, n, jitter=0.16):
        segs = [(np.asarray(a, float), np.asarray(b, float)) for a, b in segs]
        w = np.asarray(weights, float)
        w = w / w.sum()
        out = []
        for _ in range(n):
            a, b = segs[r.choice(len(segs), p=w)]
            u = r.random()
            out.append(a + u * (b - a) + r.normal(0, jitter, 2))
        return np.array(out)

    # Hider 1 (door sealer): outside box spawn -> door -> just inside the doorway
    h1 = corridor([([2.95, 2.75], door),
                   (door, [3.95, 1.15]),
                   ([2.6, 2.4], door)],
                  [0.5, 0.3, 0.2], 16000)
    # Hider 2 (ramp fetcher): center -> ramp spawn (out west), and door -> ramp interior
    h2 = corridor([([3.6, 1.6], [2.30, 2.05]),
                   (door, [4.10, 0.72]),
                   ([2.30, 2.05], door)],
                  [0.40, 0.35, 0.25], 16000)

    fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.6), sharey=True)
    for ax, pts, title in [(axes[0], h1, "Hider 1 (door sealer)"),
                           (axes[1], h2, "Hider 2 (ramp fetcher)")]:
        hh = ax.hist2d(pts[:, 0], pts[:, 1], bins=60, range=[[0, 6], [0, 6]], cmap="magma")
        draw_arena(ax, wall_color="white", fill=False)
        ax.scatter(*BOX_DOOR, marker="s", s=60, color="#4dd0e1", ec="k", zorder=6)
        ax.scatter(*RAMP_IN, marker="^", s=80, color="#4dd0e1", ec="k", zorder=6)
        ax.set_title(title)
        cb = fig.colorbar(hh[3], ax=ax, fraction=0.046, pad=0.04)
        cb.set_label("Occupancy (episodes aggregated)")
    fig.suptitle(FAKE + "Aggregated Per-Hider Occupancy over the Preparation Phase", y=1.02)
    save(fig, "fig_traj_heatmap.png")


# ----------------------------------------------------------------------------- policy architecture
def fig_architecture():
    """Clean single-column schematic of the policy wrapped by the adaptive auto-curriculum."""
    fig, ax = plt.subplots(figsize=(10.2, 8.6))
    ax.set_xlim(0, 11.8)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")

    INK, RAIL, DARK = "#1a1a1a", "#90a4ae", "#37474f"
    EMB_F, EMB_E = "#e8eaf6", "#3949ab"
    ATT_F, ATT_E = "#ede7f6", "#5e35b1"
    POOL_F, POOL_E = "#eceff1", "#607d8b"
    LSTM_F, LSTM_E = "#e0f2f1", "#00897b"
    ACT_F, ACT_E = "#e3f2fd", "#1565c0"
    CUR_F, CUR_E, CUR_D = "#c8e6c9", "#2e7d32", "#1b5e20"

    def box(cx, cy, w, h, text, fc, ec, fs=9.5, lw=1.6, weight="bold", rs=0.10):
        ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                     boxstyle=f"round,pad=0.0,rounding_size={rs}",
                     linewidth=lw, edgecolor=ec, facecolor=fc, zorder=3))
        ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, zorder=4,
                color=INK, weight=weight)
        return dict(c=(cx, cy), t=(cx, cy + h / 2), b=(cx, cy - h / 2),
                    l=(cx - w / 2, cy), r=(cx + w / 2, cy))

    def arw(p1, p2, color=DARK, lw=1.8, rad=0.0):
        ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle="-|>", mutation_scale=15,
                     lw=lw, color=color, zorder=2,
                     connectionstyle=f"arc3,rad={rad}", shrinkA=1.0, shrinkB=2.5))

    ax.text(4.95, 9.55, "Policy Architecture", fontsize=15, weight="bold", ha="center")

    # inputs, left to right: own senses, objects, opponents
    inps = [
        (1.15, "Self", "#e1f5fe", "#039be5"),
        (3.05, "Lidar\n1D conv", "#e0f7fa", "#00acc1"),
        (4.95, "Boxes", "#fff8e1", "#ffb300"),
        (6.85, "Ramps", "#fffde7", "#f9a825"),
        (8.75, "Other\nagents", "#ffebee", "#e53935"),
    ]
    for cx, lbl, fc, ec in inps:
        box(cx, 8.55, 1.6, 0.72, lbl, fc, ec, fs=8.6)

    # bus rail: short stubs merge into one arrow (avoids a tangle of diagonals)
    rail_y = 7.75
    ax.plot([1.15, 8.75], [rail_y, rail_y], color=RAIL, lw=1.6, zorder=1)
    for cx, *_ in inps:
        ax.plot([cx, cx], [8.19, rail_y], color=RAIL, lw=1.4, zorder=1)

    emb = box(4.95, 6.85, 6.0, 0.8, "Fully connected \u2192 entity embeddings",
              EMB_F, EMB_E, fs=9.6)
    att = box(4.95, 5.45, 6.0, 0.95, "Masked self-attention across entities",
              ATT_F, ATT_E, fs=9.8, weight="bold")
    pool = box(4.95, 4.15, 4.4, 0.72, "Average pooling", POOL_F, POOL_E, fs=9.4)
    lstm = box(4.95, 2.95, 3.0, 0.72, "LSTM", LSTM_F, LSTM_E, fs=10, weight="bold")

    arw((4.95, rail_y), emb["t"])
    arw(emb["b"], att["t"])
    arw(att["b"], pool["t"])
    arw(pool["b"], lstm["t"])
    # recurrent self-loop: a circular arrow that leaves and returns to the LSTM's right edge
    lr = 0.30
    gap = np.radians(30)                       # half-width of the opening that faces the box
    lcx = lstm["r"][0] + lr * np.cos(gap)      # so both ends land exactly on the box edge
    lcy = lstm["c"][1]
    th = np.linspace(np.radians(210), np.radians(510), 160)
    lx, ly = lcx + lr * np.cos(th), lcy + lr * np.sin(th)
    ax.plot(lx, ly, color=LSTM_E, lw=2.0, zorder=4)
    ax.add_patch(FancyArrowPatch((lx[-7], ly[-7]), (lx[-1], ly[-1]),
                 arrowstyle="-|>", mutation_scale=14, lw=2.0, color=LSTM_E, zorder=5))

    # action heads
    mv = box(3.55, 1.7, 1.3, 0.6, "Move", ACT_F, ACT_E, fs=9.2)
    gb = box(4.95, 1.7, 1.3, 0.6, "Grab", ACT_F, ACT_E, fs=9.2)
    lk = box(6.35, 1.7, 1.3, 0.6, "Lock", ACT_F, ACT_E, fs=9.2)
    arw(lstm["b"], mv["t"], rad=0.16)
    arw(lstm["b"], gb["t"])
    arw(lstm["b"], lk["t"], rad=-0.16)

    # adaptive auto-curriculum: outer self-play loop feeding back into the opponents
    cur_x = 10.5
    ax.plot([lk["r"][0], cur_x], [1.7, 1.7], color=CUR_E, lw=2.2, zorder=2)
    ax.plot([cur_x, cur_x], [1.7, 8.55], color=CUR_E, lw=2.2, zorder=2)
    ax.add_patch(FancyArrowPatch((cur_x, 8.55), (9.58, 8.55), arrowstyle="-|>",
                 mutation_scale=16, lw=2.2, color=CUR_E, zorder=2))
    ax.text(cur_x, 5.0, "Adaptive auto-curriculum", rotation=90, ha="center",
            va="center", fontsize=11, weight="bold", color=CUR_D,
            bbox=dict(boxstyle="round,pad=0.35", fc=CUR_F, ec=CUR_E, lw=1.6), zorder=6)

    save(fig, "fig_arch.png")


if __name__ == "__main__":
    fig_curve()
    fig_ablation()
    fig_movement()
    fig_position()
    fig_sensitivity()
    fig_curriculum()
    fig_traj_paths()
    fig_traj_heatmap()
    fig_architecture()
    print("all figures written to", OUT)
