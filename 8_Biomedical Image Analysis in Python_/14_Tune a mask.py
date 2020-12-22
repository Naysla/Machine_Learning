#Tune a mask
#
#Imperfect masks can be tuned through the addition and subtraction of pixels. SciPy includes several useful methods for accomplishing these ends. These include:
#
#binary_dilation: Add pixels along edges
#binary_erosion: Remove pixels along edges
#binary_opening: Erode then dilate, "opening" areas near edges
#binary_closing: Dilate then erode, "filling in" holes
#For this exercise, create a bone mask then tune it to include additional pixels.
#
#For the remaining exercises, we have run the following import for you:
#
#import scipy.ndimage as ndi

# Create and tune bone mask
mask_bone = im>=145
mask_dilate = ndi.binary_dilation(mask_bone, iterations=5)
mask_closed = ndi.binary_closing(mask_bone,iterations=5)

# Plot masked images
fig, axes = plt.subplots(1,3)
axes[0].imshow(mask_bone)
axes[1].imshow(mask_dilate)
axes[2].imshow(mask_closed)
format_and_render_plot()

#Very nice! Dilation, erosion, and closing are useful techniques when you want to fine-tune your masks.