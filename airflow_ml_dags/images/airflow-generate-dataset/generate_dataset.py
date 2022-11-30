import os

import click
import pandas as pd
from sklearn.datasets import load_iris


@click.command("generate")
@click.argument("output_dir")
def generate_dataset(output_dir: str):
    X, y = load_iris(return_X_y=True, as_frame=True)

    os.makedirs(output_dir, exist_ok=True)
    X.to_csv(os.path.join(output_dir, "data.csv"))


if __name__ == "__main__":
    generate_dataset()
