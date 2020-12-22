#GridSearchCV warm-up
#In the video we saw that increasing the RBF kernel hyperparameter gamma increases training accuracy. In this exercise we'll search for the gamma that maximizes cross-validation accuracy using scikit-learn's GridSearchCV. A binary version of the handwritten digits dataset, in which you're just trying to predict whether or not an image is a "2", is already loaded into the variables X and y

#En el video vimos que aumentar el hiperparámetro del núcleo RBF gammaaumenta la precisión del entrenamiento. En este ejercicio buscaremos el gammaque maximiza la precisión de la validación cruzada utilizando scikit-learn GridSearchCV

# Instantiate an RBF SVM
svm = SVC()

# Instantiate the GridSearchCV object and run the search
parameters = {'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
searcher = GridSearchCV(svm, parameters)
searcher.fit(X,y)

# Report the best parameters
print("Best CV params", searcher.best_params_)

#Answer

Best CV params {'gamma': 0.001}

#Great job! Larger values of gamma are better for training accuracy, but cross-validation helped us find something different (and better!).