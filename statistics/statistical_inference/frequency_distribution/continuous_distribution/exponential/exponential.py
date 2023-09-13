from numpy.random import exponential
import plotly.figure_factory as ff
# This type of continuous distribution is often used to
# calculate waiting time or the time spent in a activity.

# For example, while the Poisson distribution is used to
# count how many people are in a queue, the exponential
# distribution is used to show how long is the waiting
# time in that queue.

# One pratical use of this distribution is to show how
# long the users stay in an app or website.

# scale represents the time average
exponential(scale=5, size=10)

sample = exponential(scale=5, size=500000)
distplot = ff.create_distplot(
    [sample], ['exponential curve'], show_rug=False, bin_size=2, show_hist=False)
distplot.update_layout(title_text='Exponential average 5')
distplot.write_html(
    file='statistical_inference/frequency_distribution/continuous_distribution/exponential/exponential_distplot.html')
