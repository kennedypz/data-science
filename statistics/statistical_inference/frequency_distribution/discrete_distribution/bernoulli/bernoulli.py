import numpy as np
from scipy.stats import bernoulli
import plotly.express as px

# We can divide the types of distribution in two: continuous or discrete

# discrete distributions are those where the data are finitely or countably,
# which mean we can count how many data are, for example: how many people
# are on a queue.

# Continuous distributions are those where we can't count the data,
# therefore we utilize intervals. For example: people height, time or money

# Bernoulli distribution: this distribution is used for discrete data when,
# the data can be either 1 or 0. For example: if we are trying to understand
# if a person is going to subscribe to a streaming service or not.

# creates a random sample list with length 10 where the elements can only be
# 0 or 1 and the success rate (which is the chance of one element being 1) is 0.2.
# So there is going to be only a few 1 on the sample.
bernoulli.rvs(p=0.2, size=10)

# here we are controlling the random state, so it is going to create a random
# list at first, but every time we run it again, it will return the same list.
bernoulli.rvs(p=0.2, size=10, random_state=100)

# for this sample we are expecting that only 30% of the data is going to be
# success (1).
sample = bernoulli.rvs(p=0.3, size=500000)

histogram = px.histogram(sample)
histogram.update_layout(title_text='Bernoulli\'s histogram with p = 0.30')
histogram.write_html(
    file='statistical_inference/frequency_distribution/discrete_distribution/bernoulli/bernoullis_histogram.html')
