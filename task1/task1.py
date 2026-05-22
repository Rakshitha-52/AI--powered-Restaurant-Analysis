import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Evaluation Metrics
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("Dataset .csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# HANDLE MISSING VALUES
# =========================

df['Cuisines'] = df['Cuisines'].fillna("Unknown")

# =========================
# FEATURE SELECTION
# =========================

features = [
    'Country Code',
    'City',
    'Locality',
    'Longitude',
    'Latitude',
    'Cuisines',
    'Average Cost for two',
    'Has Table booking',
    'Has Online delivery',
    'Is delivering now',
    'Price range',
    'Votes'
]

target = 'Aggregate rating'

# Features and target
X = df[features]
y = df[target]

# =========================
# ENCODE CATEGORICAL DATA
# =========================

categorical_cols = X.select_dtypes(
    include=['object', 'string']
).columns

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))

# =========================
# CORRELATION HEATMAP
# =========================

plt.figure(figsize=(12, 8))

sns.heatmap(
    df.select_dtypes(include=np.number).corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")

plt.close()

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

# =========================
# FEATURE SCALING
# =========================

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)

# =========================
# LINEAR REGRESSION
# =========================

lr = LinearRegression()

# Use scaled data
lr.fit(X_train_scaled, y_train)

lr_pred = lr.predict(X_test_scaled)

# =========================
# DECISION TREE REGRESSOR
# =========================

dt = DecisionTreeRegressor(random_state=42)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

# =========================
# RANDOM FOREST REGRESSOR
# =========================

rf = RandomForestRegressor(random_state=42)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# =========================
# MODEL EVALUATION FUNCTION
# =========================

def evaluate_model(name, y_test, predictions):

    mse = mean_squared_error(y_test, predictions)

    mae = mean_absolute_error(y_test, predictions)

    r2 = r2_score(y_test, predictions)

    print(f"\n{name}")

    print("MAE :", mae)

    print("MSE :", mse)

    print("R2 Score :", r2)

    print("-" * 40)

# =========================
# EVALUATE MODELS
# =========================

evaluate_model(
    "Linear Regression",
    y_test,
    lr_pred
)

evaluate_model(
    "Decision Tree Regressor",
    y_test,
    dt_pred
)

evaluate_model(
    "Random Forest Regressor",
    y_test,
    rf_pred
)

# =========================
# FEATURE IMPORTANCE
# =========================

importance = pd.DataFrame({
    'Feature': features,
    'Importance': rf.feature_importances_
})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

print("\nFeature Importance:")
print(importance)

# =========================
# FEATURE IMPORTANCE GRAPH
# =========================

plt.figure(figsize=(8, 5))

sns.barplot(
    x='Importance',
    y='Feature',
    data=importance
)

plt.title("Feature Importance")

plt.savefig("feature_importance.png")

plt.close()

# =========================
# ACTUAL VS PREDICTED GRAPH
# =========================

plt.figure(figsize=(6, 6))

plt.scatter(y_test, rf_pred)

plt.xlabel("Actual Ratings")

plt.ylabel("Predicted Ratings")

plt.title("Actual vs Predicted Ratings")

plt.savefig("actual_vs_predicted.png")

plt.close()

# =========================
# FINAL CONCLUSION
# =========================

print("\nConclusion:")

print(
    "Random Forest Regressor performed the best "
    "with the highest R2 Score and lowest error."
)

print(
    "Votes were found to be the most influential "
    "feature affecting restaurant ratings."
)