#Distribution of no-hitters and cycles
#Now, you'll use your sampling function to compute the waiting time to observe a no-hitter and hitting of the cycle. The mean waiting time for a no-hitter is 764 games, and the mean waiting time for hitting the cycle is 715 games.

#Distribución de no-hitters y ciclos.
#Ahora, usará su función de muestreo para calcular el tiempo de espera para observar un no-hitter y un hit del ciclo. El tiempo medio de espera para un no hitter es de 764 juegos, y el tiempo medio de espera para alcanzar el ciclo es de 715 juegos.

# Draw samples of waiting times: waiting_times
waiting_times=successive_poisson(764 , 715 ,100000 )

# Make the histogram
_=plt.hist(waiting_times,histtype='step',normed=True,bins=100)


# Label axes
_ = plt.xlabel('x')
_ = plt.ylabel('y')


# Show the plot
plt.show()
