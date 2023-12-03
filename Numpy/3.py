import numpy as np
import os
os.system('cls')
seed = np.random.seed(4)
randn = np.random.randn(5)
print(f'randn=/n{randn}/n' )
rangl = np.random.RandomState(seed = 2) #Estado de la cosa
print(f'rang1=/n{rangl}/n')