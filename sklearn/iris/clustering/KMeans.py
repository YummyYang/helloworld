from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
clf = KMeans(n_clusters = 3)
clf.fit(iris.data, iris.target)
predicted = clf.predict(iris.data)

L1 = [x[0] for x in iris.data]
L2 = [x[1] for x in iris.data]

plt.scatter(L1, L2, c=predicted, marker='s', s=200, cmap=plt.cm.Paired)
plt.title("KMeans")
plt.show()
