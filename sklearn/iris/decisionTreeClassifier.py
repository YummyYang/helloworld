from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split #from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
n_classes = 3
plot_colors = "bry"
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.25)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)		# I think this pleace is better if we use different variable name of 'clf';

y_predict = clf.predict(x_test)
print("accuracy_score:" + str(accuracy_score(y_predict, y_test) * 100 ) + "%" )

X=x_test[:,0]
Y=x_test[:,3]

plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[2])
plt.axis("tight")

for i , color in zip(range(n_classes), plot_colors):
	idx = np.where(y_predict == i)
	plt.scatter(X[idx], Y[idx], c=color, label=iris.target_names[i], marker='+')

plt.axis("tight")
plt.suptitle("DCT")
plt.legend()
plt.show()
