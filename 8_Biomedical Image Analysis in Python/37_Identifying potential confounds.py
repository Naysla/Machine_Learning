#Identifying potential confounds
#Once measures have been extracted, double-check for dependencies within your data. This is especially true if any image parameters (sampling rate, field of view) might differ between subjects, or you pull multiple measures from a single image.
#
#For the final exercises, we have combined demographic and brain volume measures into a pandas DataFrame (df).
#
#First, you will explore the table and available variables. Then, you will check for correlations between the data.

#Print three random rows in df using the .sample() method.


print(df.sample(3))

#<script.py> output:
#               age sex  alzheimers  brain_vol    skull_vol
#    OAS1_0065   90   M       False    670.187  1245.058802

#Print the unique number of individuals with Alzheimer's disease patients.

# Print prevalence of Alzheimer's Disease
print(df.alzheimers.value_counts())

#Print the correlation table between each variable.
# Print a correlation table
print(df.corr())

#rbrainvol,skullvol=0.69

#Great work! There is a high correlation - nearly 0.7 - between the brain_vol and skull_vol. We should be wary of this (and other highly correlated variables) when interpreting results.



