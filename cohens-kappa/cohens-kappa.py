import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    r1 = np.array(rater1, dtype = np.float64)
    r2 = np.array(rater2, dtype = np.float64)
    p = 0
    kappa = 0
    for i in range(len(r1)):
        if r1[i] == r2[i]:
            p += 1
    p0 = p / len(r1)
    count1 = np.unique(r1, return_counts = True)[1]
    count2 = np.unique(r2, return_counts = True)[1]
    if len(count1) != len(count2):
        raise ValueError("Raters must have the same number of categories.")
    elif len(count1) <= 1 or len(count2) <= 1:
        kappa = 1
    pe = 0
    for j in range (len(count1)):
        pe += (count1[j] / len(r1)) * (count2[j] / len(r2))
    kappa = (p0 - pe) / (1 - pe) if (1 - pe) != 0 else 1
    return kappa
    
