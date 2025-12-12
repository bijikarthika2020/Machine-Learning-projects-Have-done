# Machine-Learning-projects-Have-done
Sonar Rock vs Mine Classification Using Logistic Regression
📌 Project Overview

This project applies Logistic Regression to classify whether a sonar signal corresponds to a rock or a metal mine.
The dataset contains 60 sonar frequency features, with each row representing the energy of sonar signals bounced off underwater objects.

This is a well-known binary classification problem and demonstrates how logistic regression can be used for real-world predictive modeling.

🧠 Objectives

Build a classification model to predict Rock (R) or Mine (M).

Perform data preprocessing and train-test split.

Train and evaluate a Logistic Regression model.

Measure performance using accuracy and confusion matrix.

📂 Dataset Information

Dataset: Sonar, Mines vs Rocks (UCI Repository)

Samples: 208 instances

Features: 60 numerical features

Target values:

R → Rock

M → Mine

🛠 Technologies Used

Python

NumPy

Pandas

Scikit-learn

Matplotlib / Seaborn (optional for visualization)

🔧 Project Workflow

Load the dataset

Exploratory Data Analysis

Data preprocessing

Split data into training and test sets

Train Logistic Regression model

Evaluate the model

Predict for new sonar values (optional)

📊 Model Performance
Metric	Score
Training Accuracy	83%
Testing Accuracy	74%


📈 Confusion Matrix

A confusion matrix was used to evaluate model performance on test data.

TP – Correct prediction (Mines)
TN – Correct prediction (Rocks)
FP – Incorrect prediction
FN – Incorrect prediction
