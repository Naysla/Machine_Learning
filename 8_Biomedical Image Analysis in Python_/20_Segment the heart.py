#Segment the heart
#In this chapter, we'll work with magnetic resonance (MR) imaging data from the Sunnybrook Cardiac Dataset (http://www.cardiacatlas.org/studies/sunnybrook-cardiac-data/). The full image is a 3D time series spanning a single heartbeat. These data are used by radiologists to measure the ejection fraction: the proportion of blood ejected from the left ventricle during each stroke.
#
#To begin, segment the left ventricle from a single slice of the volume (im). First, you'll filter and mask the image; then you'll label each object with ndi.label().
#
#This chapter's exercises have the following imports:
#
#		import imageio
#		import numpy as np
#		import scipy.ndimage as ndi
#		import matplotlib.pyplot as plt
		

		
# Smooth intensity values
im_filt = ndi.median_filter(im, size=3)

# Select high-intensity pixels
mask_start = np.where(im_filt>60, 1, 0)
mask = ndi.binary_closing(mask_start)

# Label the objects in "mask"
labels, nlabels = ndi.label(mask)
print('Num. Labels:', nlabels)

# Create a `labels` overlay
overlay = np.where(labels >0, labels , np.nan)

# Use imshow to plot the overlay
plt.imshow(overlay, cmap='rainbow', alpha=0.75)
format_and_render_plot()

#Robust image segmentation is an entire research domain, but the simple principle is to leverage intensity and location information to differentiate objects of interest from the background. Once labeled, the objects can be manipulated easily.