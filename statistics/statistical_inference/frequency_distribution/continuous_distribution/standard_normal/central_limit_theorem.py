import plotly.figure_factory as ff
import pandas

# The central limit theorem says that when the sample size
# grows, the sample's distribution mean gets closer and closer
# to a standard normal distribution

data_frame = pandas.read_csv('data/netflix.csv')
movies = data_frame[data_frame['type'] == 'Movie']


def parse_duration(duration):
    duration_string_number = duration.split(' ')[0]
    parsed_duration = int(duration_string_number)
    return parsed_duration


movies['duration_minutes'] = movies['duration'].apply(parse_duration)

# The movies duration does not have a normal distribution
distplot = ff.create_distplot([movies['duration_minutes']], [
                              'Duration (min)'], show_rug=False, bin_size=2, show_hist=False)
distplot.update_layout(title_text='Movie\'s duration')
distplot.write_html(
    file='statistical_inference/frequency_distribution/continuous_distribution/standard_normal/central_limit_theorem_distplot.html')


samples_mean = []
total_iterations = 100000

for iteration in range(total_iterations):
    sample = data_frame['duration_minutes'].sample(frac=0.1)
    mean = sample.mean()
    samples_mean.append(mean)

# But the mean of the movies duration does have a normal distribution
distplotSamplesMean = ff.create_distplot(
    [samples_mean], ['Samples\' mean'], show_rug=False, bin_size=50, show_hist=False)
distplotSamplesMean.update_layout(title_text='Mean value')
distplot.write_html(
    file='statistical_inference/frequency_distribution/continuous_distribution/standard_normal/central_limit_theorem_distplot.html')
