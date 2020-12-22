#Edges
#In this exercise you will identify the shapes in a grapefruit image by detecting the edges, using the Canny algorithm.
#Image preloaded as grapefruit.
#The color module has already been preloaded for you.

# Import the canny edge detector 
from skimage.feature import canny

# Convert image to grayscale
grapefruit = color.rgb2gray(grapefruit)

# Apply canny edge detector
canny_edges = canny(grapefruit)

# Show resulting image
show_image(canny_edges, "Edges with Canny")

#You can see the shapes and details of the grapefruits of the original image being highlighted.