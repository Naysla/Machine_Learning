#Blurring to reduce noise
#In this exercise you will reduce the sharpness of an image of a building taken during a London trip, through filtering.

#Image loaded as building_image

# Import Gaussian filter 
from skimage.filters import gaussian

# Apply filter
gaussian_image = gaussian(building_image,multichannel=True)

# Show original and resulting image to compare
show_image(building_image, "Original")
show_image(gaussian_image, "Reduced sharpness Gaussian")

#Awesome! You have removed the excessive sharpness in the image.