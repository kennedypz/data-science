from numpy.random import normal
import plotly.figure_factory as ff

# loc = mean and scale = standard deviation
# this is the most important normal distribution
# with mean = 0 and scale = 1
normal(loc=0, scale=1, size=10)

sample = normal(loc=0, scale=1, size=500000)
distplot = ff.create_distplot(
    [sample], ['normal curve'], show_rug=False, bin_size=2, show_hist=False)
distplot.update_layout(title_text='Standard normal distribuition')
distplot.write_html(
    file='statistical_inference/frequency_distribution/continuous_distribution/standard_normal/standard_normal_distribution.html')
