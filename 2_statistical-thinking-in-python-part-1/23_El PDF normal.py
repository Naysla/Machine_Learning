# calcular la nomal
# graficar 3 normales en una grafica
#The Normal PDF
#In this exercise, you will explore the Normal PDF and also learn a way to plot a PDF of a known distribution using hacker statistics. Specifically, you will plot a Normal PDF for various values of the variance.

# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
import numpy as np 
import matplotlib.pyplot as plt 
 
mean = 20
#std= 1,3,10
samples_std1= np.random.normal(mean, 1, size=100000) 
samples_std3=np.random.normal(mean, 3, size=100000)
samples_std10=np.random.normal(mean, 10, size=100000)

# Make histograms
_=plt.hist(samples_std1,histtype='step',normed=True,bins=100)
_=plt.hist(samples_std3,histtype='step',normed=True,bins=100)
_=plt.hist(samples_std10,histtype='step',normed=True,bins=100)

# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
