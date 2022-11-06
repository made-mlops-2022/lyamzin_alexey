import dill
import numpy as np
import pandas as pd

from src.conf.train_config import FeaturesConfig, ProcessingConfig
from src.features.feature_transformer import FeatureTransformer


def serialise_transformer(transformer: FeatureTransformer, object_path: str):
    with open(object_path, 'wb') as file:
        dill.dump(transformer, file)


def process_train(X: pd.DataFrame, feature_cfg: FeaturesConfig, processing_cfg: ProcessingConfig):
    feature_transformer = FeatureTransformer(
        feature_cfg, processing_cfg).fit(X)
    X_transformed = feature_transformer.transform(X)

    serialise_transformer(feature_transformer, processing_cfg.object_path)

    return X_transformed


def process_test(X: pd.DataFrame, object_path: str):
    with open(object_path, 'rb') as file:
        transformer = dill.load(file)

    return transformer.transform(X)
