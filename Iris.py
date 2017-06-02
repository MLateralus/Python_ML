from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf.fit(iris.data, iris.target)
example_iris = [[1.8, 2.0, 1.2, 2.0], [0.7, 0.7, 0.7, 0.7], [2.0, 2.0, 2.0, 2.0], [4.0, 4.0, 4.0, 4.0]]
print(clf.predict(example_iris))
