#k-Nearest Neighbors: Fit

#Habiendo explorado el conjunto de datos de los registros de votación del Congreso, es hora de construir su primer clasificador. En este ejercicio, ajustará un clasificador k-Nearest Neighbours al conjunto de datos de votación, que una vez más se ha cargado previamente en un DataFrame df.
#
#En el video, Hugo discutió la importancia de garantizar que sus datos se adhieran al formato requerido por la API scikit-learn. Las características deben estar en una matriz donde cada columna es una característica y cada fila es un punto de observación o de datos diferente, en este caso, el registro de votación de un congresista. El objetivo debe ser una sola columna con el mismo número de observaciones que los datos de la característica. Lo hemos hecho por usted en este ejercicio. Observe que nombramos la matriz de características Xy la variable de respuesta y: esto está de acuerdo con la práctica común de aprendizaje de scikit.
#
#Su trabajo es crear una instancia de un clasificador k-NN con 6 vecinos (especificando el n_neighborsparámetro) y luego ajustarlo a los datos. Los datos se han precargado en un DataFrame llamado df.

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn= KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)


#Answer
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=6, p=2,
           weights='uniform')