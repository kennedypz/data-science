from numpy.random import beta
import plotly.figure_factory as ff
# This type of continuous distribution is often used to
# modelate probabilities because the data must be between
# 0 and 1.

beta(a=5, b=3, size=10)

sample = beta(a=5, b=20, size=500000)
distplot = ff.create_distplot(
    [sample], ['beta curve'], show_rug=False, bin_size=2, show_hist=False)
distplot.update_layout(title_text='Beta with a=5 and b=20')
distplot.write_html(
    file='statistical_inference/frequency_distribution/continuous_distribution/beta/beta_distplot.html')
