#Visualizing easy and difficult examples
#In this exercise, you'll visualize the examples that the logistic regression model is most and least confident about by looking at the largest and smallest predicted probabilities.
#
#The handwritten digits dataset is already loaded into the variables X and y. The show_digit function takes in an integer index and plots the corresponding image, with some extra information displayed above the image.

lr = LogisticRegression()
lr.fit(X,y)

# Get predicted probabilities
proba = lr.predict_proba(X)

# Sort the example indices by their maximum probability
proba_inds = np.argsort(np.max(proba,axis=1))
#print(np.max(proba_inds))
# Show the most confident (least ambiguous) digit
show_digit(proba_inds[-1] , lr) 

# Show the least confident (most ambiguous) digit
show_digit(proba_inds[0], lr)

#Answer

#la clave es : proba_inds[-1] y proba_inds[0] devuelve una grafica indicando las probabilidades , sin embargo es complejo, no es una grafica ordenada como la de los ejercicios anteriores, no es facil identificar la probabilidad generada.

#Great job! As you can see, the least confident example looks like a weird 4, and the most confident example looks like a very typical 0.