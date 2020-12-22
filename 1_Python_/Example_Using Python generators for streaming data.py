#Sequence
def num_sequence(n):
	"""Generate values from0 to n"""
	I=0
	while i<0:
		yield i
		i+=1
		

#In this exercise, you will process the first 1000 rows of a file line by line, to create a dictionary of the counts of how many times each country appears in a column in the dataset.

#world_dev_ind.csv --> imported default

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000) :

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)

#{'Arab World': 80, 
#'Caribbean small states': 77, 
#'Central Europe and the Baltics': 71, 
#'East Asia & Pacific (all income levels)': 122, 
#'East Asia & Pacific (developing only)': 123, 
#'Euro area': 119, 
#'Europe & Central Asia (all income levels)': 109, 
#'Europe & Central Asia (developing only)': 89, 
#'European Union': 116, 
#'Fragile and conflict affected situations': 76, 
#'Heavily indebted poor countries (HIPC)': 18}