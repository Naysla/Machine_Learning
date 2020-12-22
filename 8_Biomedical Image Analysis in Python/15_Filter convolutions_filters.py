#Filter convolutions
#Filters are an essential tool in image processing. They allow you to transform images based on intensity values surrounding a pixel, rather than globally.
#  Ch2_L3_ConvolutionGif.gif
#For this exercise, smooth the foot radiograph. First, specify the weights to be used. (These are called "footprints" and "kernels" as well.) Then, convolve the filter with im and plot the result.

# Set filter weights
weights = [[0.11, 0.11, 0.11],
           [0.11, 0.11, 0.11], 
           [0.11, 0.11, 0.11]]

# Convolve the image with the filter
im_filt = ndi.convolve(im, weights)

# Plot the images
fig, axes = plt.subplots(1,2)
axes[0].imshow(im)
axes[1].imshow(im_filt)
format_and_render_plot()

#Great. The size and pattern of the filter weights control the effect it will have on your image.