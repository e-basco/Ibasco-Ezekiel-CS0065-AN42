# TA3 - Case Study 2: AI-Based Legal Decision Support System

This folder contains the third technical assessment for the Intelligent Systems course. The project focuses on a case-based reasoning (CBR) prototype for a legal decision support system.

## Overview

The case study models a simplified AI-based legal analysis workflow that compares a new legal problem against a set of past cases to recommend a suitable legal strategy. The system evaluates similarities across several factors, including:

- offense type
- communication channel
- available evidence
- intent level
- financial loss
- prior record

The prototype then reuses and adapts the most relevant past solution to the new case, producing a revised recommendation that reflects the current context.

## Files in this folder

- `TA3 - Technical Assessment.pdf` — the official assessment document
- `TA3_Ibasco.pdf` — the student submission PDF
- `case_study_2.ipynb` — the interactive notebook implementation of the case-based reasoning workflow
- `case_study_2.py` — the Python script version of the same prototype
- `README.md` — summary of the assessment and project purpose

## Learning objectives

- Understand the concept of case-based reasoning in AI
- Represent legal problems and solutions as structured case data
- Compare new cases to stored past cases using similarity metrics
- Reuse relevant legal arguments and recommended actions
- Adapt prior solutions to fit new problem details
- Retain solved cases for future reuse

## Project description

The system in this folder is designed as an academic prototype and is explicitly not legal advice. It demonstrates a simplified approach to legal decision support by:

- storing historical legal scenarios in a case base
- retrieving the most similar prior cases
- calculating weighted similarity scores across key attributes
- adapting the retrieved legal reasoning to a new case
- saving the newly solved case for future reference

The assessed scenario involves a theft case involving electronic transfer, with relevant evidence such as transaction logs, device records, and messages. The prototype identifies the closest past cases and generates a revised legal strategy based on their similarities.

## Technical focus

The implementation includes:

- structured case representation for legal problems and solutions
- weighted similarity calculation
- evidence overlap using set-based comparison
- financial loss comparison
- intent similarity based on severity levels
- adaptation logic for new legal problems
- case retention in the case base

## Author

Ezekiel M. Ibasco

## Course

CS0065 (Intelligent Systems) — Section AN42
