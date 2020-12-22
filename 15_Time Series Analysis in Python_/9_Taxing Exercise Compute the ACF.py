#Taxing Exercise: Compute the ACF
#In the last chapter, you computed autocorrelations with one lag. Often we are interested in seeing the autocorrelation over many lags. The quarterly earnings for H&R Block (ticker symbol HRB) is plotted on the right, and you can see the extreme cyclicality of its earnings. A vast majority of its earnings occurs in the quarter that taxes are due.
#
#You will compute the array of autocorrelations for the H&R Block quarterly earnings that is pre-loaded in the DataFrame HRB. Then, plot the autocorrelation function using the plot_acf module. This plot shows what the autocorrelation function looks like for cyclical earnings data. The ACF at lag=0 is always one, of course. In the next exercise, you will learn about the confidence interval for the ACF, but for now, suppress the confidence interval by setting alpha=1.

# Import the acf module and the plot_acf module from statsmodels
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf

# Compute the acf array of HRB
acf_array = acf(HRB)
print(acf_array)

# Plot the acf function
plot_acf(HRB, alpha=1)
plt.show()

[ 1.         -0.22122696 -0.39856504 -0.26615093  0.83479804 -0.1901038
     -0.3475634  -0.23140368  0.71995993 -0.15661007 -0.29766783 -0.22097189
      0.61656933 -0.15022869 -0.27922022 -0.22465946  0.5725259  -0.08758288
     -0.24075584 -0.20363054  0.4797058  -0.06091139 -0.20935484 -0.18303202
      0.42481275 -0.03352559 -0.17471087 -0.16384328  0.34341079 -0.01734364
     -0.13820811 -0.12232172  0.28407164 -0.01927656 -0.11757974 -0.10386933
      0.20156485 -0.0120634  -0.07509539 -0.0707104   0.10222029]
	  
	  #Notice the strong positive autocorrelation at lags 4, 8, 12, 16,20, ...