from dataclasses import dataclass


@dataclass
class PredictConfig:
    transformer_path: str
    classifier_path: str
    test_path: str
    prediction_path: str
