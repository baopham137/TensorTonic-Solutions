import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    A = np.array(a, dtype=np.float64)
    B = np.array(b, dtype=np.float64)
    dot = np.dot(A,B)
    norms = np.linalg.norm(A) * np.linalg.norm(B)
    if norms != 0 :
        cs = dot / norms 
        return cs
    else :
        return 0
    