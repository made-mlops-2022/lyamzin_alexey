from dataclasses import dataclass, field
from typing import List


@dataclass
class SplitConfig:
    test_size: int = field(default=0.2)
    random_state: int = field(default=42)


@dataclass
class ModelConfig:
    object_path: str
    report_path: str
    model_type: str = field(default='LogisticRegression')
    random_state: int = field(default=42)


@dataclass
class FeaturesConfig:
    data_path: str
    target_column: str

    cat_feats: List[str]
    cont_feats: List[str]


@dataclass
class ProcessingConfig:
    cat_na_strategy: str
    cont_na_strategy: str
    one_hot_encoding: bool
    standart_scaling: bool
    object_path: str


@dataclass
class TrainConfig:
    split_params: SplitConfig
    model_params: ModelConfig
    features_params: FeaturesConfig
    prcessing_params: ProcessingConfig
