# Game Strategy Simulator

    ![Last Commit](https://img.shields.io/github/last-commit/Divyansh1101/game-strategy-simulator)
![CI](https://github.com/Divyansh1101/game-strategy-simulator/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

    A minimal game theory toolkit to build payoff matrices, compute Nash equilibria (pure and mixed via `nashpy`), and visualize payoffs as heatmaps. If `nashpy` is missing, the script falls back to pure-strategy enumeration.

    ## Features
    - Built-in examples: Prisoner’s Dilemma (2x2) and a 3x3 game
- Nash equilibria via `nashpy` with graceful fallback
- Heatmap visualizations for both players’ payoffs

    ## Requirements
    - Python 3.9+

    ## Setup & Usage
    ```bash
    pip install -r requirements.txt
    python main.py
    ```

    Outputs are saved to the `results/` folder.

    ## License
    MIT © 2025 Divyansh1101
