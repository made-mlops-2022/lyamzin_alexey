import os
from random import randint

import click
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris


@click.command("generate")
@click.argument("output_dir")
def generate_dataset(output_dir: str):
    new_data = pd.concat(load_iris(return_X_y=True, as_frame=True), axis=1).sample(
        randint(80, 100)
    )
    X, y = new_data.drop(columns="target"), new_data["target"]
    X = X + np.random.normal(0, 0.1, X.shape)

    os.makedirs(output_dir, exist_ok=True)
    X.to_csv(os.path.join(output_dir, "data.csv"), index=False)
    y.to_csv(os.path.join(output_dir, "target.csv"), index=False)


if __name__ == "__main__":
    generate_dataset()
