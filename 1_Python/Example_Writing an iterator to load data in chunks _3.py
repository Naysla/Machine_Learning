#you've only processed the data from the first DataFrame chunk. 
# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population' --> nueva columna
df_pop_ceb['Total Urban Population'] = [int(item[0]*item[1]*0.01) for item in pops_list]
#print(df_pop_ceb['Total Urban Population'])
# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()



#print(df_pop_ceb['Total Urban Population'])
2      40680944
244    41697325
486    42662734
728    43670267
970    44717348
Name: Total Urban Population, dtype: int64