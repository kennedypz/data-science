import pandas
import plotly.figure_factory as ff
from scipy import stats

# steps in a mean test hypothesis

# 0: the central limit theorem says that the mean has a normal distribution

# 1.1: In a hypothesis test comparing two means, we have two hypotheses:
# null or alternative. The null hypothesis (H0) says that both means are the same, so
# it means that the idea we want to test does not change the current reality
# and that is why both means are the same. The alternative hypothesis (H1) says that
# the means are different, and that means the idea we are testing has changed the
# current reality, the quo status has been changed

# 1.2: the sample obtained using the current reality is called 'control sample' or
# 'control group'. The sample obtained using the new reality, with the idea we are
# testing, is called 'variant sample' or 'variant group'.

# 2: In order to measure if there was a difference between the control group and
# variant group means, we need to subtract the control group mean from the variant
# group mean, creating a new variable, which we are going to call X.

# 3: this new X variable has a normal distribution!

# 4: If we consider that H0 is true, then X has mean equal to 0.

# 5: If we know how much is the population's variance, we use normal distribution
# for the test. If we do not know, then we use Student's T distribution

# 6.1: We look at the value observed in both groups means, as well as theirs sizes
# and variances, then we get to a statistic called test statistic.

# 6.2: If this value is very unlike to happen according to the X's distribution
# (the difference between the means) under H0 (X's mean is 0), then we reject
# the null hypothesis and say that the groups means are different. Otherwise,
# we say they are the same.

# 7: We call 'p value' the test statistic's occurence probability of more extreme
# values, according to X's distribution, under H0

# 8.1: Basically, if p value's value is low we reject H0 and say that the groups
# means are different. If the p value is high, we do not reject H0 and say that
# the groups means are the same

# 8.2: To decide if p value is low, we define a threshold before stating the test,
# which will be called significance. If p value is equal to or lower than the significance
# level, then it is low.
# For example, let's say that our significance level is 5. Under the null hypothesis
# the proposed means are not the same. So:
# if p value is lower than 5%, we reject the null hypothesis with 95% confidence.
# if p value is lower than 1%, we reject the null hypothesis with 99% confidence.
# else, we do not reject the null hypothesis.

data_frame = pandas.read_csv('data/netflix.csv')

# getting only the movies from the data frame
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

# data = [drama, comedy]
# labels = ['Dramas, International Movies',
#           'Comedies, Dramas, International Movies']

# distplot = ff.create_distplot(data, labels, show_hist=False, show_rug=False)
# distplot.update_layout(title_text='Movies\' duration')
# distplot.write_html(
#     file='hypothesis_testing/mean_testing/mean_testing.html')

# Are the means different from each other?
drama_mean = drama.mean()  # 112.5027
comedy_mean = comedy.mean()  # 119.1350

# The means are different, but the hypothesis test is going
# to tell us if we should reject it or not.
# the hypothesis test considers more than just the mean
# it consideres the sample size, variance

# Let's see if the p value is going to tell us to accept
# or not this value

# returns statistic (test statistic) in [0] and pvalue in [1]
stats.ttest_ind(drama, comedy, equal_var=False)

p_value = stats.ttest_ind(drama, comedy, equal_var=False)[1]

if (p_value >= 0.01):
    print('I accept that the means are the same, with 99% confidence')
else:
    print('I reject the the means are the same, with 99% confidence')
