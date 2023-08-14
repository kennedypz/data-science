import numpy as np
from scipy.stats import anderson

# the Anderson-Darling test is used to check if a data sample came
# from a population with a specific distribution.

# For example, we can test if a data set follows the normal distribution
normal_data = np.random.normal(loc=0, scale=1, size=1000)
beta_data = np.random.beta(a=2, b=10, size=1000)

# returns 3 values: statistics, critical_values and significance_level
# but we are only going to look at the statistics and significance_level.
# if the statistic is bigger than the significance level, then we reject
# the hypothesis that the data comes from the specified distribution
# in this case the normal distribution (norm).

anderson(normal_data, dist='norm')
anderson(beta_data, dist='norm')
