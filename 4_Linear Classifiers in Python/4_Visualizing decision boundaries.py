#Visualizing decision boundaries
#In this exercise, you'll visualize the decision boundaries of various classifier types.

#A subset of scikit-learn's built-in wine dataset is already loaded into X, along with binary labels in y.

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier

# Define the classifiers
classifiers = [LogisticRegression(), LinearSVC(), SVC(), KNeighborsClassifier()]

# Fit the classifiers
for c in classifiers:
    c.fit(X, y)

# Plot the classifiers
plot_4_classifiers(X, y, classifiers)
plt.show()

#Answer
# grafica cada una de las clasificaciones llamadas en classifiers en la grafica se puede ver la diferencia de limites generada por cada una, se observa una mejor agrupacion con SVC
#Nice! As you can see, logistic regression and linear SVM are linear classifiers whereas the default SVM and KNN are not.