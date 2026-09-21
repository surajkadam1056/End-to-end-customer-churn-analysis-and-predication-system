# 📊 End-to-End Customer Churn Analytics & Prediction System

An end-to-end **Customer Churn Analytics and Prediction System** that combines **Python, SQL, Machine Learning, Power BI, Flask API, and Postman** to analyze customer behavior, identify churn patterns, and predict whether a customer is likely to churn.

The project covers the complete data analytics and machine learning workflow — from data preprocessing and SQL analysis to model development, business intelligence dashboards, and API-based predictions.

---

## 🎯 Project Objective

Customer churn is an important business problem where companies need to identify customers who are likely to stop using their products or services.

The objective of this project is to:

* Analyze customer behavior and purchasing patterns
* Identify factors associated with customer churn
* Perform customer segmentation and KPI analysis using SQL
* Build and compare multiple Machine Learning classification models
* Predict customer churn using the trained model
* Create an interactive Power BI dashboard
* Deploy the prediction model through a Flask API
* Test the API using Postman

---

## 🚀 Project Highlights

* 📊 **50,000+ customer records**
* 🤖 Multiple Machine Learning classification models
* 🌲 Random Forest achieved approximately **91% accuracy**
* 🗄️ SQL-based customer analysis and segmentation
* 📈 Interactive Power BI dashboard
* 🌐 Flask REST API for predictions
* 🧪 Postman API testing
* 🔍 Feature engineering and customer risk classification
* 📦 Complete end-to-end analytics workflow

---

## 🛠️ Technologies Used

| Technology           | Purpose                                           |
| -------------------- | ------------------------------------------------- |
| **Python**           | Data preprocessing, analysis and Machine Learning |
| **Pandas**           | Data manipulation                                 |
| **NumPy**            | Numerical operations                              |
| **Matplotlib**       | Data visualization                                |
| **Seaborn**          | Statistical visualization                         |
| **Scikit-learn**     | Machine Learning                                  |
| **MySQL**            | Database and SQL analysis                         |
| **Power BI**         | Interactive dashboard                             |
| **Flask**            | Machine Learning API                              |
| **Postman**          | API testing                                       |
| **Jupyter Notebook** | Model development and experimentation             |
| **GitHub**           | Version control and project management            |

---

# 📂 Project Structure

```text
End-to-end-customer-churn-analysis-and-predication-system/
│
├── App/
│   └── Final app/
│       ├── app.py
│       ├── model.pkl
│       ├── scaler.pkl
│       └── columns.pkl
│
├── Dashboard/
│   └── Power BI Dashboard
│
├── Dataset/
│   └── Customer Churn Dataset
│
├── Notebooks/
│   ├── Data Cleaning
│   ├── EDA
│   ├── Feature Engineering
│   └── Machine Learning
│
├── Project Documentation/
│   └── Project documentation files
│
├── Project overview/
│   └── Project overview
│
├── SQL/
│   └── SQL analysis queries
│
├── reports/
│   └── Project reports
│
├── .gitignore
│
└── README.md
```

---

# 📊 Dataset

The project uses customer-level transactional and behavioral data.

### Important Features

```text
Age
Gender
Country
City
Membership_Years
Login_Frequency
Session_Duration_Avg
Pages_Per_Session
Total_Purchases
Average_Order_Value
Lifetime_Value
Credit_Balance
Signup_Quarter
Churned
```

### Target Variable

```text
Churned
```

The target represents whether a customer has churned:

```text
0 → Not Churned
1 → Churned
```

---

# 🔄 End-to-End Workflow

```text
Customer Dataset
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
SQL Analysis
       ↓
Customer Segmentation
       ↓
Machine Learning
       ↓
Model Evaluation
       ↓
Power BI Dashboard
       ↓
Flask API
       ↓
Postman Testing
```

---

# 🧹 1. Data Cleaning

The raw customer dataset is processed before analysis and model training.

Major preprocessing steps include:

* Checking missing values
* Checking duplicate records
* Handling data types
* Identifying numerical and categorical features
* Preparing data for Machine Learning
* Encoding categorical variables
* Feature scaling where required

---

# 🔎 2. Exploratory Data Analysis

EDA is performed to understand customer behavior and identify patterns related to churn.

### Analysis Areas

* Customer demographics
* Membership duration
* Login frequency
* Session duration
* Pages viewed per session
* Purchase behavior
* Average order value
* Customer lifetime value
* Credit balance
* Churn distribution

Visualization techniques include:

* Histograms
* Count plots
* Box plots
* Correlation analysis
* Distribution plots
* Churn comparison charts

---

# ⚙️ 3. Feature Engineering

Additional features were created to improve customer analysis and interpretation.

### Engagement Score

A combined metric representing customer engagement based on behavioral activity.

### Average Purchase Value

Used to understand customer spending behavior.

### Customer Value

Used to categorize customers based on their overall business value.

### Risk Level

Customers can be categorized into different churn-risk groups based on behavioral and business indicators.

Example:

```text
Low Risk
Medium Risk
High Risk
```

---

# 🗄️ 4. SQL Analysis

MySQL is used for structured customer analysis and business-oriented queries.

SQL analysis includes:

* Customer segmentation
* Churn analysis
* Purchase analysis
* Customer value analysis
* KPI calculations
* Aggregations
* Group-wise analysis
* Filtering
* Sorting
* Joins
* Conditional analysis

### Example SQL Query

```sql
SELECT
    Churned,
    COUNT(*) AS customer_count,
    AVG(Lifetime_Value) AS avg_lifetime_value
FROM customers
GROUP BY Churned;
```

This helps compare customer count and average lifetime value between churned and non-churned customers.

---

# 🤖 5. Machine Learning

The project treats customer churn as a **binary classification problem**.

### Models Evaluated

#### Logistic Regression

Used as a baseline classification model.

Approximate accuracy:

```text
80.73%
```

#### Decision Tree

A tree-based classification model used to capture nonlinear relationships.

Approximate accuracy:

```text
84.69%
```

#### Random Forest

An ensemble learning model combining multiple decision trees.

Approximate accuracy:

```text
91.04%
```

### Model Comparison

| Model               | Accuracy |
| ------------------- | -------: |
| Logistic Regression |  ~80.73% |
| Decision Tree       |  ~84.69% |
| Random Forest       |  ~91.04% |

> Accuracy is based on the project's evaluation results. Model performance can vary depending on preprocessing, train/test split, and dataset version.

---

# 📈 6. Model Evaluation

The classification models are evaluated using metrics such as:

* Accuracy
* Confusion Matrix
* Classification Report
* Precision
* Recall
* F1-score

### Random Forest Confusion Matrix

```text
[[6945, 185],
 [ 701, 2169]]
```

The confusion matrix helps understand:

* True Negatives
* False Positives
* False Negatives
* True Positives

---

# 📊 7. Power BI Dashboard

Power BI is used to convert customer data and analysis results into an interactive business dashboard.

### Key KPIs

* 👥 Total Customers
* 🛒 Total Purchases
* 💰 Average Order Value
* 📉 Churn Rate
* 💎 Customer Lifetime Value

### Dashboard Analysis

The dashboard provides insights into:

* Overall churn rate
* Customer demographics
* Customer purchasing behavior
* Customer engagement
* Churn by customer segments
* High-value customers
* Customer risk levels
* Business KPIs

---

# 🌐 8. Flask API

The trained Machine Learning model is integrated into a Flask application.

The API allows users/applications to send customer information and receive a churn prediction.

### API Flow

```text
Client
  ↓
Flask API
  ↓
Input Validation
  ↓
Feature Preprocessing
  ↓
Scaler
  ↓
Trained ML Model
  ↓
Prediction
  ↓
JSON Response
```

---

# 🧪 9. Postman Testing

Postman is used to test the Flask API.

### Example Request

```http
POST /predict
```

Example JSON:

```json
{
    "Age": 30,
    "Gender": "Male",
    "Membership_Years": 3,
    "Login_Frequency": 15,
    "Session_Duration_Avg": 20,
    "Pages_Per_Session": 5,
    "Total_Purchases": 10,
    "Average_Order_Value": 750,
    "Lifetime_Value": 7500,
    "Credit_Balance": 1000
}
```

### Example Response

```json
{
    "prediction": 0
}
```

Where:

```text
0 → Customer is predicted as Not Churned
1 → Customer is predicted as Churned
```

---

# 💡 Business Insights

The system can help businesses:

* Identify customers at risk of churn
* Understand customer engagement patterns
* Identify high-value customers
* Analyze purchasing behavior
* Segment customers based on business value
* Monitor churn-related KPIs
* Support customer retention strategies

---

# 📌 Key Learning Outcomes

Through this project, the following practical skills were developed:

### Data Analytics

* Data cleaning
* EDA
* Feature engineering
* KPI analysis
* Customer segmentation

### SQL

* Database analysis
* Aggregation
* `GROUP BY`
* `HAVING`
* Joins
* Conditional logic
* Business queries

### Machine Learning

* Classification
* Train/test split
* Feature preprocessing
* Feature scaling
* Model comparison
* Model evaluation
* Random Forest
* Logistic Regression
* Decision Tree

### Business Intelligence

* Power BI
* Data modeling
* KPI cards
* Interactive visualizations
* Business dashboards

### Deployment

* Flask REST API
* Model serialization
* API testing
* Postman

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/surajkadam1056/End-to-end-customer-churn-analysis-and-predication-system.git
```

```bash
cd End-to-end-customer-churn-analysis-and-predication-system
```

---

## 2. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask
```

---

## 3. Run the Flask Application

Navigate to the application folder:

```bash
cd "App/Final app"
```

Run:

```bash
python app.py
```

The Flask server will start locally.

---

## 4. Test API Using Postman

Send a `POST` request to:

```text
http://127.0.0.1:5000/predict
```

Add the required customer features as JSON in the request body.

---

## 5. Open Power BI Dashboard

Open the Power BI `.pbix` file available in the `Dashboard` folder.

Refresh the data if required.

---

# 📸 Project Components

The repository contains separate sections for:

* Dataset
* Jupyter notebooks
* SQL analysis
* Power BI dashboard
* Flask application
* Project documentation
* Reports

---

# 🔮 Future Improvements

Possible future enhancements include:

* Churn probability prediction
* More advanced hyperparameter tuning
* XGBoost/Gradient Boosting comparison
* Model explainability using SHAP
* Automated model retraining
* Cloud deployment
* Real-time dashboard refresh
* Customer retention recommendation system
* Automated email alerts for high-risk customers

---

# 👨‍💻 Author

## Suraj Kadam

**B.E. Electronics & Telecommunication Engineering**

### Skills

```text
Python
SQL
Power BI
Excel
Machine Learning
Pandas
NumPy
Scikit-learn
Flask
GitHub
```

### Areas of Interest

* Data Analytics
* Data Science
* Machine Learning
* Business Intelligence

---

## ⭐ Project Summary

```text
        CUSTOMER DATA
              ↓
        DATA ANALYTICS
              ↓
          SQL + EDA
              ↓
      FEATURE ENGINEERING
              ↓
     MACHINE LEARNING MODEL
              ↓
        CHURN PREDICTION
          ↙          ↘
     POWER BI       FLASK API
    DASHBOARD       + POSTMAN
```

This project demonstrates a complete **end-to-end data analytics and machine learning pipeline**, from raw customer data to business insights and real-time churn prediction.
