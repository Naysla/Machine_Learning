#covarianza
#la covarianza es un valor que indica el grado de variaci�n conjunta de dos variables aleatorias respecto a sus medias.

#Gr�fico de dispersi�n
#Cuando hiciste diagramas de enjambre de abejas, diagramas de caja y diagramas de ECDF en ejercicios anteriores, comparaste las longitudes de p�talos de diferentes especies de iris. Pero, �qu� pasa si quieres comparar dos propiedades de una sola especie? Esto es exactamente lo que haremos en este ejercicio. Haremos un diagrama de dispersi�n de las medidas de longitud y ancho de p�talos de las flores versicolor Iris de Anderson . Si la flor escala (es decir, conserva su proporci�n a medida que crece), esperar�amos que la longitud y el ancho est�n correlacionados.
#
#Para su referencia, el c�digo utilizado para producir el diagrama de dispersi�n en el video se proporciona a continuaci�n:
#
#_ = plt.plot(total_votes/1000, dem_share, marker='.', linestyle='none')
#
#_ = plt.xlabel('total votes (thousands)')
#
#_ = plt.ylabel('percent of vote for Obama')

# Make a scatter plot

_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')


# Label the axes
_=plt.xlabel('petal length')
_=plt.ylabel('petal width')


# Show the result
plt.show()

#devuelve una grafica para analizar la covarianzade la data especificada en plt.plot

#The covariance may be computed using the Numpy function np.cov()