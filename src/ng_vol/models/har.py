import statsmodels.api as sm
from .base import VolatilityModel

class HARModel(VolatilityModel):
    def fit(self, X, y):
        self.model = sm.OLS(y, sm.add_constant(X)).fit()
        return self

    def predict(self, X):
        return self.model.predict(sm.add_constant(X))
