#Trazando el binomio PMF
#Como se menciona en el video, trazar un PMF de aspecto agradable requiere un poco de truco matplotlib que no vamos a entrar aquí. En cambio, trazaremos el PMF de la distribución Binomial como un histograma con habilidades que ya has aprendido. El truco consiste en configurar los bordes de los contenedores para pasar a plt.hist()través del binsargumento de la palabra clave. Queremos que los contenedores se centren en los enteros. Por lo tanto, los bordes de los contenedores deben estar a la -0.5, 0.5, 1.5, 2.5, ...altura max(n_defaults) + 1.5. Puede generar una matriz como esta usando np.arange()y luego restando 0.5de la matriz.

#Ya ha tomado muestras de la distribución Binomial durante sus ejercicios sobre impagos de préstamos, y las muestras resultantes están en la matriz NumPy n_defaults.

#python  función de masa de probabilidad ( pmf )

#numpy.arange(): Otra función que nos permite crear un array NumPy es numpy.arange. Al igual que la función predefinida de Python range, genera un conjunto de números entre un valor de inicio y uno final, pudiendo especificar un incremento entre los valores, pero, al contrario de lo que ocurre con range, el resultado aquí es un array NumPy:

#Continuacion delejercicio 19

# Compute bin edges: bins
bins = np.arange(min(n_defaults), max(n_defaults) + 1.5) - 0.5


# Generate histogram
_=plt.hist(n_defaults,normed=True,bins=bins)

# Label axes
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')


# Show the plot
plt.show()

#Devuelve un histograma