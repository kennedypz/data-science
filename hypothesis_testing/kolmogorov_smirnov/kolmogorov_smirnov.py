import pandas
from scipy.stats import kstest

# The Kolmogorov-Smirnov test (AKA K-S test or KS test) answers
# the question: "Which is the probability that this sample may
# have been extracted from this distribution?". We can also use it
# to compare two samples. In this case, it answer the question:
# "Which is the probability that these two samples have been
# extracted from the same probability distribution (which we
# do not know)?"

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

# returns statistic (test statistic) in [0] and pvalue in [1]
p_value = kstest(drama, comedy)[1]

if (p_value >= 0.05):
    print('I accept that the distributions are the same, with 95% confidence')
else:
    print('I reject the the distributions are the same, with 95% confidence')
