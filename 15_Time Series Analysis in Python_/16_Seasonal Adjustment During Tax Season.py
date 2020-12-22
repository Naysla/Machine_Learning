#Seasonal Adjustment During Tax Season
#Many time series exhibit strong seasonal behavior. The procedure for removing the seasonal component of a time series is called seasonal adjustment. For example, most economic data published by the government is seasonally adjusted.
#
#You saw earlier that by taking first differences of a random walk, you get a stationary white noise process. For seasonal adjustments, instead of taking first differences, you will take differences with a lag corresponding to the periodicity.
#
#Look again at the ACF of H&R Block's quarterly earnings, pre-loaded in the DataFrame HRB, and there is a clear seasonal component. The autocorrelation is high for lags 4,8,12,16,… because of the spike in earnings every four quarters during tax season. Apply a seasonal adjustment by taking the fourth difference (four represents the periodicity of the series). Then compute the autocorrelation of the transformed series.

# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf

# Seasonally adjust quarterly earnings
HRBsa = HRB.diff(4)

# Print the first 10 rows of the seasonally adjusted series
print(HRBsa.head(10))

# Drop the NaN data in the first four rows
HRBsa = HRBsa.dropna()

# Plot the autocorrelation function of the seasonally adjusted series
plot_acf(HRBsa)
plt.show()

#By seasonally adjusting the series, we eliminated the seasonal pattern in the autocorrelation function

#<script.py> output:
#            Earnings
#   Quarter          
#   2007Q1        NaN
#   2007Q2        NaN
#   2007Q3        NaN
#   2007Q4        NaN
#   2008Q1       0.02
#   2008Q2      -0.04
#   2008Q3      -0.05
#   2008Q4       0.26
#   2009Q1      -0.05
#   2009Q2       0.02