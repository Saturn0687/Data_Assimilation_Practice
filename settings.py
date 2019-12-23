"""
General settings
"""
import numpy as np

# parameters
N = 40 #was40              # number of grid point
F = 8   #was 8.          # forcing term

Tmax = 40.   #was10.       # time length of the experiment
dT = 0.05 #was 0.05           # DA cycle length
nT = int(Tmax / dT) # number of cycles