import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.array(x, dtype=np.float64)
    q = np.array(q, dtype=np.float64)
    p  = np.percentile(x, q, method = 'linear')
    return p