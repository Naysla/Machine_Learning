#Creating dummy variables
#As Andy discussed in the video, scikit-learn does not accept non-numerical features. You saw in the previous exercise that the 'Region' feature contains very useful information that can predict life expectancy. For example, Sub-Saharan Africa has a lower life expectancy compared to Europe and Central Asia. Therefore, if you are trying to predict life expectancy, it would be preferable to retain the 'Region' feature. To do this, you need to binarize it by creating dummy variables, which is what you will do in this exercise.

# Import pandas
import pandas as pd

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create dummy variables: df_region
df_region =pd.get_dummies(df)

# Print the columns of df_region
#print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df,drop_first=True)

# Print the new columns of df_region
print(df_region.columns)


#Answer

#print(df_region.columns)
#Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
#       'BMI_female', 'life', 'child_mortality', 'Region_America',
#       'Region_East Asia & Pacific', 'Region_Europe & Central Asia',
#       'Region_Middle East & North Africa', 'Region_South Asia',
#       'Region_Sub-Saharan Africa'],
#      dtype='object')

#print(df_region.columns)	  
#Index(['population', 'fertility', 'HIV', 'CO2', 'BMI_male', 'GDP',
#       'BMI_female', 'life', 'child_mortality', 'Region_East Asia & Pacific',
#       'Region_Europe & Central Asia', 'Region_Middle East & North Africa',
#       'Region_South Asia', 'Region_Sub-Saharan Africa'],
#      dtype='object')


#Excellent! Now that you have created the dummy variables, you can use the 'Region' feature to predict life expectancy!