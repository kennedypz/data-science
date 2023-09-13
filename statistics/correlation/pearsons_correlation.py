from scipy.stats import pearsonr
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = a * 3 + 2

# b has a linear correlation with a cause b = a * constant1 + constant2.
# So b is completely dependent of a and their correlation is linear

correlation = pearsonr(a, b)
print(correlation)
