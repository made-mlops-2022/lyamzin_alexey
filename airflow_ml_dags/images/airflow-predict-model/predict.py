import json
import os

import click
import dill
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


@click.command("generate")
@click.argument("input_data_dir")
@click.argument("input_model_path")
@click.argument("output_dir")
def evaluate_model(input_data_dir: str, input_model_path, output_dir: str):
    X_test = pd.read_csv(os.path.join(input_data_dir, "data.csv"))

    with open(input_model_path, "rb") as file:
        model = dill.load(file)

    X_test["predictions"] = model.predict(X_test)
    os.makedirs(output_dir, exist_ok=True)
    X_test.to_csv(os.path.join(output_dir, "predictions.csv"), index=False)


if __name__ == "__main__":
    evaluate_model()
