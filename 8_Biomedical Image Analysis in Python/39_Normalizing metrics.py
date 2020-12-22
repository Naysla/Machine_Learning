#Normalizing metrics
#We previously saw that there was not a significant difference between the brain volumes of elderly individuals with and without Alzheimer's Disease.
#
#But could a correlated measure, such as "skull volume" be masking the differences?
#
#For this exercise, calculate a new test statistic for the comparison of brain volume between groups, after adjusting for the subject's skull size.
#
#Using results.statistic and results.pvalue as your guide, answer the question: Is there strong evidence that Alzheimer's Disease is marked by smaller brain size, relative to skull size?

# Import independent two-sample t-test
from scipy.stats import ttest_ind

# Adjust `brain_vol` by `skull_vol`
df['adj_brain_vol'] = df.brain_vol / df.skull_vol

# Select brain measures by group
brain_alz = df.loc[df.alzheimers == True, 'adj_brain_vol']
brain_typ = df.loc[df.alzheimers == False, 'adj_brain_vol']

# Evaluate null hypothesis
results = ttest_ind(brain_alz, brain_typ)

print('t = ', results.statistic)
print('p = ', results.pvalue)

#t =  -5.850136931483197
#p =  2.1902794284991254e-08

#Congratulations! You've worked your way through several levels of biomedical image analysis and are well-prepared for tackling new datasets and problems. For more advanced tools, I recommend checking out scikit-image, which extends the capabilities of scipy for image processing. Good luck!