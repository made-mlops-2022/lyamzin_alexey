import json
import os

import click
import dill
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


@click.command("generate")
@click.argument("input_data_dir")
@click.argument("input_model_dir")
@click.argument("output_dir")
def evaluate_model(input_data_dir: str, input_model_dir, output_dir: str):
    X_val = pd.read_csv(os.path.join(input_data_dir, "x_train.csv"))
    y_val = pd.read_csv(os.path.join(input_data_dir, "y_train.csv"))

    with open(os.path.join(input_model_dir, "model.dill"), "rb") as file:
        model = dill.load(file)

    y_pred = model.predict(X_val)
    os.makedirs(output_dir, exist_ok=True)

    metrics = {
        "accuracy": accuracy_score(y_val, y_pred),
        "f1": f1_score(y_val, y_pred, average="macro"),
    }

    with open(os.path.join(output_dir, "metrics.json"), "w") as file:
        json.dump(metrics, file)


if __name__ == "__main__":
    evaluate_model()
