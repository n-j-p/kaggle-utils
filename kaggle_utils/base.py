from sklearn.base import BaseEstimator, TransformerMixin
class Transformer0(BaseEstimator, TransformerMixin):
    '''Base Transformer class'''
    def __init__(self):
        pass
    def set_output(self, transform):
        pass
    def fit(self, X, y=None):
        return self
