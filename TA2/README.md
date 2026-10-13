# TA2 - Rule-Based Vacuum Cleaner Agent

This folder contains the second technical assessment for the Intelligent Systems course. The project focuses on a simple rule-based agent that navigates a two-room environment and cleans dirty rooms.

## Overview

The simulation models a vacuum cleaner agent operating in a two-room environment:

- Room A
- Room B

The agent follows a basic decision policy:

1. If the current room is dirty, it cleans it.
2. If the current room is already clean, it moves to the other room.

This demonstrates a simple form of agent behavior in an environment with clearly defined rules and state transitions.

## Files in this folder

- `TA2 - Technical Assessment.pdf` — the official assessment document
- `clean_a_room.ipynb` — the Jupyter notebook with the implementation and simulation
- `README.md` — overview and usage notes for the assessment

## Learning objectives

- Understand the concept of a rule-based intelligent agent
- Represent an environment as a set of states
- Implement decision rules for simple agent behavior
- Simulate agent actions over multiple steps
- Validate user input and handle invalid states safely

## Notebook details

The notebook implements:

- environment creation for two rooms
- state validation (`Dirty` or `Clean`)
- a vacuum cleaner agent class
- movement between rooms
- perception and action logic
- interactive or sample-based simulation execution

It also includes a sample demonstration where the environment is initialized with specific room states and the agent runs for a set number of steps.

## Requirements

To run the notebook successfully, you need:

- Python 3.x
- Jupyter Notebook or VS Code with notebook support
- Standard Python libraries only

## Author

Ezekiel M. Ibasco

## Course

CS0065 (Intelligent Systems) — Section AN42
