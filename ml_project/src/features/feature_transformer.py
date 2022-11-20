from sklearn.base import TransformerMixin
from src.conf.train_config import FeaturesConfig, ProcessingConfig
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


class FeatureTransformer(TransformerMixin):
    def __init__(self, features_cfg: FeaturesConfig, processing_cfg: ProcessingConfig):
        self.cat_feats = features_cfg.cat_feats
        self.cont_feats = features_cfg.cont_feats

        cat_pipe = [('fillna', SimpleImputer(
            strategy=processing_cfg.cat_na_strategy))]

        if processing_cfg.one_hot_encoding:
            cat_pipe.append(('encode', OneHotEncoder()))

        cont_pipe = [('fillna', SimpleImputer(
            strategy=processing_cfg.cont_na_strategy))]

        if processing_cfg.standart_scaling:
            cont_pipe.append(('scale', StandardScaler()))

        self.transformer = ColumnTransformer(
            transformers=[
                ('transform_cat', Pipeline(cat_pipe), features_cfg.cat_feats),
                ('transform_cont', Pipeline(cont_pipe), features_cfg.cont_feats),
            ]
        )

    def fit(self, X):
        return self.transformer.fit(X)

    def transform(self, X):
        return self.transformer.transform(X)
