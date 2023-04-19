import numpy as np
import pandas

population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dataFrame = pandas.DataFrame(population, columns=["values"])

# dataFrame.shape returns two values, the first one is the rows count
# the second one is the columns count (whithout the index column)

# dataFrame.iloc returns only the values at the indexes passed


def systematicSample(dataFrame, start=0, step=3):
    indexes = np.arange(start, dataFrame.shape[0], step=step)
    sample = dataFrame.iloc[indexes]
    return sample


print(systematicSample(dataFrame, 1, 3))
