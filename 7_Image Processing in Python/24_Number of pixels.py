#Number of pixels
#Let's calculate the total number of pixels in this image.
#	Image preloaded as face_image
#The total amount of pixel is its resolution. Given by Height×Width.
#
#Use .shape from NumPy which is preloaded as np, in the console to check the width and height of the image.

In [2]: np.shape(face_image)
Out[2]: (265, 191, 3)

In [3]: 265*191
Out[3]: 50615

#Yes! The image is 50,615 pixels in total.