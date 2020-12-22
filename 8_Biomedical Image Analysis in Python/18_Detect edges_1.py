#Detect edges (1)
#Filters can also be used as "detectors." If a part of the image fits the weighting pattern, the returned value will be very high (or very low).
#
#In the case of edge detection, that pattern is a change in intensity along a plane. A filter detecting horizontal edges might look like this:
#
#		weights = [[+1, +1, +1],
#           [ 0,  0,  0],
#           [-1, -1, -1]]
#		   
#For this exercise, create a vertical edge detector and see how well it performs on the hand x-ray (im).

# Set weights to detect vertical edges
weights = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]

# Convolve "im" with filter weights
edges =  ndi.convolve(im, weights)

# Draw the image in color
plt.imshow(edges, cmap='seismic', vmin=-150, vmax=150)
plt.colorbar()
format_and_render_plot()

#Pretty cool, right? Take a close look at where the edges are - and are not - highlighted to reinforce your understanding of how this detector works.