#Fitting multi-class logistic regression
#In this exercise, you'll fit the two types of multi-class logistic regression, one-vs-rest and softmax/multinomial, on the handwritten digits data set and compare the results. The handwritten digits dataset is already loaded and split into X_train, y_train, X_test, and y_test.

# Fit one-vs-rest logistic regression classifier
lr_ovr = LogisticRegression()
lr_ovr.fit(X_train, y_train)

print("OVR training accuracy:", lr_ovr.score(X_train, y_train))
print("OVR test accuracy    :", lr_ovr.score(X_test, y_test))


#Answer1
OVR training accuracy: 0.9948032665181886
OVR test accuracy    : 0.9644444444444444


#======================================
# Fit softmax classifier --> multinomial
lr_mn = LogisticRegression(multi_class="multinomial",solver="lbfgs")
lr_mn.fit(X_train, y_train)

print("Softmax training accuracy:", lr_mn.score(X_train, y_train))
print("Softmax test accuracy    :", lr_mn.score(X_test, y_test))

#Answer2
Softmax training accuracy: 1.0
Softmax test accuracy    : 0.9688888888888889

#Es mas exacta la respuesta de la funcion multinomial
#Nice work! As you can see, the accuracies of the two methods are fairly similar on this data set.