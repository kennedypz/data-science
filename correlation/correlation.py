import pandas

data_frame = pandas.read_csv(
    'data/BigmacPriceJuly2022.csv')

# pandas uses Pearson's correlation by default in this method
correlation = data_frame.corr(numeric_only=True)

print(correlation)
