import numpy as np
import matplotlib.pyplot as plt

inputs = np.array([
    [1, 0, 1],   # sample 1
    [0, 1, 1]    # sample 2
])

weights = np.array([
    [0.2],
    [0.5],
    [0.3]
])

print(1*0.2)
output = np.dot(inputs, weights)
print(output)
