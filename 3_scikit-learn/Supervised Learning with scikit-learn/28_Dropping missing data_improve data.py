#Dropping missing data
#The voting dataset from Chapter 1 contained a bunch of missing values that we dealt with for you behind the scenes. Now, it's time for you to take care of these yourself!
#
#The unprocessed dataset has been loaded into a DataFrame df. Explore it in the IPython Shell with the .head() method. You will see that there are certain data points labeled with a '?'. These denote missing values. As you saw in the video, different datasets encode missing values in different ways. Sometimes it may be a '9999', other times a 0 - real-world data can be very messy! If you're lucky, the missing values will already be encoded as NaN. We use NaN because it is an efficient and simplified way of internally representing missing data, and it lets us take advantage of pandas methods such as .dropna() and .fillna(), as well as scikit-learn's Imputation transformer Imputer().
#
#In this exercise, your job is to convert the '?'s to NaNs, and then drop the rows that contain them from the DataFrame.


#los datos actuales print(df.head()) demuestran que hay valores 0 que deben ser tratados ya sea borrando las filas que contegan estos valores o reemplazandolos por la media 
#estos valores pueden iniciar reemplazandose por NaN para luego usar los metodos .dropna() y .fillna() de pandas ó Imputer() de scikit-learn

 party infants water budget physician salvador religious satellite aid  \		  missile immigration synfuels education superfund crime duty_free_exports  \	  eaa_rsa  
0  republican       0     1      0         1        1         1         0   0   	0       0           1        ?         1         1     1                 0 		0       1
1  republican       0     1      0         1        1         1         0   0   	1       0           0        0         1         1     1                 0		1       ?  
2    democrat       ?     1      1         ?        1         1         0   0   	2       0           0        1         0         1     1                 0		2       0 
3    democrat       0     1      1         0        ?         1         0   0  		3       0           0        1         0         1     0                 0 		3       1 
4    democrat       1     1      1         0        1         1         0   0   	4       0           0        1         ?         1     1                 1		4       1 


# Convert '?' to NaN
df[df == '?'] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

#party                0
#infants              0
#water                0
#budget               0
#physician            0
#salvador             0
#religious            0
#satellite            0
#aid                  0
#missile              0
#immigration          0
#synfuels             0
#education            0
#superfund            0
#crime                0
#duty_free_exports    0
#eaa_rsa              0
#dtype: int64
#Shape of Original DataFrame: (435, 17)

# Drop missing values and print shape of new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))



#Great work! When many values in your dataset are missing, if you drop them, you may end up throwing away valuable information along with the missing data. It's better instead to develop an imputation strategy. This is where domain knowledge is useful, but in the absence of it, you can impute missing values with the mean or the median of the row or column that the missing value is in.
