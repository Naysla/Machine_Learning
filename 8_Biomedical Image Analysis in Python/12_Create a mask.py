#Create a mask
#Masks are the primary method for removing or selecting specific parts of an image. They are binary arrays that indicate whether a value should be included in an analysis. Typically, masks are created by applying one or more logical operations to an image.
#
#For this exercise, try to use a simple intensity threshold to differentiate between skin and bone in the hand radiograph. (im has been equalized to utilize the whole intensity range.)
#
#Below is the histogram of im colored by the segments we will plot.

# Create skin and bone masks
mask_bone = im >= 145
mask_skin =(im >= 45)& (im < 145)

# Plot the skin (0) and bone (1) masks
fig, axes = plt.subplots(1,2)
axes[0].imshow( mask_skin , cmap='gray')
axes[1].imshow( mask_bone , cmap='gray')
format_and_render_plot()

#Well done! You can chain logic together to make some quite complex masks.