import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib


def load_data(file_path):
    """
    Load the dataset.
    """
    return pd.read_csv(file_path)


def preprocess_data(df):
    """
    Perform preprocessing and feature engineering.
    """

    # Remove duplicate records
    df.drop_duplicates(inplace=True)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Create new features
    df["Year"] = df["date"].dt.year
    df["Month"] = df["date"].dt.month
    df["Day"] = df["date"].dt.day
    df["Hour"] = df["date"].dt.hour
    df["Minute"] = df["date"].dt.minute
    df["DayOfWeek"] = df["date"].dt.dayofweek
    df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)

    # Drop unnecessary columns
    df.drop("date", axis=1, inplace=True)
    df.drop(["rv1", "rv2"], axis=1, inplace=True)

    return df


def scale_features(df):
    """
    Scale input features.
    """

    X = df.drop("Appliances", axis=1)
    y = df["Appliances"]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, "models/scaler.joblib")

    return X_scaled, y


def save_processed_data(df, output_path):
    """
    Save processed dataset.
    """
    df.to_csv(output_path, index=False)