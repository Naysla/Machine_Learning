#Translations
#In this chapter, we'll leverage data use data from the Open Access Series of Imaging Studies to compare the brains of different populations: young and old, male and female, healthy and diseased.
#
#To start, center a single slice of a 3D brain volume (im). First, find the center point in the image array and the center of mass of the brain. Then, translate the image to the center.
#
#This chapter's exercises have all had the following imports:

#import imageio
#import numpy as np
#import scipy.ndimage as ndi
#import matplotlib.pyplot as plt

# Find image center of mass
com = ndi.center_of_mass(im)

# Calculate amount of shift needed
d0 = 128 - com[0]
d1 = 128 - com[1]

# Translate the brain towards the center
xfm = ndi.shift(im, shift=[d0, d1])

# Plot the original and adjusted images
fig, axes = plt.subplots(2,1)
axes[0].imshow(im)
axes[1].imshow(xfm)
format_and_render_plot()

#Good job! You can shift your image in as many directions as there are image dimensions.

