#Muestreo fuera de la distribución binomial
#Calcule la función de masa de probabilidad para el número de incumplimientos que esperaríamos para 100 préstamos como en la última sección, pero en lugar de simular todos los ensayos de Bernoulli, realice el muestreo utilizando np.random.binomial(). Esto es idéntico al cálculo que hizo en el último conjunto de ejercicios utilizando su perform_bernoulli_trials()función personalizada, pero mucho más eficiente computacionalmente. Dada esta eficiencia adicional, tomaremos 10,000 muestras en lugar de 1000. Después de tomar las muestras, grafique el CDF como la última vez. Este CDF que está trazando es el de la distribución Binomial.
#
#Nota : Para este ejercicio y para todos en adelante, el generador de números aleatorios está pre-sembrado para usted (con np.random.seed(42)) para evitar que escriba cada vez.

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
