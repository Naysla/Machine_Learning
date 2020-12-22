#Enlarging images
#Have you ever tried resizing an image to make it larger? This usually results in loss of quality, with the enlarged image looking blurry.
#
#The good news is that the algorithm used by scikit-image works very well for enlarging images up to a certain point.
#
#In this exercise you'll enlarge an image three times!!
#
#You'll do this by rescaling the image of a rocket, that will be loaded from the data module.

# Import the module and function to enlarge images
from skimage.transform import rescale

# Import the data module
from skimage import data

# Load the image from data
rocket_image = data.rocket()

# Enlarge the image so it is 3 times bigger
enlarged_rocket_image = rescale(rocket_image, 1/3, anti_aliasing=True, multichannel=True)

# Show original and resulting image
show_image(rocket_image)
show_image(enlarged_rocket_image, "3 times enlarged image")

#Wow! The image went from being 600 pixels wide to over 2500 and it still does not look poorly pixelated. Nice work!