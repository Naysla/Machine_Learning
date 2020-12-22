#Detect edges (2)
#Edge detection can be performed along multiple axes, then combined into a single edge value. For 2D images, the horizontal and vertical "edge maps" can be combined using the Pythagorean theorem:
#
#Detect_edges_2.jpg
#
#One popular edge detector is the Sobel filter. The Sobel filter provides extra weight to the center pixels of the detector:
#
#	weights = [[ 1,  2,  1], 
#			   [ 0,  0,  0],
#			   [-1, -2, -1]]
#			   
#
#For this exercise, improve upon your previous detection effort by merging the results of two Sobel-filtered images into a composite edge map.

# Apply Sobel filter along both axes
sobel_ax0 = ndi.sobel(im, axis=0)
sobel_ax1 = ndi.sobel(im, axis=1)

# Calculate edge magnitude 
edges = np.sqrt(np.square(sobel_ax0) + np.square(sobel_ax1))

# Plot edge magnitude
plt.imshow(edges, cmap='gray', vmax=75)
format_and_render_plot()

#Congratulations! In this chapter, you learned how to modify and extract parts of images based on their location and intensity. You are now ready to begin analyzing individual images!