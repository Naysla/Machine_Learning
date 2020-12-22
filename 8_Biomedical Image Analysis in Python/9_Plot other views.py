#Plot other views
#Any two dimensions of an array can form an image, and slicing along different axes can provide a useful perspective. However, unequal sampling rates can create distorted images.
#
#
#
#Changing the aspect ratio can address this by increasing the width of one of the dimensions.
#
#For this exercise, plot images that slice along the second and third dimensions of vol. Explicitly set the aspect ratio to generate undistorted images.

# Select frame from "vol"
im1 = vol[:, 256, :]
im2 = vol[:, :, 256]

# Compute aspect ratios
d0, d1, d2 = vol.meta['sampling']
asp1 = d0 / d2
asp2 = d0 / d1

# Plot the images on a subplots array 
fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].imshow(im1, cmap='gray',aspect=asp1)
axes[1].imshow(im2, cmap='gray',aspect=asp2)
plt.show()

#Great work in this chapter! Next, we'll begin to manipulate images and extract salient features from them.