# 🏦 Bank Customer Churn Prediction using Machine Learning

## 📌 **Project Overview**
This project predicts whether a bank customer is likely to churn (leave the bank) based on demographic and financial information.
Machine learning techniques are applied to analyze customer behavior and build a predictive classification model that helps banks improve customer retention strategies.

---

## 🎯 **Objective**
- Analyze customer data to understand churn patterns
- Predict customer churn using machine learning
- Evaluate model performance using classification metrics
- Identify key factors influencing customer attrition

---

## 📊 **Dataset Description**
- **Dataset Name:** Churn Modeling.csv
- **Total Records:** ~10,000

### 🔑 **Features**:
- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary


### 🎯 Target Variable
- **Exited**  
  - `0` → Not Churned  
  - `1` → Churned

---

## 🛠️ **Tools & Technologies**
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Environment:** Jupyter Notebook / Google Colab

---

## 🔍 **Steps Performed**
- Data loading and inspection
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature encoding and scaling
- Train-test data splitting
- Model training
- Model evaluation using classification metrics

--- 

## 🤖 **Model Used**
- **Algorithm:**
- Logistic Regression
- Random Forest Classifier
- K-Nearest Neighbours(KNN)
- Decision Tree
- **Problem Type:** Binary Classification

---
  
## 📈 Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC Score

---

## 📈 **Results**
- The model successfully predicts customer churn with reasonable accuracy
- Recall and ROC-AUC were prioritized to identify churn-prone customers
- The analysis shows churn is influenced by factors such as age, balance, and geography

---

## 🚀 **How to Run**
```bash
1. Clone the repository
git clone https://github.com/Addychauhan/Data-Analysis.git

2. Navigate to the project directory
cd Data-Analysis/Customer-churn-prediction

3. Open and run the notebook
- Open `bank_customer_churn_prediction.ipynb` in Jupyter Notebook or Google Colab
- Run all cells sequentially to train and evaluate the model





