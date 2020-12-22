#Smoothing
#
#Smoothing can improve the signal-to-noise ratio of your image by blurring out small variations in intensity. The Gaussian filter is excellent for this: it is a circular (or spherical) smoothing kernel that weights nearby pixels higher than distant ones.
#
#The width of the distribution is controlled by the sigma argument, with higher values leading to larger smoothing effects.
#
#For this exercise, test the effects of applying Gaussian filters to the foot x-ray before creating a bone mask.

# Smooth "im" with Gaussian filters
im_s1 = ndi.gaussian_filter(im, sigma=1)
im_s3 = ndi.gaussian_filter(im, sigma=3)

# Draw bone masks of each image
fig, axes = plt.subplots(1,3)
axes[0].imshow(im >= 145)
axes[1].imshow(im_s1 >= 145)
axes[2].imshow(im_s3 >= 145)
format_and_render_plot()

#Great work! Many analyses can benefit from an initial smoothing of the data.