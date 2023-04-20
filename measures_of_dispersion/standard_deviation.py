import pandas

data_frame = pandas.read_csv(
    'data/BigmacPriceJuly2022.csv')

# gets the standard deviation of the big mac price
standard_deviation = data_frame['dollar_price'].std()

# using numpy
# np.std(list)

print(standard_deviation)
