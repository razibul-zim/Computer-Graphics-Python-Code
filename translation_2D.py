import numpy as np
point = np.array([2, 3, 1])
# Translation distances
tx, ty = 4, 5
# Translation matrix
T = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])
# Apply translation
translated_point = T @ point
print("Original point:", point[:2])
print("Translated point:", translated_point[:2])