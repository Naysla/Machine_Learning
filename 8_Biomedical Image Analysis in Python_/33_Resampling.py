#Resampling
#Images can be collected in a variety of shapes and sizes. Resampling is a useful tool when these shapes need to be made consistent. Two common applications are:
#
#Downsampling: combining pixel data to decrease size
#Upsampling: distributing pixel data to increase size
#For this exercise, transform and then resample the brain image (im) to see how it affects image shape.

# Center and level image
xfm = ndi.shift(im, shift=(-20, -20))
xfm = ndi.rotate(xfm, angle=-35, reshape=False)

# Resample image
#se ndi.zoom() to downsample the image from (256, 256) to (64, 64).
im_dn = ndi.zoom(xfm, zoom= (64/256))
#Use ndi.zoom() to upsample the image from (256, 256) to (1024, 1024).
im_up = ndi.zoom(xfm, zoom= (1024/256))

# Plot the images
fig, axes = plt.subplots(2, 1)
axes[0].imshow(im_dn)
axes[1].imshow(im_up)
format_and_render_plot()

#You can also resample data along a single dimension by passing a tuple: e.g. ndi.zoom(im, zoom=(2,1,1)). This can be useful for making voxels cubic.