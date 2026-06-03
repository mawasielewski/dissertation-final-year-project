import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy import stats

routes = [
    {"name": "J1 R1", "time": 32,  "risk": 9.6, "class": "HIGH",   "journey": "J1"},
    {"name": "J1 R2", "time": 56,  "risk": 4.4, "class": "MEDIUM", "journey": "J1"},
    {"name": "J1 R3", "time": 55,  "risk": 4.8, "class": "MEDIUM", "journey": "J1"},
    {"name": "J2 R1", "time": 45,  "risk": 3.2, "class": "LOW",    "journey": "J2"},
    {"name": "J2 R2", "time": 40,  "risk": 8.8, "class": "HIGH",   "journey": "J2"},
    {"name": "J2 R3", "time": 62,  "risk": 5.2, "class": "MEDIUM", "journey": "J2"},
    {"name": "J3 R1", "time": 60,  "risk": 3.6, "class": "LOW",    "journey": "J3"},
    {"name": "J3 R2", "time": 35,  "risk": 3.2, "class": "LOW",    "journey": "J3"},
    {"name": "J3 R3", "time": 61,  "risk": 1.2, "class": "LOW",    "journey": "J3"},
    {"name": "J4 R1", "time": 27,  "risk": 2.4, "class": "LOW",    "journey": "J4"},
    {"name": "J4 R2", "time": 26,  "risk": 3.2, "class": "LOW",    "journey": "J4"},
    {"name": "J4 R3", "time": 36,  "risk": 3.2, "class": "LOW",    "journey": "J4"},
]

CLASS_COLOUR = {
    "HIGH":   "#D7263D",
    "MEDIUM": "#F4A261",
    "LOW":    "#2A9D8F"
}

JOURNEY_MARKER = {
    "J1": "o",
    "J2": "s",
    "J3": "^",
    "J4": "D"
}

# fastest and safest per journey for arrows
tradeoffs = {
    "J1": {"fastest": ("J1 R1", 32, 9.6),  "safest": ("J1 R2", 56, 4.4)},
    "J2": {"fastest": ("J2 R2", 40, 8.8),  "safest": ("J2 R1", 45, 3.2)},
    "J3": {"fastest": ("J3 R2", 35, 3.2),  "safest": ("J3 R3", 61, 1.2)},
    "J4": {"fastest": ("J4 R2", 26, 3.2),  "safest": ("J4 R1", 27, 2.4)},
}

JOURNEY_ARROW_COLOUR = {
    "J1": "#1D3557",
    "J2": "#6D6875",
    "J3": "#457B9D",
    "J4": "#2D6A4F",
}

fig, ax = plt.subplots(figsize=(12, 7))

# background bands
ax.fill_between([0, 75], 7, 10.5, color="#D7263D", alpha=0.04)
ax.fill_between([0, 75], 4, 7,   color="#F4A261", alpha=0.04)
ax.fill_between([0, 75], 0, 4,   color="#2A9D8F", alpha=0.04)

# threshold lines
ax.axhline(y=7.0, color="#D7263D", linestyle="--", linewidth=1, alpha=0.5)
ax.axhline(y=4.0, color="#F4A261", linestyle="--", linewidth=1, alpha=0.5)

# trend line
times = np.array([r["time"] for r in routes])
risks = np.array([r["risk"] for r in routes])
slope, intercept, r_value, p_value, std_err = stats.linregress(times, risks)
x_line = np.linspace(15, 75, 100)
y_line = slope * x_line + intercept
ax.plot(x_line, y_line, color="#888888", linestyle="-.", linewidth=1.5,
        alpha=0.6, label=f"Trend line (R²={r_value**2:.2f})", zorder=2)

# arrows showing fastest -> safest tradeoff per journey
for journey, data in tradeoffs.items():
    fx, fy = data["fastest"][1], data["fastest"][2]
    sx, sy = data["safest"][1], data["safest"][2]
    colour = JOURNEY_ARROW_COLOUR[journey]
    ax.annotate(
        "",
        xy=(sx, sy),
        xytext=(fx, fy),
        arrowprops=dict(
            arrowstyle="-|>",
            color=colour,
            lw=1.5,
            alpha=0.6,
            connectionstyle="arc3,rad=0.15"
        ),
        zorder=3
    )
    mid_x = (fx + sx) / 2
    mid_y = (fy + sy) / 2 + 0.3
    ax.text(mid_x, mid_y, journey, fontsize=7.5, color=colour,
            ha="center", fontweight="bold", alpha=0.8)

# scatter points
for r in routes:
    ax.scatter(
        r["time"], r["risk"],
        color=CLASS_COLOUR[r["class"]],
        marker=JOURNEY_MARKER[r["journey"]],
        s=140,
        zorder=5,
        edgecolors="white",
        linewidths=0.8
    )
    offset_x = 1.2
    offset_y = 0.18
    if r["name"] in ["J1 R2", "J4 R1"]:
        offset_y = -0.38
    if r["name"] in ["J3 R1", "J3 R3"]:
        offset_x = -6.5
    ax.annotate(
        r["name"],
        xy=(r["time"], r["risk"]),
        xytext=(r["time"] + offset_x, r["risk"] + offset_y),
        fontsize=8,
        color="#333333"
    )

ax.set_xlabel("Travel Time (mins)", fontsize=11)
ax.set_ylabel("Risk Score (/10)", fontsize=11)
ax.set_title("Risk Score vs Travel Time — All Routes\n"
             "Arrows indicate fastest → safest route per journey",
             fontsize=12, fontweight="bold", pad=15)
ax.set_xlim(15, 75)
ax.set_ylim(0, 10.5)
ax.grid(True, linestyle="--", alpha=0.3, zorder=0)

# risk band labels
ax.text(16, 9.0, "HIGH", fontsize=8, color="#D7263D", alpha=0.5, fontstyle="italic")
ax.text(16, 5.5, "MEDIUM", fontsize=8, color="#F4A261", alpha=0.5, fontstyle="italic")
ax.text(16, 1.8, "LOW", fontsize=8, color="#2A9D8F", alpha=0.5, fontstyle="italic")

colour_patches = [
    mpatches.Patch(color="#D7263D", label="High risk"),
    mpatches.Patch(color="#F4A261", label="Medium risk"),
    mpatches.Patch(color="#2A9D8F", label="Low risk"),
]
marker_patches = [
    plt.scatter([], [], marker="o", color="grey", s=80, label="Journey 1"),
    plt.scatter([], [], marker="s", color="grey", s=80, label="Journey 2"),
    plt.scatter([], [], marker="^", color="grey", s=80, label="Journey 3"),
    plt.scatter([], [], marker="D", color="grey", s=80, label="Journey 4"),
]

legend1 = ax.legend(handles=colour_patches + [plt.Line2D([0],[0], color="#888", linestyle="-.", label=f"Trend (R²={r_value**2:.2f})")],
                    loc="upper right", fontsize=9, title="Risk Classification")
ax.add_artist(legend1)
ax.legend(handles=marker_patches, loc="center right", fontsize=9, title="Journey")

plt.tight_layout()
plt.savefig("scatter_v3.png", dpi=150, bbox_inches="tight")
plt.close()
