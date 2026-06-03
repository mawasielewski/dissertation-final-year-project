import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

COLOUR_HIGH   = "#D7263D"
COLOUR_MEDIUM = "#F4A261"
COLOUR_LOW    = "#2A9D8F"
COLOUR_INFEASIBLE = "#6D6875"

disruption_data = [
    # (route, station, severity, base, disrupted, infeasible)
    ("J1 R1", "Victoria",    "Minor", 9.6,  9.6,  False),
    ("J1 R1", "Victoria",    "Major", 9.6,  10.0, True),
    ("J1 R3", "Westferry",   "Minor", 4.8,  4.8,  False),
    ("J1 R3", "Westferry",   "Major", 4.8,  10.0, True),
    ("J2 R1", "Waterloo",    "Minor", 3.2,  3.2,  False),
    ("J2 R1", "Waterloo",    "Major", 3.2,  10.0, True),
    ("J2 R3", "KX St P",     "Major", 5.2,  10.0, True),
    ("J3 R3", "Kilburn",     "Minor", 1.2,  10.0, True),
    ("J4 R1", "Farringdon",  "Minor", 2.4,  1.6,  False),
    ("J4 R1", "Farringdon",  "Major", 2.4,  10.0, True),
    ("J4 R2", "Bank",        "Major", 3.2,  10.0, True),
]

labels = [f"{d[0]}\n{d[1]}\n({d[2]})" for d in disruption_data]
base_scores = [d[3] for d in disruption_data]
disrupted_scores = [d[4] for d in disruption_data]
infeasible = [d[5] for d in disruption_data]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(16, 6))

bars_base = ax.bar(x - width/2, base_scores, width, color=COLOUR_LOW, alpha=0.85, label="Base score", zorder=3)

bar_colours = [COLOUR_INFEASIBLE if inf else COLOUR_HIGH for inf in infeasible]
bars_disrupted = ax.bar(x + width/2, disrupted_scores, width, color=bar_colours, alpha=0.85, label="Disrupted score", zorder=3)

ax.set_ylabel("Risk Score (/10)", fontsize=11)
ax.set_ylim(0, 12)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9, rotation=35, ha='right')
ax.set_title("Figure 11: Route Risk Score Before and After Disruption Simulation", fontsize=13, fontweight="bold", pad=15)
ax.axhline(y=7.0, color=COLOUR_HIGH,   linestyle="--", linewidth=1, alpha=0.6)
ax.axhline(y=4.0, color=COLOUR_MEDIUM, linestyle="--", linewidth=1, alpha=0.6)
ax.grid(axis="y", linestyle="--", alpha=0.4, zorder=0)

for i, (bar, inf) in enumerate(zip(bars_disrupted, infeasible)):
    if inf:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
                "INFEASIBLE", ha="center", va="bottom", fontsize=6, color=COLOUR_INFEASIBLE, fontweight="bold")

legend_patches = [
    mpatches.Patch(color=COLOUR_LOW,        alpha=0.85, label="Base risk score"),
    mpatches.Patch(color=COLOUR_HIGH,       alpha=0.85, label="Disrupted score (route remains feasible)"),
    mpatches.Patch(color=COLOUR_INFEASIBLE, alpha=0.85, label="Disrupted score (infeasible)"),
]
ax.legend(handles=legend_patches, loc="upper right", fontsize=8)

plt.tight_layout()
plt.savefig("grouped_bar_disruption.png", dpi=300, bbox_inches="tight")
plt.close()
