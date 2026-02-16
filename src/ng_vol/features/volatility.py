import numpy as np

def realized_vol(series, window):
    returns = np.log(series).diff()
    return returns.rolling(window).std() * np.sqrt(252)
