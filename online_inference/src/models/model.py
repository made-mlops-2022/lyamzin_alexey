from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, roc_auc_score


class HeartDiseaseClassifier(BaseEstimator, TransformerMixin):
    def __init__(self, model_conf):
        if model_conf.model_type == "LogisticRegression":
            self.model = LogisticRegression(random_state=model_conf.random_state)
        elif model_conf.model_type == "DecisionTree":
            self.model = DecisionTreeClassifier(random_state=model_conf.random_state)
        elif model_conf.model_tye == "RidgeClassifier":
            self.model = RidgeClassifier(random_state=model_conf.random_state)
        else:
            raise NotImplementedError(f"Unknown model_type={model_conf.model_type}")

    def fit(self, X, y):
        self.model.fit(X, y)
        return self

    def predict(self, X):
        return self.model.predict(X)

    def evaluate_model(self, y, y_pred):
        return {"roc_auc": f1_score(y, y_pred), "f1": roc_auc_score(y, y_pred)}
