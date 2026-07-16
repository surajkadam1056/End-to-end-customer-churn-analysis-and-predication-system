import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
df = pd.read_csv("final_dataset.csv")

# 2. Split input and output
X = df.drop("Churned", axis=1)
y = df["Churned"]

# 3. Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train model
model = RandomForestClassifier()
model.fit(X_scaled, y)

# 5. Save model
pickle.dump(model, open("model.pkl", "wb"))

# 6. Save scaler
pickle.dump(scaler, open("scaler.pkl", "wb"))

# 7. Save columns
pickle.dump(X.columns.tolist(), open("columns.pkl", "wb"))

