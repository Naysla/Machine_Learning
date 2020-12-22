#Running LogisticRegression and SVC
#In this exercise, you'll apply logistic regression and a support vector machine to classify images of handwritten digits.

from sklearn import datasets
digits = datasets.load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

# Apply logistic regression and print scores
lr = LogisticRegression()
lr.fit(X_train,y_train)
print(lr.score(X_train,y_train))
print(lr.score(X_test, y_test))

# Apply SVM and print scores
svm = SVC()
svm.fit(X_train,y_train)
print(svm.score(X_test, y_test))
print(svm.score(X_test, y_test))

#Answer

0.9955456570155902
0.9622222222222222
0.48
0.48


#Nicely done! Later in the course we'll look at the similarities and differences of logistic regression vs. SVMs.