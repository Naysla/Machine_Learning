#Will the bank fail?
#Plot the number of defaults you got from the previous exercise, in your namespace as n_defaults, as a CDF. The ecdf() function you wrote in the first chapter is available.
#
#If interest rates are such that the bank will lose money if 10 or more of its loans are defaulted upon, what is the probability that the bank will lose money?

#Trace el número de valores predeterminados que obtuvo del ejercicio anterior, en su espacio de nombres como n_defaults, como un CDF. La ecdf()función que escribió en el primer capítulo está disponible.
#
#Si las tasas de interés son tales que el banco perderá dinero si se dejan de pagar 10 o más de sus préstamos, ¿cuál es la probabilidad de que el banco pierda dinero?

# Compute ECDF: x, y
import numpy as np
x, y = ecdf (n_defaults)

# Plot the ECDF with labeled axes
_=plt.plot(x,y,marker = '.',linestyle = 'none')
_ = plt.xlabel('probability') 
_ = plt.ylabel('ECDF') 


# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money=np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))

#devuelve una grafica