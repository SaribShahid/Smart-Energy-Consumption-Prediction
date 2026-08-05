import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import mutual_info_regression


def load_processed_data(file_path):
    """
    Load the preprocessed dataset.
    """
    return pd.read_csv(file_path)


def split_features_target(df):
    """
    Split dataset into features and target.
    """
    X = df.drop("Appliances", axis=1)
    y = df["Appliances"]

    return X, y


def variance_feature_selection(X, threshold=0.01):
    """
    Remove low-variance features.
    """
    selector = VarianceThreshold(threshold=threshold)
    selector.fit(X)

    selected_features = X.columns[selector.get_support()]

    return selected_features


def mutual_information_scores(X, y):
    """
    Calculate feature importance using Mutual Information.
    """
    mi_scores = mutual_info_regression(X, y)

    mi_scores = pd.Series(
        mi_scores,
        index=X.columns
    ).sort_values(ascending=False)

    return mi_scores