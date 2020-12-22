#Muestreo fuera de la distribuci�n binomial
#Calcule la funci�n de masa de probabilidad para el n�mero de incumplimientos que esperar�amos para 100 pr�stamos como en la �ltima secci�n, pero en lugar de simular todos los ensayos de Bernoulli, realice el muestreo utilizando np.random.binomial(). Esto es id�ntico al c�lculo que hizo en el �ltimo conjunto de ejercicios utilizando su perform_bernoulli_trials()funci�n personalizada, pero mucho m�s eficiente computacionalmente. Dada esta eficiencia adicional, tomaremos 10,000 muestras en lugar de 1000. Despu�s de tomar las muestras, grafique el CDF como la �ltima vez. Este CDF que est� trazando es el de la distribuci�n Binomial.
#
#Nota : Para este ejercicio y para todos en adelante, el generador de n�meros aleatorios est� pre-sembrado para usted (con np.random.seed(42)) para evitar que escriba cada vez.

# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults=np.random.binomial(100,0.05,size=10000)

# Compute CDF: x, y
import numpy as np
x, y = ecdf (n_defaults)

# Plot the CDF with axis labels
_=plt.plot(x,y,marker = '.',linestyle = 'none')
_ = plt.xlabel('default loans') 
_ = plt.ylabel('CDF') 



# Show the plot
plt.show()
