#Regularization and probabilities
#In this exercise, you will observe the effects of changing the regularization strength on the predicted probabilities.
#
#A 2D binary classification dataset is already loaded into the environment as X and y.

# Set the regularization strength
model = LogisticRegression(C=1)

# Fit and plot
model.fit(X,y)
plot_classifier(X,y,model,proba=True)

# Predict probabilities on training points
prob = model.predict_proba(X)
print("Maximum predicted probability", np.max(prob))

#Answer

#Devuelve una grafica indicando 50 y 50 de probabilidad, devuelvelos siguientes valores
Maximum predicted probability [[0.9209835  0.0790165 ]
 [0.95866275 0.04133725]
 [0.84074059 0.15925941]
 [0.07667962 0.92332038]
 [0.07026958 0.92973042]
 [0.48558394 0.51441606]
 [0.023877   0.976123  ]
 [0.07068669 0.92931331]
 [0.1125408  0.8874592 ]
 [0.95855226 0.04144774]
 [0.71378564 0.28621436]
 [0.10913863 0.89086137]
 [0.04431288 0.95568712]
 [0.89400692 0.10599308]
 [0.03608222 0.96391778]
 [0.61928355 0.38071645]
 [0.77089251 0.22910749]
 [0.9511639  0.0488361 ]
 [0.85283928 0.14716072]
 [0.92092304 0.07907696]]
 
 # Set the regularization strength
model = LogisticRegression(C=1)

#==============================================================================

# Set the regularization strength
model = LogisticRegression(C=0.1)

# Fit and plot
model.fit(X,y)
plot_classifier(X,y,model,proba=True)

# Predict probabilities on training points
prob = model.predict_proba(X)
print("Maximum predicted probability", np.max(prob))

#devuelve que rojo tiene mas probabilidad en la grafica

Maximum predicted probability [[0.67168317 0.32831683]
 [0.75160868 0.24839132]
 [0.59689789 0.40310211]
 [0.17413171 0.82586829]
 [0.16740845 0.83259155]
 [0.39661788 0.60338212]
 [0.10090343 0.89909657]
 [0.16742907 0.83257093]
 [0.208472   0.791528  ]
 [0.746066   0.253934  ]
 [0.51330603 0.48669397]
 [0.19535921 0.80464079]
 [0.14029265 0.85970735]
 [0.64426922 0.35573078]
 [0.12719146 0.87280854]
 [0.44577301 0.55422699]
 [0.55036297 0.44963703]
 [0.74079094 0.25920906]
 [0.61274386 0.38725614]
 [0.67622691 0.32377309]]

Maximum predicted probability 0.8990965659596716

#You got it! As you probably noticed, smaller values of C lead to less confident predictions. That's because smaller C means more regularization, which in turn means smaller coefficients, which means raw model outputs closer to zero and, thus, probabilities closer to 0.5 after the raw model output is squashed through the sigmoid function. That's quite a chain of events!