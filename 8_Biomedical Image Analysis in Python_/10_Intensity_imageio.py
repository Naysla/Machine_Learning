#Intensity
#In this chapter, we will work with a hand radiograph from a 2017 Radiological Society of North America competition. X-ray absorption is highest in dense tissue such as bone, so the resulting intensities should be high. Consequently, images like this can be used to predict "bone age" in children.
#
#To start, let's load the image and check its intensity range.
#
#The image datatype determines the range of possible intensities: e.g., 8-bit unsigned integers (uint8) can take values in the range of 0 to 255. A colorbar can be helpful for connecting these values to the visualized image.
#
#All exercises in this chapter have the following imports:

#import imageio
#import numpy as np
#import matplotlib.pyplot as plt

# Load the hand radiograph
im = imageio.imread('hand-xray.jpg')
print('Data type:', im.dtype)
print('Min. value:', im.min())
print('Max value:', im.max())

# Plot the grayscale image
plt.imshow(im,cmap='gray',vmin=0, vmax=255)
plt.colorbar()
format_and_render_plot()

#Data type: uint8
#Min. value: 1
#Max value: 230

#Good work! Although only a coarse descriptor, the range of intensities can help you get a quick feel for your image's content.