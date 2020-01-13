"""
Definition of the Lorenz 40-variable (Lorenz 96) model
"""
import numpy as np

def f(t, y, F):
    np.random.seed(21010+np.array([t]).astype(int))
    error_of_F = 1
    F = F + error_of_F * np.random.randn(y.size) # test
    return (np.roll(y, -1) - np.roll(y, 2)) * np.roll(y, 1) - y + F
