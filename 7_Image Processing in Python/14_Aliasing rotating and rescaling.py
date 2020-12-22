#Aliasing, rotating and rescaling
#Let's look at the impact of aliasing on images.
#
#Remember that aliasing is an effect that causes different signals, in this case pixels, to become indistinguishable or distorted.
#
#You'll make this cat image upright by rotating it 90 degrees and then rescaling it two times. Once with the anti aliasing filter applied before rescaling and a second time without it, so you can compare them.
#
#Image preloaded as image_cat.

# Import the module and the rotate and rescale functions
from skimage.transform import rotate, rescale

# Rotate the image 90 degrees clockwise 
rotated_cat_image = rotate(image_cat, -90)

# Rescale with anti aliasing
rescaled_with_aa = rescale(rotated_cat_image, 1/4, anti_aliasing=True, multichannel=True)

# Rescale without anti aliasing
rescaled_without_aa = rescale(rotated_cat_image, 1/4, anti_aliasing=False, multichannel=True)

# Show the resulting images
show_image(rescaled_with_aa, "Transformed with anti aliasing")
show_image(rescaled_without_aa, "Transformed without anti aliasing")

#Great job! You rotated and rescaled the image.
#Seems like the anti aliasing filter prevents the poor pixelation effect to happen, making it look better but also less sharp.