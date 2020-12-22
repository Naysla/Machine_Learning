#Contouring shapes
#In this exercise we'll find the contour of a horse.
#
#For that we will make use of a binarized image provided by scikit-image in its data module. Binarized images are easier to process when finding contours with this algorithm. Remember that contour finding only supports 2D image arrays.
#
#Once the contour is detected, we will display it together with the original image. That way we can check if our analysis was correct!
#
#show_image_contour(image, contours) is a preloaded function that displays the image with all contours found using Matplotlib.
#
#Remember you can use the find_contours() function from the measure module, by passing the thresholded image and a constant value.

# Import the modules
from skimage import data, measure

# Obtain the horse image
horse_image = data.horse()

# Find the contours with a constant level value of 0.8
contours = measure.find_contours(horse_image, 0.8)

# Shows the image with contours found
show_image_contour(horse_image, contours)

#Awesome job! You were able to find the horse contours! In the next exercise you will do some image preparation first and binarize the image yourself before finding the contours.