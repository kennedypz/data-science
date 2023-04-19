import pandas
from random import sample

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
group = ["A", "A", "A", "A", "B", "B", "C", "C", "C", "D", "D", "D"]

dataFrame = pandas.DataFrame({'group': group, 'values': values})

# dataFrame[cluster].unique() gets the clusters (groups)
# Ex.: "A", "B", "C", "D"

# len(allClusters) gets how many clusters I have

# the n is to avoid erros, for example, if I only have 3 clusters
# but ask for 5, n will be 3 instead of 5.

# the sample(allClusters, n) will get n values from all the clusters
# so if I use sample(allClusters, 2) it could return "A" and "B"
# or "A" and "D", and so on.


def clusteredSample(dataFrame, clusterQuantity, cluster):
    allClusters = list(dataFrame[cluster].unique())
    clustersSize = len(allClusters)
    n = min(clusterQuantity, clustersSize)
    selectedClusters = sample(allClusters, n)

    clusteredSample = dataFrame[dataFrame[cluster].isin(selectedClusters)]
    return clusteredSample


print(clusteredSample(dataFrame, 2, 'group'))
