from sklearn.metrics import roc_auc_score, f1_score
from abc import ABC, ABCMeta
from streamad.base import BaseMetrics


class AUCMetric(BaseMetrics):
    def __init__(self) -> None:
        super().__init__()

    def evaluate(self):

        return roc_auc_score(self.y_true, self.y_pred)