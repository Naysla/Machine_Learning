#Histograms
#
#In this exercise, you will analyze the amount of red in the image. To do this, the histogram of the red channel will be computed for the image shown below:
#
#Image loaded as image.
#Extracting information from images is a fundamental part of image enhancement. This way you can balance the red and blue to make the image look colder or warmer.
#
#You will use hist() to display the 256 different intensities of the red color. And ravel() to make these color values an array of one flat dimension.
#
#Matplotlib is preloaded as plt and Numpy as np.


# Obtain the red channel
red_channel = image[:, :, 0]

# Plot the red histogram with bins in a range of 256
plt.hist(red_channel.ravel(), bins=256)

# Set title and show
plt.title('Red Histogram')
plt.show()

#Good! With this histogram we see that the image is quite reddish, meaning it has a sensation of warmness. This is because it has a wide and large distribution of bright red pixels, from 0 to around 150.