#Computing percentiles
#In this exercise, you will compute the percentiles of petal length of Iris versicolor.



# Specify array of percentiles: percentiles
import numpy as np
percentiles= np.array([2.5,25, 50, 75,97.5])

# Compute percentiles: ptiles_vers
ptiles_vers=np.percentile(versicolor_petal_length,percentiles)

# Print the result
print(ptiles_vers)

#devuelve los percentiles [3.3    4.     4.35   4.6    4.9775]