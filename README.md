🏦 Bank Customer Churn Prediction

A complete end-to-end Machine Learning project that predicts whether a bank customer is likely to leave (churn) based on demographic, financial, and behavioral features.

This project includes:

✔ MySQL database integration

✔ Exploratory Data Analysis (EDA)

✔ Data preprocessing using Scikit-Learn

✔ Model training & evaluation

✔ Saving model + preprocessor using joblib

✔ Interactive Streamlit web app for prediction

📊 Dataset Description

The dataset contains bank customer information such as:

Feature -	Description

Geography	- Country of residence

Gender -	Male / Female

Age	- Customer age

Balance	- Account balance

Tenure	- Years with the bank

NumOfProducts	- Number of bank products

HasCrCard	- Whether the customer owns a credit card

IsActiveMember	- Activity status

EstimatedSalary	- Customer’s salary

Complain	- Whether customer has raised a complaint

SatisfactionScore	- Customer satisfaction rating

CardType	- Debit/Credit card category

PointEarned	- Loyalty points

Exited	- (Target) 1 → Churned / 0 → Not Churned

🧪 EDA Highlights

The notebook includes:

📍 Missing value analysis

📍 Outlier detection

📍 Histograms, countplots, boxplots

📍 Correlation heatmap

📍 Feature importance visualization

Key findings:

✔ Older customers churn more frequently

✔ Customers with multiple products churn less

✔ Inactive members have a higher churn rate

✔ Geography affects churn (France < Germany < Spain)

✔ Credit score does not significantly impact churn

⚙️ Model Training

The model pipeline uses:

🛠 Preprocessing

✔ OneHotEncoding for categorical columns

✔ StandardScaler for numeric features

✔ ColumnTransformer to combine transformations

🤖 Models Tried

✔ Logistic Regression

✔ Random Forest

✔ Gradient Boosting

✔ XGBoost


The final model and preprocessing pipeline are saved as:

models/churn_model.pkl

models/preprocessor.pkl

🖥 Streamlit App (Frontend)

The app.py file provides an interactive UI where users enter customer information and the model predicts:

👉 Will the customer churn? Yes/No

streamlit run app.py
