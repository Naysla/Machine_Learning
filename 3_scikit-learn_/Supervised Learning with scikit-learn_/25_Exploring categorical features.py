#Exploring categorical features
#The Gapminder dataset that you worked with in previous chapters also contained a categorical 'Region' feature, which we dropped in previous exercises since you did not have the tools to deal with it. Now however, you do, so we have added it back in!
#
#Your job in this exercise is to explore this feature. Boxplots are particularly useful for visualizing categorical features such as this.


# Import pandas
import pandas as pd

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('gapminder.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'Region', rot=60)

# Show the plot
plt.show()


#Answer

#En la grafica se puede identificar que la expectativa de vida es mayor en la region "Europa & Asia central"
#�frica Subsahariana tiene una esperanza de vida m�s baja en comparaci�n con Europa y Asia Central.

#Great work! Exploratory data analysis should always be the precursor to model building.