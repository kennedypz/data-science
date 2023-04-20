import pandas
from random import sample

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
group = ["A", "A", "A", "A", "B", "B", "C", "C", "C", "D", "D", "D"]

data_frame = pandas.DataFrame({'group': group, 'values': values})

# data_frame[cluster].unique() gets the clusters (groups)
# Ex.: "A", "B", "C", "D"

# len(allClusters) gets how many clusters I have

# the n is to avoid erros, for example, if I only have 3 clusters
# but ask for 5, n will be 3 instead of 5.

# the sample(allClusters, n) will get n values from all the clusters
# so if I use sample(allClusters, 2) it could return "A" and "B"
# or "A" and "D", and so on.


def clusteredSample(data_frame, clusterQuantity, cluster):
    allClusters = list(data_frame[cluster].unique())
    clustersSize = len(allClusters)
    n = min(clusterQuantity, clustersSize)
    selectedClusters = sample(allClusters, n)

    clusteredSample = data_frame[data_frame[cluster].isin(selectedClusters)]
    return clusteredSample


print(clusteredSample(data_frame, 2, 'group'))
