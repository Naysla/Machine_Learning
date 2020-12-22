#Evaluate the model
#Remember the test data that you set aside waaaaaay back in chapter 3? It's finally time to test your model on it! You can use the same evaluator you made to fit the model.

# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))

#Congratulations! What do you think of the AUC? Your model isn't half bad! You went from knowing nothing about Spark to doing advanced machine learning. Great job on making it to the end of the course! The next steps are learning how to create large scale Spark clusters and manage and submit jobs so that you can use models in the real world. Check out some of the other DataCamp courses that use Spark! And remember, Spark is still being actively developed, so there's new features coming all the time!