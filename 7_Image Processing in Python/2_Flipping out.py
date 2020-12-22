#Flipping out
#As a prank, someone has turned an image from a photo album of a trip to Seville upside-down and back-to-front! Now, we need to straighten the image, by flipping it.
#Image loaded as flipped_seville.
#Using the NumPy methods learned in the course, flip the image horizontally and vertically. Then display the corrected image using the show_image() function.
#NumPy is already imported as np.

# Flip the image vertically
seville_vertical_flip = np.flipud(flipped_seville)
show_image(seville_vertical_flip,'Vertically flipped image')

#Answer

#Muestra la imagen ajustada vertialmente, antes estaba mostrandose de cabeza


# Flip the previous image horizontally
seville_horizontal_flip = np.fliplr(seville_vertical_flip)

show_image(seville_horizontal_flip,'Horizontally flipped image')

#Answer

#Muestra la imagen acomodada horizontalmente


# Show the resulting image
show_image(seville_horizontal_flip, 'Seville')
