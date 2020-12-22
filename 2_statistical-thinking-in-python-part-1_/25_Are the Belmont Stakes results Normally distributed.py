#Calcula la normal teorica y real de dos arreglos
#los muestra en la misma gr�fica
#Are the Belmont Stakes results Normally distributed?
#Since 1926, the Belmont Stakes is a 1.5 mile-long race of 3-year old thoroughbred horses. Secretariat ran the fastest Belmont Stakes in history in 1973. While that was the fastest year, 1970 was the slowest because of unusually wet and sloppy conditions. With these two outliers removed from the data set, compute the mean and standard deviation of the Belmont winners' times. Sample out of a Normal distribution with this mean and standard deviation using the np.random.normal() function and plot a CDF. Overlay the ECDF from the winning Belmont times. Are these close to Normally distributed?
#
#Note: Justin scraped the data concerning the Belmont Stakes from the Belmont Wikipedia page.

# Compute mean and standard deviation: mu, sigma
#belmont_no_outliers is a numpyarray
mu = np.mean(belmont_no_outliers)
sigma= np.std(belmont_no_outliers)

# Sample out of a normal distribution with this mu and sigma: samples
samples= np.random.normal(mu, sigma, size=10000) 

# Get the CDF of the samples and of the data
x, y = ecdf(belmont_no_outliers) 
x_theor, y_theor = ecdf(samples) 


# Plot the CDFs and show the plot
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.xlabel('Belmont winning time (sec.)')
_ = plt.ylabel('CDF')
plt.show()


#The theoretical CDF and the ECDF of the data suggest that the winning Belmont times are, indeed, Normally distributed. This also suggests that in the last 100 years or so, there have not been major technological or training advances that have significantly affected the speed at which horses can run this race.