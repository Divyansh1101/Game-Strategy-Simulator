# 🎮 Game Strategy Simulator  

A **minimal game theory toolkit** to build, simulate, and analyze payoff matrices. This project provides tools for studying strategic interactions like the **Prisoner’s Dilemma**, **Coordination Games**, and more, with visualization support.  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)  
![Last Commit](https://img.shields.io/github/last-commit/Divyansh1101/Game-Strategy-Simulator?style=flat-square)  
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)  

---

## ✨ Features  

- 📚 **Built-in Game Examples** – Includes classic cases like Prisoner’s Dilemma.  
- 🧮 **Nash Equilibrium Computation** – Powered by [nashpy](https://github.com/drvinceknight/nashpy), with graceful fallbacks.  
- 🔥 **Visualization Tools** – Generate **heatmaps** for both players’ payoff distributions.  
- ⚡ **Lightweight & Extensible** – Easy to extend with your own games and strategies.  

---

## 📂 Project Structure  

```
Game-Strategy-Simulator/
│── main.py                # Entry point for running simulations
│── requirements.txt       # Python dependencies
│── examples/              # Pre-built game setups
│── utils/                 # Helper functions for analysis & visualization
│── README.md              # Project documentation
```

---

## 🚀 Getting Started  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Divyansh1101/Game-Strategy-Simulator.git
cd Game-Strategy-Simulator
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Simulator  
```bash
python main.py
```

---

## 🔧 Usage Examples  

### 1. Define a Custom Game  
```python
import nashpy as nash
import numpy as np

# Define payoff matrices
A = np.array([[3, 0], [5, 1]])  # Player 1
B = np.array([[3, 5], [0, 1]])  # Player 2

# Create the game
game = nash.Game(A, B)
print("Game created:", game)
```

---

### 2. Compute Nash Equilibria  
```python
# Find Nash equilibria using support enumeration
equilibria = game.support_enumeration()
for eq in equilibria:
    print("Nash Equilibrium:", eq)
```

---

### 3. Visualize Payoff Heatmaps  
```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(A, annot=True, cmap="Blues", cbar=False)
plt.title("Player 1 Payoffs")
plt.show()

sns.heatmap(B, annot=True, cmap="Oranges", cbar=False)
plt.title("Player 2 Payoffs")
plt.show()
```

✅ These visualizations help compare **strategies and payoffs** intuitively.  

---

## 📊 Example Output  

- **Game Matrix Example (Prisoner’s Dilemma):**  
  Visualizes payoff matrix with equilibrium points.  

- **Heatmap Visualization:**  
  Both players’ payoffs shown in intuitive color-coded grids.  

*(Insert screenshots or generated plots here for better presentation!)*  

---

## ⚙️ Requirements  

- Python **3.9+**  
- Dependencies listed in `requirements.txt`  

---

## 📜 License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  

---

## 🤝 Contributing  

Contributions are welcome!  
- Fork the repo  
- Create a feature branch (`git checkout -b feature-name`)  
- Commit changes & open a PR  

---

## 🙌 Acknowledgements  

- [nashpy](https://github.com/drvinceknight/nashpy) for Nash Equilibria computation.  
- Game theory fundamentals from **John Nash** and classic strategic interaction models.  
