#Can you adjust the model or parameters to improve accuracy?
#You just saw a substantial improvement in accuracy by swapping out the model. Pipelines are amazing!
#
#Can you make it better? Try changing the parameter n_estimators of RandomForestClassifier(), whose default value is 10, to 15.


# Import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

# Add model step to pipeline: pl
pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list = [
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', Imputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer())
                ]))
             ]
        )),
        ('clf', RandomForestClassifier(n_estimators=15))
    ])

# Fit to the training data
pl.fit(X_train, y_train)

# Compute and print accuracy
accuracy = pl.score(X_test, y_test)
print("\nAccuracy on budget dataset: ", accuracy)

#Answer
#Accuracy on budget dataset:  0.3211538461538462
#Wow, you're becoming a master! It's time to get serious and work with the log loss metric. You'll learn expert techniques in the next chapter to take the model to the next level.