import pandas

data_frame = pandas.read_csv(
    'measures_of_central_tendency/data/BigmacPriceJuly2022.csv')

# gets the variance of the big mac price
variance = data_frame['dollar_price'].var()

print(variance)
