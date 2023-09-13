import numpy as np

# the variance is the mean of the distance's square between each
# observation and the mean

list_variance_example = [1, 2, 3, 4, 5]


def mean(list):
    return sum(list)/len(list)


def sample_variance(list):
    list_mean = mean(list)
    list_size = len(list)

    square_distances = []

    for observation in list:
        square_distance = (observation - list_mean) ** 2
        square_distances.append(square_distance)

    variance = sum(square_distances)/(list_size-1)
    return variance


def populational_variance(list):
    list_mean = mean(list)
    list_size = len(list)

    square_distances = []

    for observation in list:
        square_distance = (observation - list_mean) ** 2
        square_distances.append(square_distance)

    # the single difference between populational and sample variance
    # is that we do not subtract one from the list size
    variance = sum(square_distances)/list_size
    return variance


print(sample_variance(list_variance_example))
print(populational_variance(list_variance_example))

# numpy already has a variance function but returns only the
# populational variance
print(np.var(list_variance_example))
