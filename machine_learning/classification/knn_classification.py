# Importing data
from sklearn.datasets import load_iris

# We are going to split data between train and test
# by using the function imported below
from sklearn.model_selection import train_test_split

# Importing KNN that uses a normal distribution
from sklearn.neighbors import KNeighborsClassifier

# To make sure the data has the same mean and variance
# StandardScaler is going to calculate the mean and
# standard deviation of each column. Then it subtracts
# the mean of each column and divide by the standard
# deviation
from sklearn.preprocessing import StandardScaler

iris_frame = load_iris(as_frame=True)

# flower data
data = iris_frame['data']

# Iris type
type = iris_frame['target']

# We are using data train and type train to train our model,
# and data test and type test to check if our model is accurate
data_train, data_test, type_train, type_test = train_test_split(
    data, type, test_size=0.25, random_state=0)

# Algorithm without any data, where K = 3
neigh = KNeighborsClassifier(n_neighbors=3)

# Training the algorithm
neigh.fit(data_train, type_train)

# Using the already trained algorithm to make predictions using the
# test's data
type_pred = neigh.predict(data_test)

# Now we check in how many cases we were wrong
print('Number of iris predicted wrong in a total of {0} test observations: {1}'.format(
    data_test.shape[0], (type_test != type_pred).sum()))

# Making sure the data has the same mean and variance
scaler = StandardScaler()
scaler.fit(data_train)

data_train = scaler.transform(data_train)
data_test = scaler.transform(data_test)


# Now that the data is already transformed, we
# run the test again
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data_train, type_train)
type_pred = neigh.predict(data_test)

# the result will be the same since this dataset has
# only a few observations

# What would be the best value for K?
success_percentage = []
test_size = data_test.shape[0]

# Runs the test for K values from 1 to 14
# and adds the success percentage to the list
for i in range(1, 15):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(data_train, type_train)
    pred_i = knn.predict(data_test)

    success_i = (type_test == pred_i).sum()/test_size
    success_percentage.append(100 * success_i)

# After running the previous for loop, we can
# see that the best K value is 3 because the next
# values had the same amount of success, but would
# take more time and resources to run.
