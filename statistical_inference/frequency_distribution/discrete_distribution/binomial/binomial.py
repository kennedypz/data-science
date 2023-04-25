from numpy.random import binomial
import plotly.express as px

# This is a discrete data distribution for when the data we
# have is basically the number of successful cases in a sequence
# of n tries, where each try can be either a success or a failure.
# For example: the amount of heads in 10 coin flips.

# Following the coin example, here we are creating a list that
# will show the result of a coin being tossed 10 times, with
# a success rate of 70% in 5 different cases.
# this list's items represents the number of successful results
# for each case
print(binomial(n=10, p=0.7, size=5))

sample = binomial(n=20, p=0.7, size=500000)
histogram = px.histogram(sample)
histogram.update_layout(
    title_text='Binomial\'s histogram with n = 20 and p = 0.70')
histogram.write_html(
    file='statistical_inference/frequency_distribution/discrete_distribution/binomial/binomials_histogram.html')
