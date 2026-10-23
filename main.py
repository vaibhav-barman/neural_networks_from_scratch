import numpy as np

inputs = [4.3, 5.1, 6.7, 3.9, 2.8]
weights = [[0.2, 0.5, 0.3, 0.1, 0.4],
           [0.5, -0.9, 0.3, -0.1, 0.6],
           [0.3, -0.4, 0.7, 0.3, 0.8]]

biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
print(output)
