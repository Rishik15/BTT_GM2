# SRI – Predicting and Measuring Grit in Leaders

## **Team Members**

| Name    | GitHub Handle | Contribution                                                                 |
| ------- | ------------- | ---------------------------------------------------------------------------- |
| Rishik  | @Rishik15     | BaselineModeling, FeatureSelection, StreamlitApplication                     |
| Fida    | @fibi5        | EDA, Data Preperation, Regression Model Training and Tuning, Task Management |
| Rithika | @rashok1      | Data Cleaning/Preprocessing, EDA, Classification Model Training              |
| Annie   | @annie251     | EDA, Data Cleaning, Data Preprocessing, Documentation                        |
| Amal    | @AmalBilal1   | EDA, Data Preprocessing                                                      |

## Project Overview

Investors often rely on both financial data and leadership qualities when making funding decisions. Leadership plays a critical role in a company’s success, and research shows that “grit”—a combination of perseverance and passion—is a strong predictor of long-term success.

This project explores methods to estimate grit in individuals, especially leaders (e.g., CEOs), with the ultimate goal of designing a lightweight, data-driven grit survey that can support investment decision-making.

## Problem Statement

We aim to answer two key questions:

1. **What are the main predictors of grit in an individual?**
2. **Can we design a survey that reliably estimates whether or not an individual demonstrates grit?**

## Datasets

We will leverage well-established psychological datasets:

- **Duckworth’s Grit Data** – includes grit scores from validated surveys.
- **Cattell’s 16 Personality Factors Test** – focuses on personality traits; we will pay special attention to “self-reliance” as a proxy for grit.

## Project Roadmap

### **Month 1: Data Cleaning & Exploration (by end of September)**

- Gather and clean grit-related datasets (resolve missing or inconsistent data).
- Exploratory Data Analysis (EDA):
  - Correlate grit scores with personality traits.
  - Compare demographic distributions across datasets.

### **Month 2: ML Model Building & Testing (by end of October)**

- Train regression and classification models to predict grit.
- Address class imbalance, particularly for underrepresented groups.
- Evaluate models with standard metrics (accuracy, F1, ROC-AUC) and **bias/fairness metrics**.
- Use **SHAP values** to identify top predictors of grit.

### **Month 3: Solution Delivery (by end of November / early December)**

- Draft a lightweight **grit survey** for use with funding applicants.
- Build a prototype **Streamlit app** to administer the survey.
- Deliver a final report summarizing:
  - Key predictive factors of grit.
  - Model limitations and generalizability concerns.
  - Recommendations for future improvements and scaling.

## **Next Steps**

### **Regression Model Limitations & Future Improvements**

While the final regression model (XGBoost) achieves solid and competitive performance, several limitations and opportunities for improvement remain:

- Future work could explore leveraging XGBoost’s built-in feature importance metrics or SHAP-based feature ranking to select the top predictors in a way that is more tightly aligned with the model’s internal decision-making process.
- Additional performance gains may be possible through feature engineering, such as:
  - Interaction features between key personality traits
  - Nonlinear transformations of existing variables
  - Aggregated or composite features that better capture behavioral patterns
- While XGBoost was chosen for its strong performance and robustness, experimenting with alternative models (e.g., ensemble stacking, neural networks, or regularized nonlinear models) may further improve predictive accuracy or generalizability.

## **License**

MIT License

Copyright (c) 2025 SRI – Predicting and Measuring Grit in Leaders

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

## **References** (Optional but encouraged)

Cite relevant papers, articles, or resources that supported your project.

## **Acknowledgements** (Optional but encouraged)

Thank your Challenge Advisor, host company representatives, TA, and others who supported your project.

## Tech Stack

- **Python** (pandas, scikit-learn, SHAP, matplotlib/seaborn)
- **Jupyter Notebooks** for data exploration & model building
- **Streamlit** for prototype survey app
- **Git/GitHub** for version control & collaboration

## **Setup and Installation**

## Running the Streamlit App

### 1. Clone the repository

First, clone the project repository to your local machine using Git:

```bash
git clone https://github.com/Rishik15/BTT_GM2.git
```

After cloning, move into the project directory:

```
cd BTT_GM2
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

From the project root directory:

```bash
pip install -r requirements.txt
```

### 4. Navigate to the Streamlit app folder

```bash
cd streamlit_app
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will be available at http://localhost:8501.
To stop the app, press Ctrl + C.
