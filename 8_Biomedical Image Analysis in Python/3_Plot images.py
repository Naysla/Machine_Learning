#Plot images
#Perhaps the most critical principle of image analysis is: look at your images!
#
#Matplotlib's imshow() function gives you a simple way to do this. Knowing a few simple arguments will help:
#
#cmap controls the color mappings for each value. The "gray" colormap is common, but many others are available.
#vmin and vmax control the color contrast between values. Changing these can reduce the influence of extreme values.
#plt.axis('off') removes axis and tick labels from the image.
#For this exercise, plot the CT scan and investigate the effect of a few different parameters.

# Import ImageIO and PyPlot 
import imageio
import matplotlib.pyplot as plt

# Read in "chest-220.dcm"
im = imageio.imread('chest-220.dcm')

# Draw the image in grayscale
plt.imshow(im, cmap='gray')

# Render the image
plt.show()

# Draw the image with greater contrast
plt.imshow(im, cmap='gray', vmin=-200, vmax=200)

# Render the image
plt.show()

# Remove axis ticks and labels
plt.axis('off')

# Render the image
plt.show()

#Nice work! Manipulating cmap, vmin, and vmax will give you the flexibility to plot all types of data. Remember, though, that they only affect the plot and not the underlying data.