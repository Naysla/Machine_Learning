#Looking at a Regression's R-Squared
#R-squared measures how closely the data fit the regression line, so the R-squared in a simple regression is related to the correlation between the two variables. In particular, the magnitude of the correlation is the square root of the R-squared and the sign of the correlation is the sign of the regression coefficient.
#
#In this exercise, you will start using the statistical package statsmodels, which performs much of the statistical modeling and testing that is found in R and software packages like SAS and MATLAB.
#
#You will take two series, x and y, compute their correlation, and then regress y on x using the function OLS(y,x) in the statsmodels.api library (note that the dependent, or right-hand side variable y is the first argument). Most linear regressions contain a constant term which is the intercept (the a in the regression yt=a+�xt+?t). To include a constant using the function OLS(), you need to add a column of 1's to the right hand side of the regression.
#
#The module statsmodels.api has been imported for you as sm.

# Import the statsmodels module
import statsmodels.api as sm

# Compute correlation of x and y
correlation = x.corr(y)
print("The correlation between x and y is %4.2f" %(correlation))

# Convert the Series x to a DataFrame and name the column x
dfx = pd.DataFrame(x, columns=['x'])

# Add a constant to the DataFrame dfx
dfx1 = sm.add_constant(dfx)

# Regress y on dfx1
result = sm.OLS(y, dfx1).fit()

# Print out the results and look at the relationship between R-squared and the correlation above
print(result.summary())

 #   The correlation between x and y is -0.90
 #                               OLS Regression Results                            
 #   ==============================================================================
 #   Dep. Variable:                      y   R-squared:                       0.818
 #   Model:                            OLS   Adj. R-squared:                  0.817
 #   Method:                 Least Squares   F-statistic:                     4471.
 #   Date:                Sun, 06 Sep 2020   Prob (F-statistic):               0.00
 #   Time:                        22:12:33   Log-Likelihood:                -560.10
 #   No. Observations:                1000   AIC:                             1124.
 #   Df Residuals:                     998   BIC:                             1134.
 #   Df Model:                           1                                         
 #   Covariance Type:            nonrobust                                         
 #   ==============================================================================
 #                    coef    std err          t      P>|t|      [0.025      0.975]
 #   ------------------------------------------------------------------------------
 #   const         -0.0052      0.013     -0.391      0.696      -0.032       0.021
 #   x             -0.9080      0.014    -66.869      0.000      -0.935      -0.881
 #   ==============================================================================
 #   Omnibus:                        0.048   Durbin-Watson:                   2.066
 #   Prob(Omnibus):                  0.976   Jarque-Bera (JB):                0.103
 #   Skew:                          -0.003   Prob(JB):                        0.950
 #   Kurtosis:                       2.951   Cond. No.                         1.03
 #   ==============================================================================
 #   
 #   Warnings:
 #   [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
	
	
	#Notice that the two different methods of computing correlation give the same result. The correlation is about -0.9 and the R-squared is about 0.81