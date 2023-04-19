import pandas

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
group = ["A", "A", "A", "A", "B", "B", "C", "C", "C", "D", "D", "D"]

dataFrame = pandas.DataFrame({'group': group, 'values': values})

# gets n samples from the stratum (group).
# for example, if called like this: stratifiedSample(dataFrame, 1, "group")
# the output will be one random value from each group.


def stratifiedSampleByStatumSamples(dataFrame, n, stratum):
    # the x in the lambda function represents the stratum
    sample = dataFrame.groupby(stratum, group_keys=False).apply(
        lambda x: x.sample(min(len(x), n)))
    return sample

# by using this method of sampling, every group will always have at least
# one value representing the group.


# print(stratifiedSampleByStatumSamples(dataFrame, 2, 'group'))


# the result of len(x)/populationSize inside the lambda function is
# the percentage that one stratum represents in the population.

# using the values and group previously declared we could say that the "A" group
# corresponds to 1/3 of the population.

# then when multiply this result by the final size we want the sample to have
# which is represented by the N in the function (N*len(x)/populationSize).

# for example, if I say that 30% of my data is from stratum (group) "A" and my
# sample size is 10, then how many values group group "A" should I get so my
# sample has the same representation than the population?
# I should get 30% out of 10, which is 3, meaning that I should get 3 values
# from group "A".

# the reset_index formats the dataFrame.

# sort_values sorts the data frame by stratum.
def stratifiedSampleByFinalSampleSize(dataframe, N, stratum):
    populationSize = dataFrame.shape[0]

    sample = dataFrame.groupby(stratum, group_keys=False).apply(lambda x: x.sample(
        int(N*len(x)/populationSize))).reset_index(drop=True).sort_values(by=stratum)
    return sample


print(stratifiedSampleByFinalSampleSize(dataFrame, 9, 'group'))
