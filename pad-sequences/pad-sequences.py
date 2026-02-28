import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is None :
        max_len = max((len(seq) for seq in seqs), default = 0)
    for i in seqs :
        if len(i) < max_len :
            for j in range (len(i), max_len):
                i.append(pad_value)
        elif len(i) > max_len :
            del i[max_len:]
    return seqs