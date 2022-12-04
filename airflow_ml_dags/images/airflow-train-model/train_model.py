import os

import click
import dill
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


@click.command("generate")
@click.argument("input_dir")
@click.argument("output_dir")
def train_model(input_dir: str, output_dir: str):
    X_train = pd.read_csv(os.path.join(input_dir, "x_train.csv"))
    y_train = pd.read_csv(os.path.join(input_dir, "y_train.csv"))

    parameters = {
        "estimator__C": np.logspace(-2, 2, num=100),
        "estimator__multi_class": ["multinomial"],
        "estimator__solver": ["saga"],
        "estimator__tol": [1e-3],
        "estimator__penalty": ["l1", "l2"],
    }

    pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "estimator",
                LogisticRegression(),
            ),
        ]
    )

    clf = GridSearchCV(pipeline, parameters, n_jobs=-1, refit=True, scoring="accuracy")
    clf = clf.fit(X_train, y_train.values.ravel())
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "model.dill"), "wb") as file:
        dill.dump(clf, file)


if __name__ == "__main__":
    train_model()
