# TA1 - Random Walk Simulation Using AgentPy

This folder contains the Technical Assessment for the CS0065 Intelligent Systems laboratory activity on random walk simulations.

## Overview

The assessment focuses on modeling multiple agents moving randomly on a grid using AgentPy, a Python library for agent-based modeling. The exercises in this folder explore:

- grid-based random movement
- bounded movement within simulation limits
- multiple-agent behavior and occupancy patterns
- visualization of motion over time
- final position analysis and agent spread

## Files in this folder

- `TA1 - Technical Assessment.docx` — the official lab brief and assessment instructions
- `random_walk.ipynb` — the Jupyter notebook implementing and analyzing the random walk model
- `README.md` — project summary and usage notes

## Learning objectives

- Understand the concept of a random walk in a grid environment
- Implement a multi-agent simulation using Python and AgentPy
- Visualize agent movement over time
- Analyze final positions, distribution, and randomness effects
- Compare different simulation scenarios using reproducible parameters

## Notebook details

The notebook demonstrates a random walk model where each agent:

- starts at a random position on the grid
- moves one step at a time in a random or preference-based direction
- stays within the grid boundaries
- records its path for later analysis

It also includes additional simulation logic for:

- collision avoidance (agent spacing)
- directional preference
- scenario comparison across multiple runs
- summary tables and visual outputs

## Requirements

To run the notebook successfully, the following tools are recommended:

- Python 3.x
- Jupyter Notebook or VS Code with notebook support
- AgentPy
- NumPy
- Matplotlib
- Pandas

A virtual environment is already provided in the project root under `agentpy_env/`, which is suitable for running the simulation.


If using VS Code, simply open `TA1/random_walk.ipynb` and run the cells in order.

## Author

Ezekiel M. Ibasco

## Course

CS0065 (Intelligent Systems) — Section AN42
