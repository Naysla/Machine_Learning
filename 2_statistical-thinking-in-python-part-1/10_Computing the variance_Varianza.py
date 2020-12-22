#Varianza
#La varianza es una medida de dispersión que representa la variabilidad de una serie de datos respecto a su media. Formalmente se calcula como la suma de las residuos al cuadrado divididos entre el total de observaciones. También se puede calcular como la desviación típica al cuadrado.

#It is important to have some understanding of what commonly-used functions are doing under the hood. Though you may already know how to compute variances, this is a beginner course that does not assume so. In this exercise, we will explicitly compute the variance of the petal length of Iris veriscolor using the equations discussed in the videos. We will then use np.var() to compute it.

#Es importante tener cierta comprensión de lo que las funciones de uso común están haciendo bajo el capó. Aunque es posible que ya sepa cómo calcular las variaciones, este es un curso para principiantes que no asume eso. En este ejercicio, calcularemos explícitamente la varianza de la longitud del pétalo de Iris veriscolor usando las ecuaciones discutidas en los videos. Luego lo usaremos np.var()para calcularlo.

#Varianza
#np.var(dem_share_FL) 

#Desviacion estandar
#np.std(dem_share_FL)
#np.sqrt(np.var(dem_share_FL)) 

# Array of differences to mean: differences
import numpy as np
# versicolor_petal_length preloaded
differences= np.array(versicolor_petal_length- np.mean(versicolor_petal_length))

# Square the differences: diff_sq
diff_sq=differences**2

# Compute the mean square difference: variance_explicit
variance_explicit= np.mean(diff_sq) 

# Compute the variance using NumPy: variance_np
variance_np= np.var(versicolor_petal_length)

# Print the results
print(variance_explicit, variance_np)


#devuelve la varianza explicita y la varianza calculada
#0.21640000000000004 0.21640000000000004

