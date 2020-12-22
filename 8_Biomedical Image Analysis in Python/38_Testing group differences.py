#Testing group differences
#Let's test the hypothesis that Alzheimer's Disease is characterized by reduced brain volume.
#
#We can perform a two-sample t-test between the brain volumes of elderly adults with and without Alzheimer's Disease. In this case, the two population samples are independent from each other because they are all separate subjects.
#
#For this exercise, use the OASIS dataset (df) and ttest_ind to evaluate the hypothesis.

#Import ttest_ind() from scipy.stats.

from scipy.stats import ttest_ind

# Select data from "alzheimers" and "typical" groups
brain_alz = df.loc[df.alzheimers == True, 'brain_vol']
brain_typ = df.loc[df.alzheimers == False, 'brain_vol']

# Perform t-test of "alz" > "typ"
results = ttest_ind(brain_alz,brain_typ)
print('t = ', results.statistic)
print('p = ', results.pvalue)


# Show boxplot of brain_vol differences
df.boxplot(column='brain_vol', by='alzheimers')
plt.show()

#t =  -1.9646603431952554
#p =  0.050951046028341454

#There is some evidence for decreased brain volume in individuals with Alzheimer's Disease. Since the p-value for this t-test is greater than 0.05, we would not reject the null hypothesis that states the two groups are equal.