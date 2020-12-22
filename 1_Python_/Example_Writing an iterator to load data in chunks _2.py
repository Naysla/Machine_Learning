#In the previous exercise, you used read_csv() to read in DataFrame chunks from a large dataset. In this exercise, you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.
#
#To process the data, you will create another DataFrame composed of only the rows from a specific country. You will then zip together two of the columns from the new DataFrame, 'Total Population' and 'Urban population (% of total)'. Finally, you will create a list of tuples from the zip object, where each tuple is composed of a value from each of the two columns mentioned.
#
#You're going to use the data from 'ind_pop_data.csv', available in your current directory. Pandas has been imported as pd.

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame 
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode']=='CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])
#<zip object at 0x7f9ddd337408>
# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)


#sprint(df_urb_pop.head())

                               CountryName CountryCode  Year  Total Population  Urban population (% of total)
0                               Arab World         ARB  1960      9.249590e+07                      31.285384
1                   Caribbean small states         CSS  1960      4.190810e+06                      31.597490
2           Central Europe and the Baltics         CEB  1960      9.140158e+07                      44.507921
3  East Asia & Pacific (all income levels)         EAS  1960      1.042475e+09                      22.471132
4    East Asia & Pacific (developing only)         EAP  1960      8.964930e+08                      16.917679

print(df_pop_ceb)

                        CountryName CountryCode  Year  Total Population  Urban population (% of total)
2    Central Europe and the Baltics         CEB  1960        91401583.0                      44.507921
244  Central Europe and the Baltics         CEB  1961        92237118.0                      45.206665
486  Central Europe and the Baltics         CEB  1962        93014890.0                      45.866565
728  Central Europe and the Baltics         CEB  1963        93845749.0                      46.534093
970  Central Europe and the Baltics         CEB  1964        94722599.0                      47.208743

print(pops_list)

[(91401583.0, 44.5079211390026), (92237118.0, 45.206665319194), (93014890.0, 45.866564696018), (93845749.0, 46.5340927663649), (94722599.0, 47.2087429803526)]
