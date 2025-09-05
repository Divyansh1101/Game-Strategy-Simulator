import os
import numpy as np

print("Starting Game Strategy Simulator...")

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# ------- Try to import nashpy; provide fallback -------
nash_available = True
try:
    import nashpy as nash
except Exception as e:
    print("`nashpy` not available, falling back to pure-strategy enumeration only:", e)
    nash_available = False

# ------- Helper: pure-strategy NE finder -------
def pure_nash_equilibria(A, B):
    # A: payoff for Player 1, B: payoff for Player 2 (same shape)
    A = np.array(A); B = np.array(B)
    m, n = A.shape
    best_rows = (A == A.max(axis=0, keepdims=True))
    best_cols = (B == B.max(axis=1, keepdims=True))
    equilibria = []
    for i in range(m):
        for j in range(n):
            if best_rows[i, j] and best_cols[i, j]:
                equilibria.append((i, j))
    return equilibria

# ------- Define games -------
# Prisoner's Dilemma (2x2): Actions C (Cooperate), D (Defect)
A_pd = np.array([[-1, -3], [0, -2]])  # Player 1
B_pd = np.array([[-1, 0], [-3, -2]])  # Player 2

# A sample 3x3 game
A_3 = np.array([
    [3, 1, 2],
    [2, 3, 0],
    [0, 4, 1],
])
B_3 = np.array([
    [2, 3, 1],
    [3, 1, 2],
    [4, 0, 3],
])

games = {
    "prisoners_dilemma": (A_pd, B_pd, ["C","D"], ["C","D"]),
    "three_by_three": (A_3, B_3, ["A1","A2","A3"], ["B1","B2","B3"]),
}

# ------- Compute equilibria and save -------
report_lines = []
for name, (A, B, rlabels, clabels) in games.items():
    report_lines.append(f"Game: {name}")
    report_lines.append(f"A (P1) =\n{A}")
    report_lines.append(f"B (P2) =\n{B}")
    # Pure equilibria
    pure_eq = pure_nash_equilibria(A, B)
    if pure_eq:
        for (i, j) in pure_eq:
            report_lines.append(f"Pure NE at ({rlabels[i]}, {clabels[j]}) with payoffs ({A[i,j]}, {B[i,j]})")
    else:
        report_lines.append("No pure-strategy NE found.")
    # Mixed equilibria via nashpy if available
    if nash_available:
        game = nash.Game(A, B)
        try:
            equilibria = list(game.support_enumeration())
            if equilibria:
                for p1, p2 in equilibria:
                    report_lines.append(f"Mixed NE (support enumeration) -> P1: {np.round(p1,3)}, P2: {np.round(p2,3)}")
            else:
                report_lines.append("No mixed-strategy equilibria returned by nashpy.")
        except Exception as e:
            report_lines.append(f"nashpy support enumeration failed: {e}")
    else:
        report_lines.append("nashpy missing: skipped mixed-strategy computation.")
    report_lines.append("")

# Save equilibria report
report_path = os.path.join(RESULTS_DIR, "equilibria.txt")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))
print(f"Saved equilibria -> {report_path}")

# ------- Heatmap visualizations -------
import matplotlib.pyplot as plt
import seaborn as sns

def save_heatmaps(A, B, name, rlabels, clabels):
    plt.figure()
    sns.heatmap(A, annot=True, fmt=".1f", xticklabels=clabels, yticklabels=rlabels)
    plt.title(f"P1 Payoff Heatmap: {name}")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, f"{name}_P1_heatmap.png"), dpi=150)
    plt.close()

    plt.figure()
    sns.heatmap(B, annot=True, fmt=".1f", xticklabels=clabels, yticklabels=rlabels)
    plt.title(f"P2 Payoff Heatmap: {name}")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, f"{name}_P2_heatmap.png"), dpi=150)
    plt.close()

for name, (A, B, rlabels, clabels) in games.items():
    save_heatmaps(A, B, name, rlabels, clabels)

print("Done.")
