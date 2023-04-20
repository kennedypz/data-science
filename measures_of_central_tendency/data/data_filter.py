import pandas

data_frame = pandas.read_csv(
    'measures_of_central_tendency/data/BigmacPrice.csv')

# returns n rows from the start of the data frame
# returns the first 5 when not specified
# data_frame.head()

# getting data only from a specific month to avoid too much data
# variation so the data makes more sense
data_frame_filtered = data_frame[data_frame['date'] == '2022-07-01']

# returns how many countries are in the data frame
data_frame_filtered.groupby('name').count()['date']

# creates a new .csv file from the filtered data frame that we're gonna use later
data_frame_filtered.to_csv(
    'measures_of_central_tendency/data/BigmacPriceJuly2022.csv', index=False)
