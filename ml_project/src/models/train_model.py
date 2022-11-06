#!/usr/bin/env python3
import logging
import dill
import json
import hydra
import pandas as pd
import numpy as np
from src.conf.train_config import TrainConfig
from src.models.model import HeartDiseaseClassifier
from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate
from src.data.make_dataset import make_dataset
from src.features.feature_transformer import FeatureTransformer
from src.features.feature_processing import process_train, process_test


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


cs = ConfigStore.instance()
cs.store(name='train', node=TrainConfig)


def serialize_classifier(classifier: HeartDiseaseClassifier, object_path: str):
    with open(object_path, 'wb') as file:
        dill.dump(classifier, file)


def save_report(metrics: dict, report_path: str):
    with open(report_path, 'w') as file:
        json.dump(metrics, file)


@hydra.main(version_base=None, config_name='train_config', config_path='../../configs')
def train_model(cfg: TrainConfig):

    logger.info('Starting train pipeline...')

    cfg = instantiate(cfg, _convert_='partial')
    X_train, X_test, y_train, y_test = make_dataset(
        cfg.features_params, cfg.split_params)
    logger.info(
        "Train test split complete. Start processing features...")

    X_train = process_train(
        X_train, cfg.features_params, cfg.prcessing_params)
    X_test = pd.DataFrame(process_test(
        X_test, cfg.prcessing_params.object_path))
    logger.info(
        "Feature processed. Feature Tranformer serialized. Start fitting estimator...")

    classifier = HeartDiseaseClassifier(cfg.model_params).fit(X_train, y_train)
    serialize_classifier(classifier, cfg.model_params.object_path)
    y_pred = classifier.predict(X_test)
    logger.info(
        "Classifier serialized. Start model evaluation...")
    metrics = classifier.evaluate_model(y_pred, y_test)
    save_report(metrics, cfg.model_params.report_path)
    logger.info("Evaluation report saved. Train completed.")


if __name__ == "__main__":
    train_model()
