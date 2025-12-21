# Customer Churn Classification — Azure-Style ML Project
## 📌 Project Overview

This project implements an end-to-end customer churn classification pipeline using Python and scikit-learn, designed following Azure Machine Learning (Azure ML) best practices.

The focus is on:

* clean project structure

* configuration-driven pipelines

* reproducibility

* cloud portability

The solution predicts whether a customer is likely to churn based on demographic, service usage, and contract-related features.

----------------------------------------------------------------------------------------------------------------
## 🎯 Problem Statement

Customer churn is a critical business problem in marketing and subscription-based services.
The objective of this project is to:

* build a binary classification model to predict churn

* preprocess mixed numerical and categorical features

* train and evaluate a baseline model

* produce artifacts (model + metrics) in a reproducible manner

----------------------------------------------------------------------------------------------------------------

☁️ Azure-Style Design Philosophy

This project is intentionally structured to be Azure ML–compatible, even though the training is executed locally.

## Why no Azure ML Workspace is created?

In many real-world organizations:

* Azure ML workspaces are pre-provisioned by cloud or IT teams

* Individual developers do not have permission to create or modify infrastructure

* ML engineers focus on pipeline design, training logic, and reproducibility

To reflect this realistic enterprise setup, the project:

* does not create an Azure ML workspace in code

* follows the same folder structure and execution pattern used in Azure ML jobs

* can be migrated to Azure ML without code changes

This mirrors how ML projects are developed in regulated or policy-restricted environments.

-------------------------------------------------------------------------------------------------

## 🗂️ Project Structure

```text
Customer_Churn_Analysis/
├── data/
│   └── telco_churn.xlsx
├── scripts/
│   ├── main.py          # Pipeline entry point
│   ├── preprocessing.py
│   ├── train.py
│   └── evaluate.py
├── config/
│   └── config.yaml      # Centralized configuration
├── outputs/
│   ├── model.pkl        # Trained model artifact
│   └── metrics.json     # Evaluation results
├── requirements.txt
└── README.md
```


## Design principles:

* scripts/ → modular pipeline steps (Azure ML style)

* config/ → config-driven execution

* outputs/ → versionable ML artifacts

* single entry point (main.py) → easy orchestration
  
---------------------------------------------------------------------------------

## ⚙️ Configuration-Driven Execution

All parameters are defined in config/config.yaml:
```
project:
  name: customer_churn_ml
  version: 1.0

data:
  path: data/telco_churn.xlsx
  target: Churn

training:
  test_size: 0.2
  random_state: 42
  model: logistic_regression

```
This approach ensures:

reproducibility

easy experimentation

cloud portability

🔄 Pipeline Flow

Preprocessing

Load Excel data

Encode target variable

One-hot encode categorical features

Split into train/test sets

Training

Logistic Regression baseline model

Model persistence using joblib

Evaluation

Accuracy computation

Metrics saved as JSON for tracking

▶️ How to Run
1. Create environment
pip install -r requirements.txt

2. Run pipeline
python scripts/main.py

3. Outputs

After execution:

outputs/
├── model.pkl
└── metrics.json

📊 Model Output

Model: Logistic Regression

Metric: Accuracy (baseline)

Artifacts: Serialized model + evaluation metrics

This baseline can be extended with:

regularization tuning

tree-based models

feature importance analysis

experiment tracking

🚀 Azure ML Migration Path

This project can be moved to Azure ML by:

registering scripts/main.py as an Azure ML job

attaching a pre-existing workspace

using Azure ML compute targets

logging metrics via MLflow

No refactoring of core logic is required.

🧠 Key Takeaways

Demonstrates production-style ML pipeline design

Separates infrastructure concerns from ML logic

Mirrors how ML projects are developed in enterprise Azure environments

Fully reproducible and cloud-ready

📌 Next Improvements

Add MLflow experiment tracking

Add confusion matrix and ROC curve

Introduce feature importance analysis

Integrate CI/CD for model validation

👤 Author

Marzieh Eskandari
Master of Applied Science (Engineering)
Focus: Data Science, Predictive Analytics, Optimization
