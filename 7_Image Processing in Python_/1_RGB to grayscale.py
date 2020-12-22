#RGB to grayscale
#
#In this exercise you will load an image from scikit-image module data and make it grayscale, then compare both of them in the output.
#
#We have preloaded a function show_image(image, title='Image') that displays the image using Matplotlib. You can check more about its parameters using ?show_image() or help(show_image) in the console.

# Import the modules from skimage
from skimage import data, color

# Load the rocket image
rocket = data.rocket()

# Convert the image to grayscale
gray_scaled_rocket = color.rgb2gray(rocket)

# Show the original image
show_image(rocket, 'Original RGB image')

# Show the grayscale image
show_image(gray_scaled_rocket, 'Grayscale image')

#Answer
#devuelve la imagen en escala blanco y negro

#Great! You converted an image to grayscale. For many applications of image processing, color information doesn't help us identify important edges or other features. Something that we will cover later in the course.