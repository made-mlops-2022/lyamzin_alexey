#!/usr/bin/env python3
import hydra
import logging
import dill
import pandas as pd
from src.models.model import HeartDiseaseClassifier
from src.conf.predict_config import PredictConfig
from src.features.feature_processing import process_test
from hydra.core.config_store import ConfigStore
from hydra.utils import instantiate

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


cs = ConfigStore.instance()
cs.store(name='predict', node=PredictConfig)


@hydra.main(version_base=None, config_name='predict')
def predict_model(cfg: PredictConfig):
    cfg = instantiate(cfg)
    logger.info("Starting prediction...")
    test = pd.read_csv(cfg.test_path)
    test_transformed = pd.DataFrame(process_test(test, cfg.transformer_path))
    logger.info("Features processed. Deserealising classifier...")
    with open(cfg.classifier_path, 'rb') as file:
        classifier = dill.load(file)
    logger.info("Classifier deserealised. Starting prediction")
    y_pred = classifier.predict(test_transformed)
    test = test.assign(prediction=y_pred)
    test.to_csv(cfg.prediction_path)
    logger.info("Prediction saved.")


if __name__ == "__main__":
    predict_model()
