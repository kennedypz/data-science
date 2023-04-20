import pandas

data_frame = pandas.read_csv(
    'measures_of_central_tendency/data/BigmacPriceJuly2022.csv')

# gets the mode
mode = data_frame['dollar_price'].mode()

print(mode)

# returns how many occurrences are for each value of 'dollar_price'
# data_frame['dollar_price'].value_counts()
