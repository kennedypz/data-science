from numpy.random import standard_t
import plotly.figure_factory as ff

# this distrubition is very similar to the standard normal
# the difference is that in this one extreme values are
# more likely to happen.

# df=degrees of freedom
standard_t(df=5, size=10)
sample = standard_t(df=5, size=500000)
distplot = ff.create_distplot(
    [sample], ['Student\'s t curve'], show_rug=False, bin_size=2, show_hist=False)
distplot.update_layout(title_text='Student\'s t with 5 degrees of freedom')
distplot.write_html(
    file='statistical_inference/frequency_distribution/continuous_distribution/students_t/students_t_distribution.html')
