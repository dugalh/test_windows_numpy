import numpy as np

def test_dot():
    a = b = np.eye(3)
    c = a.dot(b)
    assert np.all(c==a)