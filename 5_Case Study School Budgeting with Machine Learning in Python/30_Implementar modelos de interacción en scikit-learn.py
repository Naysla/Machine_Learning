#Implementar modelos de interacci�n en scikit-learn
#Es hora de agregar funciones de interacci�n a su modelo. El PolynomialFeaturesobjeto en scikit-learn hace justamente eso, pero aqu� se va a utilizar un objeto de interacci�n personalizada, SparseInteractions. Los t�rminos de interacci�n son una herramienta estad�stica que le permite a su modelo expresar lo que sucede si dos caracter�sticas aparecen juntas en la misma fila.
#
#SparseInteractionshace lo mismo que PolynomialFeatures, pero utiliza matrices dispersas para hacerlo. Puede obtener el c�digo SparseInteractionsen este GitHub Gist .
#
#PolynomialFeaturesy SparseInteractionsambos toman el argumento degree, que les dice qu� grado polin�mico de interacciones calcular.
#
#Vas a considerar los t�rminos de interacci�n degree=2en tu canalizaci�n. Insertar� estos pasos despu�s de los pasos de preprocesamiento que ha desarrollado hasta ahora, pero antes de los pasos del clasificador.
#
#Las tuber�as con t�rminos de interacci�n tardan un tiempo en entrenarse (�ya que est� convirtiendo n entidades en n-cuadrados!), As� que siempre que lo configure correctamente, haremos el trabajo pesado y le diremos cu�l es su puntaje.

# Instantiate pipeline: pl
pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list = [
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', Imputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC,
                                                   ngram_range=(1, 2))),  
                    ('dim_red', SelectKBest(chi2, chi_k))
                ]))
             ]
        )),
        ('int', SparseInteractions(degree=2)),
        ('scale', MaxAbsScaler()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])
	
#Answer
#Log loss score: 1.2256. Nice improvement from 1.2681! The student is becoming the master!