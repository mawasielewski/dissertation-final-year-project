import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv

PENALTY_LABELS = {
    "interchange_base":   "Interchange Base",
    "complexity_high":    "Complexity High",
    "complexity_medium":  "Complexity Medium",
    "complexity_low":     "Complexity Low",
    "lift_high":          "Lift High",
    "lift_moderate":      "Lift Moderate",
    "lift_low":           "Lift Low",
    "destination_penalty":"Destination Penalty",
}

ROUTE_ORDER = [
    "J1 Route 1", "J1 Route 2", "J1 Route 3",
    "J2 Route 1", "J2 Route 2", "J2 Route 3",
    "J3 Route 1", "J3 Route 2", "J3 Route 3",
    "J4 Route 1", "J4 Route 2", "J4 Route 3",
]

ROUTE_SHORT = {
    "J1 Route 1": "J1 R1", "J1 Route 2": "J1 R2", "J1 Route 3": "J1 R3",
    "J2 Route 1": "J2 R1", "J2 Route 2": "J2 R2", "J2 Route 3": "J2 R3",
    "J3 Route 1": "J3 R1", "J3 Route 2": "J3 R2", "J3 Route 3": "J3 R3",
    "J4 Route 1": "J4 R1", "J4 Route 2": "J4 R2", "J4 Route 3": "J4 R3",
}

CLASS_COLOUR = {"HIGH": "#D7263D", "MEDIUM": "#F4A261", "LOW": "#2A9D8F"}

penalties = list(PENALTY_LABELS.keys())

# Load data
data = {}
with open("sensitivity_results.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        route = row["route"]
        penalty = row["penalty"]
        if route not in data:
            data[route] = {}
        data[route][penalty] = {
            "base":       float(row["base_score"]),
            "base_class": row["base_class"],
            "low":        float(row["low_score"]),
            "high":       float(row["high_score"]),
        }

# Build score range matrix (high - low = total variation)
matrix = np.zeros((len(ROUTE_ORDER), len(penalties)))
for i, route in enumerate(ROUTE_ORDER):
    for j, pen in enumerate(penalties):
        d = data[route][pen]
        matrix[i, j] = round(d["high"] - d["low"], 2)

fig, ax = plt.subplots(figsize=(11, 6))

im = ax.imshow(matrix, cmap="YlOrRd", aspect="auto", vmin=0, vmax=1.5)

# Axis labels
ax.set_xticks(range(len(penalties)))
ax.set_xticklabels([PENALTY_LABELS[p] for p in penalties], fontsize=9, rotation=20, ha="right")
ax.set_yticks(range(len(ROUTE_ORDER)))
ax.set_yticklabels([ROUTE_SHORT[r] for r in ROUTE_ORDER], fontsize=9)

# Colour route labels by risk class
for i, route in enumerate(ROUTE_ORDER):
    cls = data[route]["interchange_base"]["base_class"]
    ax.get_yticklabels()[i].set_color(CLASS_COLOUR[cls])
    ax.get_yticklabels()[i].set_fontweight("bold")

# Annotate each cell with the range value
for i in range(len(ROUTE_ORDER)):
    for j in range(len(penalties)):
        val = matrix[i, j]
        text_colour = "white" if val > 0.9 else "black"
        ax.text(j, i, f"{val:.1f}", ha="center", va="center",
                fontsize=8, color=text_colour)

cbar = fig.colorbar(im, ax=ax, shrink=0.8, pad=0.02)
cbar.set_label("Score range under ±20% variation", fontsize=9)

ax.set_title(
    "Sensitivity Analysis - Score Range Under +- 20% Penalty Weight Variation\n"
    "Cell values show total score movement (high - low). No route changes risk classification.",
    fontsize=11, fontweight="bold", pad=12
)

# Risk class legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#D7263D", label="HIGH risk"),
    Patch(facecolor="#F4A261", label="MEDIUM risk"),
    Patch(facecolor="#2A9D8F", label="LOW risk"),
]
ax.legend(handles=legend_elements, loc="lower right",
          bbox_to_anchor=(1.18, -0.02), fontsize=8, framealpha=0.9)

plt.tight_layout()
plt.savefig("heatmap_sensitivity.png", dpi=150, bbox_inches="tight")
plt.close()
print("Done")
