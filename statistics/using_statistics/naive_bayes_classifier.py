# Importing data
from sklearn.datasets import load_iris

# We are going to split data between train and test
# by using the function imported below
from sklearn.model_selection import train_test_split

# Importing Naive Bayes that uses a normal distribution
from sklearn.naive_bayes import GaussianNB

iris_frame = load_iris(as_frame=True)

# flower data
data = iris_frame['data']

# Iris type
type = iris_frame['target']

# We are using data train and type train to train our model,
# and data test and type test to check if our model is accurate
data_train, data_test, type_train, type_test = train_test_split(
    data, type, test_size=0.25, random_state=0)

# Algorithm with no data
gnb = GaussianNB()

# Training algorithm
gnb_trained = gnb.fit(data_train, type_train)

# Using out algorithm already trained to make predictions
# using the test data
type_prediction = gnb_trained.predict(data_test)

# Now we check in how many cases we were wrong
print('Number of iris predicted wrong in a total of {0} test observations: {1}'.format(
    data_test.shape[0], (type_test != type_prediction).sum()))
