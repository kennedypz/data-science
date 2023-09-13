# Importing data
from sklearn.datasets import load_iris

# We are going to split data between train and test
# by using the function imported below
from sklearn.model_selection import train_test_split

# Importing SVC which is an implementaion of SVM
from sklearn.svm import SVC

iris_frame = load_iris(as_frame=True)

# flower data
X = iris_frame['data']

# Iris type
y = iris_frame['target']

# We are using data train and type train to train our model,
# and data test and type test to check if our model is accurate
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)

# Algorithm with no data, using one vs one
clf = SVC(decision_function_shape='ovo')

# Training algorithm
clf_trained = clf.fit(X_train, y_train)

# Using the already trained algorithm to make predictions using the
# test's data
y_pred = clf_trained.predict(X_test)


print('Number of iris predicted wrong in a total of {0} test observations: {1}'.format(
    X_test.shape[0], (y_test != y_pred).sum()))
