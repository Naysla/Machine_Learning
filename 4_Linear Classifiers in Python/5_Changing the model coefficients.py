#Changing the model coefficients
#When you call fit with scikit-learn, the logistic regression coefficients are automatically learned from your dataset. In this exercise you will explore how the decision boundary is represented by the coefficients. To do so, you will change the coefficients manually (instead of with fit), and visualize the resulting classifiers.

#A 2D dataset is already loaded into the environment as X and y, along with a linear classifier object model.

# Set the coefficients
model.coef_ = np.array([[-1,1]])
model.intercept_ = np.array([-2.5])

# Plot the data and decision boundary
plot_classifier(X,y,model)

# Print the number of errors
num_err = np.sum(y != model.predict(X))
print("Number of errors:", num_err)

#Answer
#Se ajustaron los coeficientes de el arreglo y la prediccion a interceptar para que quedaran separados en la grafica los objetos y devolviera un valor 0 de error
#<script.py> output:
#    Number of errors: 0
	
#Great job! As you've been experiencing, the coefficients determine the slope of the boundary and the intercept shifts it.