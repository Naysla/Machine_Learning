#Removing logos
#As we saw in the video, another use of image restoration is removing objects from an scene. In this exercise, we'll remove the Datacamp logo from an image.
#
#	Image loaded as image_with_logo.
#You will create and set the mask to be able to erase the logo by inpainting this area.
#
#Remember that when you want to remove an object from an image you can either manually delineate that object or run some image analysis algorithm to find it.

# Initialize the mask
mask = np.zeros(image_with_logo.shape[:-1])

# Set the pixels where the logo is to 1
mask[210:272, 360:425] = 1

# Apply inpainting to remove the logo
image_logo_removed = inpaint.inpaint_biharmonic(image_with_logo,
                                  mask,
                                  multichannel=True)

# Show the original and logo removed images
show_image(image_with_logo, 'Image with logo')
show_image(image_logo_removed, 'Image with logo removed')

#Answer
# remueve de la imagen original ellogo de datacamp

#Excellent! Now you know how you can remove objects or logos from images. Be wise in how you use your new acquired knowledge, magician.