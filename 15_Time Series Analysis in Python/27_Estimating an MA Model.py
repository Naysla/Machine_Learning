#Estimating an MA Model
#You will estimate the MA(1) parameter, θ, of one of the simulated series that you generated in the earlier exercise. Since the parameters are known for a simulated series, it is a good way to understand the estimation routines before applying it to real data.
#
#For simulated_data_1 with a true θ of -0.9, you will print out the estimate of θ. In addition, you will also print out the entire output that is produced when you fit a time series, so you can get an idea of what other tests and summary statistics are available in statsmodels.

# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA

# Fit an MA(1) model to the first simulated data
mod = ARMA(simulated_data_1, order=(0,1))
res = mod.fit()

# Print out summary information on the fit
print(res.summary())

# Print out the estimate for the constant and for theta
print("When the true theta=-0.9, the estimate of theta (and the constant) are:")
print(res.params)

 ARMA Model Results                              
==============================================================================
Dep. Variable:                      y   No. Observations:                 1000
Model:                     ARMA(0, 1)   Log Likelihood               -1420.500
Method:                       css-mle   S.D. of innovations              1.001
Date:                Sun, 20 Sep 2020   AIC                           2846.999
Time:                        19:05:40   BIC                           2861.723
Sample:                             0   HQIC                          2852.595
                                                                              
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0038      0.003     -1.166      0.244      -0.010       0.003
ma.L1.y       -0.8967      0.015    -59.984      0.000      -0.926      -0.867
                                    Roots                                    
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
MA.1            1.1152           +0.0000j            1.1152            0.0000
-----------------------------------------------------------------------------
When the true theta=-0.9, the estimate of theta (and the constant) are:
[-0.00384352 -0.8967135 ]


#Notice how close the estimated parameter is to the true parameter.