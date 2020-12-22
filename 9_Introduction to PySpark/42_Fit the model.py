#Fit the model(s)
#You're finally ready to fit the models and select the best one!
#
#Unfortunately, cross validation is a very computationally intensive procedure. Fitting all the models would take too long on DataCamp.
#
#To do this locally you would use the code:
#
#	# Fit cross validation models
#	models = cv.fit(training)
#
#	# Extract the best model
#	best_lr = models.bestModel
#	
#Remember, the training data is called training and you're using lr to fit a logistic regression model. Cross validation selected the parameter values regParam=0 and elasticNetParam=0 as being the best. These are the default values, so you don't need to do anything else with lr before fitting the model.

# Call lr.fit()
best_lr = lr.fit(training)

# Print best_lr
print(best_lr)

#LogisticRegression_40dfa2d4ff7cf6b81c87

#Wow! You fit your first Spark model!