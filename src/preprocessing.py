"""
Preprocessing pipeline for NSL-KDD network traffic data.

Handles:
- Dropping the 'difficulty' scoring column (not a feature)
- One-hot encoding categorical columns (protocol_type, service, flag)
- Scaling numeric columns (StandardScaler)
- Deriving multi-class target (Normal/DoS/Probe/R2L/U2R) from raw label
- Persisting fitted encoder/scaler/feature-list so training and inference
  use IDENTICAL transformations
"""

import pandas as pd
import joblib
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from columns import COLUMNS, CATEGORICAL_COLS, get_attack_category

ARTIFACT_DIR = Path(__file__).resolve().parent.parent / "models"


def load_raw(path: str) -> pd.DataFrame:
    """Load a raw NSL-KDD txt file with proper column names."""
    df = pd.read_csv(path, names=COLUMNS)
    df = df.drop(columns=["difficulty"])
    return df


def add_target_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Derive multi-class category and binary normal/attack targets from label."""
    df = df.copy()
    df["category"] = df["label"].apply(get_attack_category)
    df["is_attack"] = (df["category"] != "Normal").astype(int)
    return df


class NIDSPreprocessor:
    """
    Fits on training data, then can transform both train and test/live data
    consistently. Persists itself to disk so the Flask app can reload it
    without retraining.
    """

    def __init__(self):
        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
        self.scaler = StandardScaler()
        self.numeric_cols = None
        self.feature_names_ = None  # final column order after transform

    def fit(self, df: pd.DataFrame):
        self.numeric_cols = [
            c for c in df.columns
            if c not in CATEGORICAL_COLS + ["label", "category", "is_attack"]
        ]
        self.encoder.fit(df[CATEGORICAL_COLS])
        self.scaler.fit(df[self.numeric_cols])

        cat_feature_names = self.encoder.get_feature_names_out(CATEGORICAL_COLS)
        self.feature_names_ = list(self.numeric_cols) + list(cat_feature_names)
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        num_part = self.scaler.transform(df[self.numeric_cols])
        cat_part = self.encoder.transform(df[CATEGORICAL_COLS])

        num_df = pd.DataFrame(num_part, columns=self.numeric_cols, index=df.index)
        cat_df = pd.DataFrame(
            cat_part, columns=self.encoder.get_feature_names_out(CATEGORICAL_COLS), index=df.index
        )
        out = pd.concat([num_df, cat_df], axis=1)
        return out[self.feature_names_]  # enforce consistent column order

    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.fit(df)
        return self.transform(df)

    def save(self, name: str = "preprocessor.joblib"):
        ARTIFACT_DIR.mkdir(exist_ok=True)
        joblib.dump(self, ARTIFACT_DIR / name)

    @staticmethod
    def load(name: str = "preprocessor.joblib") -> "NIDSPreprocessor":
        return joblib.load(ARTIFACT_DIR / name)


if __name__ == "__main__":
    train_df = load_raw("../data/KDDTrain+.txt")
    train_df = add_target_columns(train_df)

    pre = NIDSPreprocessor()
    X_train = pre.fit_transform(train_df)
    pre.save()

    print("Fitted preprocessor.")
    print("Feature count:", len(pre.feature_names_))
    print("X_train shape:", X_train.shape)
    print("Sample columns:", pre.feature_names_[:5], "...")
