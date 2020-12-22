#Edge detection
#In this exercise, you'll detect edges in an image by applying the Sobel filter.
#Image preloaded as soaps_image.
#Theshow_image() function has been already loaded for you.
#
#Let's see if it spots all the figures in the image.


# Import the color module
from skimage import color

# Import the filters module and sobel function
from skimage.filters import sobel

# Make the image grayscale
soaps_image_gray = color.rgb2gray(soaps_image)

# Apply edge detection filter
edge_sobel = sobel(soaps_image_gray)

# Show original and resulting image to compare
show_image(soaps_image, "Original")
show_image(edge_sobel, "Edges with Sobel")

#answer
#delinea todas las formas con color blanco y el fondo de la imagen queda negro

#Great job! You succesfully detected the edges in the image.
#As you can see, the edges of all the figures in the scene are highlighted.
