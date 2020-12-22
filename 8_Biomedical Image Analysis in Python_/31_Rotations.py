#Rotations
#In cases where an object is angled or flipped, the image can be rotated. Using ndi.rotate(), the image is rotated from its center by the specified degrees from the right horizontal axis.

#For this exercise, shift and rotate the brain image (im) so that it is roughly level and "facing" the right side of the image.

# Shift the image towards the center
xfm = ndi.shift(im, shift=(-20, -20))

# Rotate the shifted image
xfm = ndi.rotate(xfm, angle=-30, reshape=False)

# Plot the original and transformed images
fig, axes = plt.subplots(2, 1)
axes[0].imshow(im)
axes[1].imshow(xfm)
format_and_render_plot()

#The order of transformations makes a difference: rotating the image first will alter the object center, changing the amount of shift needed.

