#Reducing noise while preserving edges
#In this exercise, you will reduce the noise in this landscape picture.
#
#	Preloaded as landscape_image.
#Since we prefer to preserve the edges in the image, we'll use the bilateral denoising filter.

# Import bilateral denoising function
from skimage.restoration import denoise_bilateral

# Apply bilateral filter denoising
denoised_image = denoise_bilateral(landscape_image, 
                                   multichannel=True)

# Show original and resulting images
show_image(landscape_image, 'Noisy image')
show_image(denoised_image, 'Denoised image')

#Great! You denoised the image without losing sharpness.
#In this case denoise_bilateral() worked well with the default optional parameters