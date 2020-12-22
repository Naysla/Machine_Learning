#Implementar modelos de interacción en scikit-learn
#Es hora de agregar funciones de interacción a su modelo. El PolynomialFeaturesobjeto en scikit-learn hace justamente eso, pero aquí se va a utilizar un objeto de interacción personalizada, SparseInteractions. Los términos de interacción son una herramienta estadística que le permite a su modelo expresar lo que sucede si dos características aparecen juntas en la misma fila.
#
#SparseInteractionshace lo mismo que PolynomialFeatures, pero utiliza matrices dispersas para hacerlo. Puede obtener el código SparseInteractionsen este GitHub Gist .
#
#PolynomialFeaturesy SparseInteractionsambos toman el argumento degree, que les dice qué grado polinómico de interacciones calcular.
#
#Vas a considerar los términos de interacción degree=2en tu canalización. Insertará estos pasos después de los pasos de preprocesamiento que ha desarrollado hasta ahora, pero antes de los pasos del clasificador.
#
#Las tuberías con términos de interacción tardan un tiempo en entrenarse (¡ya que está convirtiendo n entidades en n-cuadrados!), Así que siempre que lo configure correctamente, haremos el trabajo pesado y le diremos cuál es su puntaje.

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