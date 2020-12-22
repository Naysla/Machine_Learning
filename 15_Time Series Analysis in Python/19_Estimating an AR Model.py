#Estimating an AR Model
#You will estimate the AR(1) parameter, ϕ, of one of the simulated series that you generated in the earlier exercise. Since the parameters are known for a simulated series, it is a good way to understand the estimation routines before applying it to real data.
#
#For simulated_data_1 with a true ϕ of 0.9, you will print out the estimate of ϕ. In addition, you will also print out the entire output that is produced when you fit a time series, so you can get an idea of what other tests and summary statistics are available in statsmodels.

# Import the ARMA module from statsmodels
from statsmodels.tsa.arima_model import ARMA

# Fit an AR(1) model to the first simulated data
mod = ARMA(simulated_data_1, order=(1,0))
res = mod.fit()

# Print out summary information on the fit
print(res.summary())

# Print out the estimate for the constant and for phi
print("When the true phi=0.9, the estimate of phi (and the constant) are:")
print(res.params)

#                             ARMA Model Results                              
==============================================================================
Dep. Variable:                      y   No. Observations:                 1000
Model:                     ARMA(1, 0)   Log Likelihood               -1420.051
Method:                       css-mle   S.D. of innovations              1.000
Date:                Sun, 20 Sep 2020   AIC                           2846.103
Time:                        17:56:55   BIC                           2860.826
Sample:                             0   HQIC                          2851.699
                                                                              
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.3986      0.317     -1.257      0.209      -1.020       0.223
ar.L1.y        0.9011      0.014     66.094      0.000       0.874       0.928
                                    Roots                                    
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.1097           +0.0000j            1.1097            0.0000
-----------------------------------------------------------------------------
When the true phi=0.9, the estimate of phi (and the constant) are:
[-0.39859166  0.90110551]


#const         -0.3986
#ar.L

#Notice how close the estimated parameter is to the true parameter.