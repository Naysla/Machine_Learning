#Sentiment analysis for movie reviews
#In this exercise you'll explore the probabilities outputted by logistic regression on a subset of the Large Movie Review Dataset.

#The variables X and y are already loaded into the environment. X contains features based on the number of times words appear in the movie reviews, and y contains labels for whether the review sentiment is positive (+1) or negative (-1).

# Instantiate logistic regression and train
lr = LogisticRegression()
lr.fit(X,y)

# Predict sentiment for a glowing review
review1 = "LOVED IT! This movie was amazing. Top 10 this year."
review1_features = get_features(review1)
print("Review:", review1)
print("Probability of positive review:", lr.predict_proba(review1_features)[0,1])

# Predict sentiment for a poor review
review2 = "Total junk! I'll never watch a film by that director again, no matter how good the reviews."
review2_features = get_features(review2)
print("Review:", review2)
print("Probability of positive review:", lr.predict_proba(review2_features)[0,1])

#Answer



Review: LOVED IT! This movie was amazing. Top 10 this year.
Probability of positive review: 0.8079007873616059
Review: Total junk! I'll never watch a film by that director again, no matter how good the reviews.
Probability of positive review: 0.5855117402793947

#Fantastic! The second probability would have been even lower, but the word "good" trips it up a bit, since that's considered a "positive" word.