import pandas
from scipy.stats import t

data_frame = pandas.read_csv('data/BigmacPriceJuly2022.csv')


def is_expensive(price):
    if price > 4:
        return 1
    return 0


data_frame['expensive_bigmac'] = data_frame['dollar_price'].apply(is_expensive)

# Creating a proportion interval with 95% of confidence
expensive_big_mac_proportion = data_frame['expensive_bigmac'].mean()
expensive_big_mac_standard_deviation = (
    expensive_big_mac_proportion * (1 - expensive_big_mac_proportion)) ** 0.5

print('Expensive big mac proportion: {}'.format(expensive_big_mac_proportion))
print('Expensive big mac standard deviation\'s proportion: {}'.format(
    expensive_big_mac_standard_deviation))


degrees_of_freedom = data_frame.shape[0] - 1
interval_95_big_mac_proportion = t.interval(
    0.95, df=degrees_of_freedom, loc=expensive_big_mac_proportion, scale=expensive_big_mac_standard_deviation/(data_frame.shape[0]**0.5))

print('95% confidence interval for the proportion: {}'.format(
    interval_95_big_mac_proportion))

margin_of_error = interval_95_big_mac_proportion[1] - \
    expensive_big_mac_proportion
print('Interval\'s margin of error: {}'.format(margin_of_error))
