import numpy as np
import pandas

population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
data_frame = pandas.DataFrame(population, columns=["values"])

# data_frame.shape returns two values, the first one is the rows count
# the second one is the columns count (whithout the index column)

# data_frame.iloc returns only the values at the indexes passed


def systematicSample(data_frame, start=0, step=3):
    indexes = np.arange(start, data_frame.shape[0], step=step)
    sample = data_frame.iloc[indexes]
    return sample


print(systematicSample(data_frame, 1, 3))
