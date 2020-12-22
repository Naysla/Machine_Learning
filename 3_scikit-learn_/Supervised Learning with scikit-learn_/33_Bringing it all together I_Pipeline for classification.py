#33_Bringing it all together I: Pipeline for classification
#It is time now to piece together everything you have learned so far into a pipeline for classification! Your job in this exercise is to build a pipeline that includes scaling and hyperparameter tuning to classify wine quality.
#
#You'll return to using the SVM classifier you were briefly introduced to earlier in this chapter. The hyperparameters you will tune are C and gamma. C controls the regularization strength. It is analogous to the C you tuned for logistic regression in Chapter 3, while gamma controls the kernel coefficient: Do not worry about this now as it is beyond the scope of this course.
#
#The following modules and functions have been pre-loaded: Pipeline, SVC, train_test_split, GridSearchCV, classification_report, accuracy_score. The feature and target variable arrays X and y have also been pre-loaded.

#Los siguientes módulos y funciones han sido pre-cargado: Pipeline, SVC, train_test_split, GridSearchCV, classification_report, accuracy_score. Los arrays de funciones y variables objetivo Xy ytambién han sido pre-cargado.

from sklearn.model_selection import GridSearchCV
# Setup the pipeline
steps = [('scaler', StandardScaler()),
         ('SVM', SVC())]

pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {'SVM__C':[1, 10, 100],
              'SVM__gamma':[0.1, 0.01]}

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=21)

# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline,parameters,cv=3)
#cv = GridSearchCV(pipeline,steps)

# Fit to the training set
cv.fit(X_train,y_train)

# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)

# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))

#Answer
#Accuracy: 0.7795918367346939
#             precision    recall  f1-score   support
#
#      False       0.83      0.85      0.84       662
#       True       0.67      0.63      0.65       318
#
#avg / total       0.78      0.78      0.78       980
#
#Tuned Model Parameters: {'SVM__C': 10, 'SVM__gamma': 0.1}


