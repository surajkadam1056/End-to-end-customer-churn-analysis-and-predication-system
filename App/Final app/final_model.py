# Random Forest model selected after evaluation using train-test split
# Accuracy, confusion matrix and classification report were checked
# Now training on full dataset for deployment
# Important: Column order must match during prediction


import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
df = pd.read_csv("final_dataset.csv")

# 2. Select important columns (optimized)
important_cols = [
    "Age",
    "Membership_Years",
    "Total_Purchases",
    "Average_Order_Value",
    "Login_Frequency",
    "Days_Since_Last_Purchase",
    "Discount_Usage_Rate",
    "Returns_Rate"
]

X = df[important_cols]
y = df["Churned"]

# 3. Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train FINAL model on FULL DATA (no split)
model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y)

# 5. Save files
with open("model2.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler2.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("columns2.pkl", "wb") as f:
    pickle.dump(important_cols, f)

print("✅ FINAL MODEL READY FOR DEPLOYMENT")