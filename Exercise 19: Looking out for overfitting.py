from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=450,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Create a classifier and fit it to our data
knn = KNeighborsClassifier(n_neighbors=42)
knn.fit(x_train, y_train)

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

def main(X_train, X_test, y_train, y_test):
    global y_predict
    k = 3    # classify our test items based on the classes of 3 nearest neighbors
    distances_list = []
    for i, test_item in enumerate(X_test):
        distances = [dist(train_item, test_item) for train_item in X_train]
        distances_list.append(distances)
    sort_index = np.argsort(distances_list)
    y_predict = []
    full_list = []
    for i in range(len(sort_index)):
        using = sort_index[i][0:k]
        y_train_use = []
        for j in using:
            y_train_use.append(y_train[j])
        m, j = stats.mode(y_train_use)
        y_predict.append(m[0])
    y_predict=np.asarray(y_predict)
    return y_predict

main(x_train, x_test, y_train, y_test)

print("training accuracy: %f" % knn.score(x_train, y_train))
print("testing accuracy: %f" % knn.score(x_test, y_test))
print("testing accuracy: %f" % knn.score(x_test, y_predict))
