from scipy import stats
import pandas

data_frame = pandas.read_csv('data/BigmacPriceJuly2022.csv')

big_mac_mean = data_frame['dollar_price'].mean()
big_mac_standard_deviation = data_frame['dollar_price'].std()

print(f'Big mac\'s price mean in dollars: U${big_mac_mean: .2f}'.format(
    big_mac_mean))
print(f'Big mac\'s price standard deviation in dollars: U${big_mac_standard_deviation: .2f}'.format(
    big_mac_standard_deviation))

# returns 2 values the lowest and the highest in that interval
# in this case the 95% interval is between 1.35 and 6.65
interval_95_big_mac = stats.norm.interval(
    0.95, loc=big_mac_mean, scale=big_mac_standard_deviation)
print(
    '95% confidence interval for the mean: {}'.format(interval_95_big_mac))

# to calculate the margin of error we must subtract the mean from the
# highest value of the interval
margin_of_error = interval_95_big_mac[1] - big_mac_mean
print('Interval\'s margin of error: {}'.format(margin_of_error))
