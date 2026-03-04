import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_true = np.array(y_true, dtype = np.float64)
    y_pred = np.array(y_pred, dtype = np.float64)
    MSE = np.mean((y_pred - y_true)**2)
    return MSE
