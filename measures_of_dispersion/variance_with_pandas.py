import pandas

data_frame = pandas.read_csv(
    'data/BigmacPriceJuly2022.csv')

# gets the variance of the big mac price
variance = data_frame['dollar_price'].var()

print(variance)
