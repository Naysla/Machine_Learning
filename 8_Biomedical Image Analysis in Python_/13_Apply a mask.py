#Apply a mask
#Although masks are binary, they can be applied to images to filter out pixels where the mask is False.
#
#NumPy's where() function is a flexible way of applying masks. It takes three arguments:
#
#np.where(condition, x, y)
#condition, x and y can be either arrays or single values. This allows you to pass through original image values while setting masked values to 0.
#
#Let's practice applying masks by selecting the bone-like pixels from the hand x-ray (im).

# Import SciPy's "ndimage" module
import scipy.ndimage as ndi 

# Screen out non-bone pixels from "im"
mask_bone = im >= 145
im_bone = np.where(mask_bone, im, 0)

# Get the histogram of bone intensities
hist = ndi.histogram(im_bone,min=1,max=255,bins=255)

# Plot masked image and histogram
fig, axes = plt.subplots(2,1)
axes[0].imshow(im_bone)
axes[1].plot(hist)
format_and_render_plot()

#Nice! Sometimes simpler methods for applying a mask such as multiplication (e.g., im * mask_bone) will meet your needs, but np.where() is an excellent tool to have in your arsenal.