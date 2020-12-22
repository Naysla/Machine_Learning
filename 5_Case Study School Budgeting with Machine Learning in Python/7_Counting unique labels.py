#Counting unique labels
#As Peter mentioned in the video, there are over 100 unique labels. In this exercise, you will explore this fact by counting and plotting the number of unique values for each category of label.
#
#The dataframe df and the LABELS list have been loaded into the workspace; the LABELS columns of df have been converted to category types.
#
#pandas, which has been pre-imported as pd, provides a pd.Series.nunique method for counting the number of unique values in a Series.

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Calculate number of unique values for each label: num_unique_labels
num_unique_labels = df[LABELS].apply(pd.Series.nunique)

# Plot number of unique values for each label
num_unique_labels.plot(kind='bar')

# Label the axes
plt.xlabel('Labels')
plt.ylabel('Number of unique values')

# Display the plot
plt.show()

#Answer

#It returns a graphic with the number of uniqe 9 columns 

#Woah! That's a lot of labels to work with. How will you measure success with these many labels? You'll find out in the next video!