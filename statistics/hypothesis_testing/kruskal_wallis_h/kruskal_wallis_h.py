import pandas
from scipy.stats import kruskal

# the Kruskal-Wallis's H tests the null hypothesis that the population's
# median of all groups are the same. This is a non-parametic test, which
# means it does not depends on any population parameter, as for example
# the mean.

data_frame = pandas.read_csv('data/netflix.csv')
movies = data_frame[data_frame['type'] == 'Movie']


def parse_duration(duration):
    duration_string_number = duration.split(' ')[0]
    parsed_duration = int(duration_string_number)
    return parsed_duration


movies['duration_minutes'] = movies['duration'].apply(parse_duration)

drama = movies[movies['listed_in'] ==
               'Dramas, International Movies']['duration_minutes']
comedy = movies[movies['listed_in'] ==
                'Comedies, Dramas, International Movies']['duration_minutes']

drama_mean = drama.mean()
drama_median = drama.median()

comedy_mean = comedy.mean()
comedy_median = comedy.median()

# returns statistic (test statistic) in [0] and pvalue in [1]
p_value = kruskal(drama, comedy)[1]

if (p_value >= 0.01):
    print('I accept that the means are the same, with 99% confidence')
else:
    print('I reject the the means are the same, with 99% confidence')
