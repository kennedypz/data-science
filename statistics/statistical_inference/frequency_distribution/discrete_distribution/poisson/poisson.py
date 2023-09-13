from numpy.random import poisson
import plotly.express as px

# This discrete data distribution is used when we have
# count data. For example, the amount of people in a queue,
# the amount of accidents in a year or the amount of clicks
# in a website button.

# the lam param represents a lambda that indicates the
# average of occurrences, for example, the average number
# of people in a bank queue
poisson(lam=5, size=10)

sample = poisson(lam=2, size=500000)
histogram = px.histogram(sample)
histogram.update_layout(title_text='Histogram of a Poisson with lambda = 4')
histogram.write_html(
    file='statistical_inference/frequency_distribution/discrete_distribution/poisson/poissons_histogram.html')
