#Understanding your classification data
#Now you will start modeling with a new dataset for a classification problem. This data includes information about passengers on the Titanic. You will use predictors such as age, fare and where each passenger embarked from to predict who will survive. This data is from a tutorial on data science competitions (https://www.kaggle.com/c/titanic). Look here for descriptions of the features.
#
#The data is pre-loaded in a pandas DataFrame called df.
#
#It's smart to review the maximum and minimum values of each variable to ensure the data isn't misformatted or corrupted. What was the maximum age of passengers on the Titanic? Use the .describe() method in the IPython Shell to answer this question.

df['age'].describe()
Out[4]: 
count    891.000000
mean      29.699118
std       13.002015
min        0.420000
25%       22.000000
50%       29.699118
75%       35.000000
max       80.000000
Name: age, dtype: float64

#Exactly! The maximum age in the data is 80.