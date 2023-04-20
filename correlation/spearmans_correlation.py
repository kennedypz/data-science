from scipy.stats import spearmanr
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = a * 3 + 2

correlation = spearmanr(a, b)
print(correlation)
