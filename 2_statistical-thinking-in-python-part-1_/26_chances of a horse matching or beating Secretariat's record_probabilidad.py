#�Cu�les son las posibilidades de que un caballo coincida o supere el r�cord de la Secretar�a?
#Suponga que los tiempos de los ganadores de Belmont se distribuyen normalmente (con los a�os 1970 y 1973 eliminados), �cu�l es la probabilidad de que el ganador de un determinado Belmont Stakes lo corra tan r�pido o m�s r�pido que la Secretar�a?
#
#What are the chances of a horse matching or beating Secretariat's record?
#Assume that the Belmont winners' times are Normally distributed (with the 1970 and 1973 years removed), what is the probability that the winner of a given Belmont Stakes will run it as fast or faster than Secretariat?

# Take a million samples out of the Normal distribution: samples
#mu = np.mean(belmont_no_outliers)
#sigma= np.std(belmont_no_outliers)
samples=np.random.normal(mu,sigma,size=1000000)

# Compute the fraction that are faster than 144 seconds: prob
prob= np.sum(samples <= 144)
prob= prob / len(samples)
# Print the result
print('Probability of besting Secretariat:', prob)
#Probability of besting Secretariat: 0.000685