import pandas
from statsmodels.stats.proportion import proportions_ztest

# The central limit theorem says that the mean has a normal distribution.
# If we consider that each observation as a Bernoulli, where 0 represents
# failure and 1 represents success, the mean of these observations is a proportion.

# from now on the steps are the same as in mean testing

# The main difference in a proportion test is that because we consider
# each observation as a Bernoulli, we know exactly it's variance,
# which simplifies our testing

data_frame = pandas.read_csv('data/netflix.csv')

# getting only the movies from the data frame
movies = data_frame[data_frame['type'] == 'Movie']

# The question we want to answer in this example is:
# Is there a difference in proportion of long movies between english movies
# and american movies?


def parse_duration(duration):
    duration_string_number = duration.split(' ')[0]
    parsed_duration = int(duration_string_number)
    return parsed_duration


movies['duration_minutes'] = movies['duration'].apply(parse_duration)


def long_movie(duration_minutes):
    return 1 if duration_minutes > 150 else 0


movies['long_movie'] = movies['duration_minutes'].apply(long_movie)

# Let's take a look at the distribution of long movies in both countries

united_kingdom = movies['country'] == 'United Kingdom'
usa = movies['country'] == 'United States'

united_kingdom_or_usa = united_kingdom | usa

movies[united_kingdom_or_usa].groupby('country').mean()['long_movie']

# Now let's calculate the p value of these two proportions, using normal distribution.
usa_long_movies = movies[usa]['long_movie']

usa_long_movies_sum = usa_long_movies.sum()
usa_sample_size = usa_long_movies.count()

united_kingdom_long_movies = movies[united_kingdom]['long_movie']

united_kingdom_long_movies_sum = united_kingdom_long_movies.sum()
united_kingdom_sample_size = united_kingdom_long_movies.count()

# count corresponds to the success cases of each county, in this case the long movies
# nobs corresponds to the number of observations which is the sample size
# returns statistic (test statistic) in [0] and pvalue in [1]
test_result = proportions_ztest(
    count=[usa_long_movies_sum, united_kingdom_long_movies_sum],
    nobs=[usa_sample_size, united_kingdom_sample_size]
)

p_value = test_result[1]

# If we define the significance level as 5%, then:
if (p_value >= 0.05):
    print('I accept that the means are the same, with 95% confidence')
else:
    print('I reject the the means are the same, with 95% confidence')
