import numpy as np


def compute(X):
    a = np.cos(X)
    b = np.sin(a)
    c = b**3
    return c


rng = np.random.default_rng(42)
N = 10000
X = rng.standard_normal(size=(N, N))

compute(X)
