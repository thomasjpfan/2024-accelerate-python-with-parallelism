import numpy as np


def compute(X):
    out = np.cos(X)
    np.sin(out, out=out)
    np.power(out, 3, out=out)
    return out


rng = np.random.default_rng(42)
N = 10000
X = rng.standard_normal(size=(N, N))

compute(X)
