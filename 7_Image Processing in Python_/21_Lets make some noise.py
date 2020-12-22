#Let's make some noise!
#In this exercise, we'll practice adding noise to a fruit image.
#
#Image preloaded as fruit_image

# Import the module and function
from skimage.util import random_noise

# Add noise to the image
noisy_image = random_noise(fruit_image)

# Show original and resulting image
show_image(fruit_image, 'Original')
show_image(noisy_image, 'Noisy image')

#Yes! Now you can add noise to any image you work with.
#You can always read more about the functions in the scikit-image documentation.
