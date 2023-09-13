import pandas

data_frame = pandas.read_csv(
    'data/BigmacPriceJuly2022.csv')

# the median is usually more consistent than the mean
median = data_frame['dollar_price'].median()

print(median)
