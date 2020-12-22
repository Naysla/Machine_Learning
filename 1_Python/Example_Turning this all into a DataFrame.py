# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())


#	 CountryCode CountryName  ...               Value  Year
#	0         ARB  Arab World  ...  133.56090740552298  1960
#	1         ARB  Arab World  ...    87.7976011532547  1960
#	2         ARB  Arab World  ...   6.634579191565161  1960
#	3         ARB  Arab World  ...   81.02332950839141  1960
#	4         ARB  Arab World  ...           3000000.0  1960
#
#	[5 rows x 6 columns]