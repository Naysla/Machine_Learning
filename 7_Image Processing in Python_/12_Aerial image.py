#Aerial image
#In this exercise, we will improve the quality of an aerial image of a city. The image has low contrast and therefore we can not distinguish all the elements in it.
#	Image loaded as image_aerial.
#For this we will use the normal or standard technique of Histogram Equalization.

# Import the required module
from skimage import exposure

# Use histogram equalization to improve the contrast
image_eq =  exposure.equalize_adapthist(image_aerial,clip_limit=0.03 )

# Show the original and resulting image
show_image(image_aerial, 'Original')
show_image(image_eq, 'Resulting image')

#Mejora el color, contraste y lineas de la imagen para distinguir mejor los elementos que la componen

#Awesome work! Now we can see more details of the objects in the image.