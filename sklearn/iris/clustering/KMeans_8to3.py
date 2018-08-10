from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
L1 = [x[0] for x in iris.data]
L2 = [x[1] for x in iris.data]

plt.ion()

clf = KMeans()
clf.fit(iris.data, iris.target)
predicted = clf.predict(iris.data)
plt.scatter(L1, L2, c=predicted, marker='s', s=200, cmap=plt.cm.Paired)
#plt.scatter(L1, L2, c=predicted, marker='s', s=200)
plt.title("KMeans8")
plt.show()

plt.pause(5)

for i in [7, 6, 5, 4, 3]:
	clf = KMeans(n_clusters = i)
	clf.fit(iris.data, iris.target)
	predicted = clf.predict(iris.data)
	print(predicted)
	#plt.scatter(L1, L2, c=predicted, marker='s', s=200, cmap=plt.cm.Paired)
	plt.scatter(L1, L2, c=predicted, marker='s', s=200)
	plt.title("KMeans"+str(i) )
	plt.show()
	plt.pause(2)
