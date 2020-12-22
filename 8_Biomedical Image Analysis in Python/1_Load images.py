#Load images
#In this chapter, we'll work with sections of a computed tomography (CT) scan from The Cancer Imaging Archive. CT uses a rotating X-ray tube to create a 3D image of the target area.
#
#The actual content of the image depends on the instrument used: photographs measure visible light, x-ray and CT measure radiation absorbance, and MRI scanners measure magnetic fields.
#
#To warm up, use the imageio package to load a single DICOM image from the scan volume and check out a few of its attributes.

# Import ImageIO
import imageio

# Load "chest-220.dcm"
im = imageio.imread('chest-220.dcm')

# Print image attributes
print('Image type:', type(im))
print('Shape of image array:', im.shape)

#

#Image type: <class 'imageio.core.util.Array'>
#Shape of image array: (512, 512)

#mageio is a versatile package. It can read in a variety of image data, including JPEG, PNG, and TIFF. But it's especially useful for its ability to handle DICOM files