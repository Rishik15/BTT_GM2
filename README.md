# SRI – Predicting and Measuring Grit in Leaders

## 👥 **Team Members**

| Name    | GitHub Handle | Contribution                                                                 |
| ------- | ------------- | ---------------------------------------------------------------------------- |
| Rishik  | @Rishik15     | BaselineModeling, FeatureSelection, StreamlitApplication                     |
| Fida    | @fibi5        | EDA, Data Preperation, Regression Model Training and Tuning, Task Management |
| Rithika | @rashok1      | Data Cleaning/Preprocessing, EDA, Classification Model Training              |
| Annie   | @annie251     | EDA, Data Cleaning, Data Preprocessing, Documentation                        |
| Amal    | @AmalBilal1   | EDA, Data Preprocessing                                                      |

## 📌 Project Overview

Investors often rely on both financial data and leadership qualities when making funding decisions. Leadership plays a critical role in a company’s success, and research shows that “grit”—a combination of perseverance and passion—is a strong predictor of long-term success.

This project explores methods to estimate grit in individuals, especially leaders (e.g., CEOs), with the ultimate goal of designing a lightweight, data-driven grit survey that can support investment decision-making.

## 🚩 Problem Statement

We aim to answer two key questions:

1. **What are the main predictors of grit in an individual?**
2. **Can we design a survey that reliably estimates whether or not an individual demonstrates grit?**

## 📊 Datasets

We will leverage well-established psychological datasets:

- **Duckworth’s Grit Data** – includes grit scores from validated surveys.
- **Cattell’s 16 Personality Factors Test** – focuses on personality traits; we will pay special attention to “self-reliance” as a proxy for grit.

## 🗺️ Project Roadmap

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

## 🚀 **Next Steps**

**You might consider addressing the following (as applicable):**

- What are some of the limitations of your model?
- What would you do differently with more time/resources?
- What additional datasets or techniques would you explore?

## 📝 **License**

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

## 📄 **References** (Optional but encouraged)

Cite relevant papers, articles, or resources that supported your project.

## 🙏 **Acknowledgements** (Optional but encouraged)

Thank your Challenge Advisor, host company representatives, TA, and others who supported your project.

## ⚙️ Tech Stack

- **Python** (pandas, scikit-learn, SHAP, matplotlib/seaborn)
- **Jupyter Notebooks** for data exploration & model building
- **Streamlit** for prototype survey app
- **Git/GitHub** for version control & collaboration

## 📂 Repository Structure

## 👩🏽‍💻 **Setup and Installation**

**Provide step-by-step instructions so someone else can run your code and reproduce your results. Depending on your setup, include:**

- How to clone the repository
- How to install dependencies
- How to set up the environment
- How to access the dataset(s)
- How to run the notebook or scripts
