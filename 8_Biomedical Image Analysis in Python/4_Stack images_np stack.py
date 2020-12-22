#Stack images
#Image "stacks" are a useful metaphor for understanding multi-dimensional data. Each higher dimension is a stack of lower dimensional arrays.
#
#https://scikit-image.org/docs/dev/user_guide/numpy_images.html#numpy-images-coordinate-conventions
#
#In this exercise, we will use NumPy's stack() function to combine several 2D arrays into a 3D volume. By convention, volumetric data should be stacked along the first dimension: vol[plane, row, col].
#
#Note: performing any operations on an ImageIO Image object will convert it to a numpy.ndarray, stripping its metadata.

# Import ImageIO and NumPy
import imageio
import numpy as np

# Read in each 2D image
im1 = imageio.imread('chest-220.dcm')
im2 = imageio.imread('chest-221.dcm')
im3 = imageio.imread('chest-222.dcm')

# Stack images into a volume
vol = np.stack([im1, im2, im3])
print('Volume dimensions:', vol.shape)

#Answer

#Volume dimensions: (3, 512, 512)

#Great work! For large volumes, you can use a for loop to quickly generate your image list.
