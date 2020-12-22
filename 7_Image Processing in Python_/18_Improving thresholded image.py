#Improving thresholded image
#In this exercise, we'll try to reduce the noise of a thresholded image using the dilation morphological operation.
#
#Image already loaded as world_image.
#This operation, in a way, expands the objects in the image.

# Import the module
from skimage import morphology

# Obtain the dilated image 
dilated_image = morphology.binary_dilation(world_image)

# See results
show_image(world_image, 'Original')
show_image(dilated_image, 'Dilated image')

#Great! You removed the noise of the segmented image and now it's more uniform.