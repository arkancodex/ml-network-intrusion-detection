"""
Train a Random Forest classifier on preprocessed NSL-KDD data to predict
attack category (Normal, DoS, Probe, R2L, U2R). Binary is_attack is derived
from this at inference time.

Run from src/: python3 train_model.py
"""

import time
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score, f1_score
)

from preprocessing import load_raw, add_target_columns, NIDSPreprocessor

ARTIFACT_DIR = Path(__file__).resolve().parent.parent / "models"


def main():
    print("Loading data...")
    train_df = add_target_columns(load_raw("../data/KDDTrain+.txt"))
    test_df = add_target_columns(load_raw("../data/KDDTest+.txt"))

    print("Fitting preprocessor on training data...")
    pre = NIDSPreprocessor()
    X_train = pre.fit_transform(train_df)
    y_train = train_df["category"]

    # NSL-KDD's official test set intentionally includes attack types NOT seen
    # in training (to test generalization). Our OneHotEncoder(handle_unknown="ignore")
    # and category map already handle unseen categorical values / labels gracefully.
    X_test = pre.transform(test_df)
    y_test = test_df["category"]

    print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
    print("Class balance (train):\n", y_train.value_counts())

    print("\nTraining RandomForestClassifier...")
    t0 = time.time()
    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        min_samples_split=2,
        class_weight="balanced",   # important: U2R/R2L are rare
        n_jobs=-1,
        random_state=42,
    )
    clf.fit(X_train, y_train)
    print(f"Training took {time.time()-t0:.1f}s")

    print("\n--- Evaluation on official NSL-KDD test set ---")
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred, digits=3))
    print("Overall accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("Macro F1:", round(f1_score(y_test, y_pred, average="macro"), 4))
    print("\nConfusion matrix (rows=true, cols=pred):")
    labels = sorted(y_test.unique())
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    print("Labels:", labels)
    print(cm)

    # Also report simple binary normal/attack performance, since that's the
    # primary detection signal shown on the dashboard.
    y_test_bin = (y_test != "Normal").astype(int)
    y_pred_bin = (y_pred != "Normal").astype(int)
    print("\n--- Binary (Normal vs Attack) view ---")
    print(classification_report(y_test_bin, y_pred_bin, target_names=["Normal", "Attack"], digits=3))

    # Feature importances (top 15) — useful for the dashboard "why flagged" info
    importances = pd.Series(clf.feature_importances_, index=pre.feature_names_)
    top_features = importances.sort_values(ascending=False).head(15)
    print("\nTop 15 most important features:")
    print(top_features)

    ARTIFACT_DIR.mkdir(exist_ok=True)
    joblib.dump(clf, ARTIFACT_DIR / "nids_model.joblib")
    pre.save()  # re-save preprocessor (fit only on train, consistent with model)
    top_features.to_csv(ARTIFACT_DIR / "feature_importances.csv")

    print("\nSaved model -> models/nids_model.joblib")
    print("Saved preprocessor -> models/preprocessor.joblib")
    print("Saved feature importances -> models/feature_importances.csv")


if __name__ == "__main__":
    main()
