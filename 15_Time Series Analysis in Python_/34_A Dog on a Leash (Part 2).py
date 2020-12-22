#A Dog on a Leash? (Part 2)
#To verify that Heating Oil and Natural Gas prices are cointegrated, First apply the Dickey-Fuller test separately to show they are random walks. Then apply the test to the difference, which should strongly reject the random walk hypothesis. The Heating Oil and Natural Gas prices are pre-loaded in DataFrames HO and NG.

# Import the adfuller module from statsmodels
from statsmodels.tsa.stattools import adfuller

# Compute the ADF for HO and NG
result_HO = adfuller(HO['Close'])
print("The p-value for the ADF test on HO is ", result_HO[1])
result_NG = adfuller(NG['Close'])
print("The p-value for the ADF test on NG is ", result_NG[1])

# Compute the ADF of the spread
result_spread = adfuller(7.25 * HO['Close'] - NG['Close'])
print("The p-value for the ADF test on the spread is ", result_spread[1])

#<script.py> output:
#    The p-value for the ADF test on HO is  0.9567108785017869
#    The p-value for the ADF test on NG is  0.900874744467673
#    The p-value for the ADF test on the spread is  7.01943930214218e-05

#As we expected, we cannot reject the hypothesis that the individual futures are random walks, but we can reject that the spread is a random walk.