import pandas

data_frame = pandas.read_csv(
    'data/BigmacPriceJuly2022.csv')

# return the mean (média) of prices
mean = data_frame['dollar_price'].mean()

# the main problem with the mean is that it can be easily
# influenced by extreme values in our sample

print(mean)
