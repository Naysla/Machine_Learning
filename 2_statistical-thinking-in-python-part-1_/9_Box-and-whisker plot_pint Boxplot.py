#Box-and-whisker plot
#Making a box plot for the petal lengths is unnecessary because the iris data set is not too large and the bee swarm plot works fine. However, it is always good to get some practice. Make a box plot of the iris petal lengths. You have a pandas DataFrame, df, which contains the petal length data, in your namespace. Inspect the data frame df in the IPython shell using df.head() to make sure you know what the pertinent columns are.
#
#For your reference, the code used to produce the box plot in the video is provided below:
#
#_ = sns.boxplot(x='east_west', y='dem_share', data=df_all_states)
#
#_ = plt.xlabel('region')
#
#_ = plt.ylabel('percent of vote for Obama')
#
#In the IPython Shell, you can use sns.boxplot? or help(sns.boxplot) for more details on how to make box plots using seaborn.
#
#rint(df.head())
#   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
#0                5.1               3.5                1.4               0.2  setosa
#1                4.9               3.0                1.4               0.2  setosa
#2                4.7               3.2                1.3               0.2  setosa
#3                4.6               3.1                1.5               0.2  setosa
#4                5.0               3.6                1.4               0.2  setosa


# Create box plot with Seaborn's default settings
#import pandas as pd
#import Seaborn as sns
#df is preloaded

_ = sns.boxplot(x= 'species',y='petal length (cm)', data=df)

# Label the axes
_= plt.xlabel('species')
_=plt.ylabel('petal length (cm)')

# Show the plot
plt.show()


#devuelve una grafica de 3 boxplot pues solo hay 3 especies de flores para analizar el tamaño de el petalo