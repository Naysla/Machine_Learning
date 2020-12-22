#Calculate distance
#A distance transformation calculates the distance from each pixel to a given point, usually the nearest background pixel. This allows you to determine which points in the object are more interior and which are closer to edges.
#
#For this exercise, use the Euclidian distance transform on the left ventricle object in labels.

# Calculate left ventricle distances
lv = np.where(labels==1, 1, 0)
dists = ndi.distance_transform_edt(lv,sampling=vol.meta['sampling'])

# Report on distances
print('Max distance (mm):', ndi.maximum(dists))
print('Max location:', ndi.maximum_position(dists))

# Plot overlay of distances
overlay = np.where(dists[5] > 0, dists[5], np.nan) 
plt.imshow(overlay, cmap='hot')
format_and_render_plot()

#Answer
#Max distance (mm): 16.320510697696196
#Max location: (5, 129, 137)

#Nicely done. You can make inferences about the shapes of objects by looking at the distribution of distances. For example, a circle will have a uniform distribution of distances along both dimensions.