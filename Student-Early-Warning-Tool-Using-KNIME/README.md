# Student Early Warning Tool

## Project Overview
This repository contains a machine learning workflow developed in KNIME Analytics Platform to predict student academic risk. The primary objective is to identify students who may require additional academic support by classifying them as either **At Risk** or **Not At Risk**.

This project serves as a deliverable for CS0065 (Intelligent Systems) Asynchronous Activity 1.

## Repository Structure

- `DemoEarlyWarningTool.knwf`: The exported KNIME workflow containing the data pipeline and machine learning models.
- `student_performance_knime.csv`: The synthetic classroom dataset used for model training and evaluation.

## Data Description
The dataset contains historical academic examples. The `student_id` variable is explicitly excluded from model training to prevent target leakage and ensure the model learns generalized patterns.

- **Input Features (X):** `attendance`, `quiz_score`, `assignment_score`, `exam_score`
- **Target Label (y):** `risk_status` (Binary Category: At Risk / Not At Risk)

## Methodology & Algorithms
This project frames the objective as a supervised binary classification task. The KNIME workflow trains, partitions, and evaluates three different algorithms to compare their predictive capabilities:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
*Note on Evaluation:* Model evaluation heavily prioritizes **Recall** for the "At Risk" class to minimize false negatives and ensure students needing intervention are not overlooked.

## Usage Instructions
To reproduce this workflow on your local machine:

1. **Download Repository:** Clone or download this GitHub repository to your local drive.
2. **Import Workflow:**
- Open KNIME Analytics Platform.
- Navigate to `File` > `Import KNIME Workflow...`
- Choose "Select archive file", browse for `DemoEarlyWarningTool.knwf`, and click **Finish**.
3. **Configure Data Source:**
- Double-click the **CSV Reader** node at the start of the pipeline.
- Update the file path to point to the `student_performance_knime.csv` file stored in your downloaded repository folder, then click **OK**.
4. **Execute Pipeline:**
- Click the **Execute All Executable Nodes** button on the top toolbar (or press `Shift + F7`).
5. **View Results:**
- Right-click any of the **Scorer** nodes at the end of the branches and select **View: Confusion Matrix** or **Accuracy Statistics** to inspect the model's performance.

## Author

- **Ezekiel Ibasco**