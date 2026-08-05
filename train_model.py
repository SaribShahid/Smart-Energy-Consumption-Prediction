import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load processed dataset
df = pd.read_csv("data/processed/energy_preprocessed.csv")

# Features and Target
X = df.drop("Appliances", axis=1)
y = df["Appliances"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Models
linear_model = LinearRegression()
ridge_model = Ridge(alpha=1.0)
lasso_model = Lasso(alpha=0.01, max_iter=10000)

# Train Models
linear_model.fit(X_train, y_train)
ridge_model.fit(X_train, y_train)
lasso_model.fit(X_train, y_train)

# Predictions
linear_pred = linear_model.predict(X_test)
ridge_pred = ridge_model.predict(X_test)
lasso_pred = lasso_model.predict(X_test)

# Evaluation Function
def evaluate(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return mae, rmse, r2

# Results
linear_results = evaluate(y_test, linear_pred)
ridge_results = evaluate(y_test, ridge_pred)
lasso_results = evaluate(y_test, lasso_pred)

results = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Ridge Regression",
        "Lasso Regression"
    ],
    "MAE": [
        linear_results[0],
        ridge_results[0],
        lasso_results[0]
    ],
    "RMSE": [
        linear_results[1],
        ridge_results[1],
        lasso_results[1]
    ],
    "R² Score": [
        linear_results[2],
        ridge_results[2],
        lasso_results[2]
    ]
})

print(results)

# Cross Validation
models = {
    "Linear Regression": linear_model,
    "Ridge Regression": ridge_model,
    "Lasso Regression": lasso_model
}

for name, model in models.items():

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="r2"
    )

    print(name)
    print("Cross Validation Scores:", scores)
    print("Average R²:", scores.mean())
    print("-" * 50)

# Select Best Model
best_model = ridge_model

# Save Model
import joblib

# Find the best model based on R² Score
models = {
    "Linear Regression": (linear_model, linear_results[2]),
    "Ridge Regression": (ridge_model, ridge_results[2]),
    "Lasso Regression": (lasso_model, lasso_results[2])
}

best_model_name, (best_model, best_score) = max(
    models.items(),
    key=lambda item: item[1][1]
)

print(f"Best Model: {best_model_name}")
print(f"Best R² Score: {best_score:.4f}")

# Save the best model
joblib.dump(best_model, "models/energy_model.joblib")

print("Model saved successfully!")