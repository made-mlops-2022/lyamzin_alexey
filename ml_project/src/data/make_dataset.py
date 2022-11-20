import pandas as pd
from sklearn.model_selection import train_test_split

from src.conf.train_config import FeaturesConfig, SplitConfig


def make_dataset(features_cfg: FeaturesConfig, split_cfg=SplitConfig):
    train_df = pd.read_csv(features_cfg.data_path)

    X = train_df.drop(columns=features_cfg.target_column)
    y = train_df.loc[:, features_cfg.target_column]

    return train_test_split(X, y, test_size=split_cfg.test_size, random_state=split_cfg.random_state)
