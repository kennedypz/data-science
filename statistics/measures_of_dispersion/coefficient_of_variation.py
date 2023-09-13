import pandas

data_frame = pandas.read_csv(
    'data/BigmacPriceJuly2022.csv')

# gets the coefficient of variation of the big mac price
# the formula is: 100 * standard deviation * mean
# the result represented in a percentage, for example
# 33.800148027441985 represents 33.8%
coefficient_of_variation = 100 * \
    data_frame['dollar_price'].std() / data_frame['dollar_price'].mean()

print(coefficient_of_variation)

# one possible classification for the coefficient of variation (CV) is:
# CV <= 15% = weak dispersion
# 15% < CV <= 30% = moderate dispersion
# CV > 30% = strong dispersion
