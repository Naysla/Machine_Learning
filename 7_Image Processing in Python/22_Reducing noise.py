#Reducing noise
#We have a noisy image that we want to improve by removing the noise in it.
#	Preloaded as noisy_image.
#Use total variation filter denoising to accomplish this.

# Import the module and function
from skimage.restoration import denoise_tv_chambolle

# Apply total variation filter denoising
denoised_image = denoise_tv_chambolle(noisy_image, 
                                      multichannel=True)

# Show the noisy and denoised images
show_image(noisy_image, 'Noisy')
show_image(denoised_image, 'Denoised image')

#Awesome! You fixed the image by applying the TV denoising function with the parameter default values. Feel free to read more about them in the scikit-image documentation.