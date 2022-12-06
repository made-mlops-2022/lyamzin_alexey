import os

import click
import pandas as pd


@click.command("generate")
@click.argument("input_dir")
@click.argument("output_dir")
def process_data(input_dir: str, output_dir: str):
    X = pd.read_csv(os.path.join(input_dir, "data.csv"))
    y = pd.read_csv(os.path.join(input_dir, "target.csv"))

    X["sepal_sqaure"] = X["sepal length (cm)"] * X["sepal width (cm)"]
    X["petal_sqaure"] = X["petal length (cm)"] * X["petal width (cm)"]

    X.columns = [
        col.replace(" ", "_").replace("(", "").replace(")", "") for col in X.columns
    ]

    os.makedirs(output_dir, exist_ok=True)
    X.to_csv(os.path.join(output_dir, "data.csv"), index=False)
    y.to_csv(os.path.join(output_dir, "target.csv"), index=False)


if __name__ == "__main__":
    process_data()
