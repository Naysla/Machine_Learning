#Mean absolute error
#Cost functions and objective functions output a single value that summarizes how well two images match.
#
#The mean absolute error (MAE), for example, summarizes intensity differences between two images, with higher values indicating greater divergence.
#
#For this exercise, calculate the mean absolute error between im1 and im2 step-by-step.

#Calculate the difference between im1 and im2.
#Plot err with the seismic colormap. To center the colormap at 0, set vmin=-200 and vmax=200.

# Calculate image difference
err = im1-im2

# Plot the difference
plt.imshow(err,cmap='seismic',vmin=-200,vmax=200)
format_and_render_plot()

#Compute the absolute error of the difference. Use np.abs(). Plot the image.

# Calculate absolute image difference
abs_err = np.abs(im1 - im2)

# Plot the difference
plt.imshow(abs_err, cmap='seismic', vmin=-200, vmax=200)
format_and_render_plot()

#Find the cost value using np.mean().

# Calculate mean absolute error
mean_abs_err = np.mean(np.abs(im1 - im2))
print('MAE:', mean_abs_err)

#MAE: 9.2608642578125

#Well done! The MAE metric allows for variations in weighting throughout the image, which gives areas with high pixel intensities more influence on the cost calculation than others