import pandas

data_frame = pandas.read_csv('data/BigmacPriceJuly2022.csv')

# the result represents big mac's price in 10% of the countries
# So if the result is 2.413, we say that the big mac costs
# $2,41 in 10% of the countries
quantile10 = data_frame['dollar_price'].quantile(0.1)

# this is the same that the median (data_frame['dollar_price'].median())
quantile50 = data_frame['dollar_price'].quantile(0.5)

print(quantile10)
print(quantile50)
