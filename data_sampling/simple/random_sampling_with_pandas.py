import pandas

population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# creates a data frame from the "population" list
# this data frame is an excel like table and in this case has 2 columns
# one unamed which represents the lines/index and other called "values"
# which was defined by me in the creation of the data frame and represents
# the values of the population list
data_frame = pandas.DataFrame(population, columns=["values"])


# gets a sample based on size (4 in this case)
print(data_frame.sample(n=4))

print("\n")

# gets a sample based on percentage/proportion (0.33 in this case)
print(data_frame.sample(frac=0.33))
