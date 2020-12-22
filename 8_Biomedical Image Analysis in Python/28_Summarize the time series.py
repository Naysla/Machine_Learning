#Summarize the time series

#The ejection fraction is the proportion of blood squeezed out of the left ventricle each heartbeat. To calculate it, radiologists have to identify the maximum volume (systolic volume) and the minimum volume (diastolic volume) of the ventricle.

#For this exercise, create a time series of volume calculations. There are 20 time points in both vol_ts and labels. The data is ordered by (time, plane, row, col).

# Create an empty time series
ts = np.zeros(20)

# Calculate volume at each voxel
d0, d1, d2, d3 = vol_ts.meta['sampling']
dvoxel = d1 * d2 * d3

# Loop over the labeled arrays
for t in range(20):
    nvoxels = ndi.sum(1,labels[t],index=1)
    ts[t] =  nvoxels * dvoxel

# Plot the data
plt.plot(ts)
format_and_render_plot()

#Great work! You can see the pumping action of the left ventricle clearly from the time series plot - a sudden decrease followed by a refilling of the chamber.