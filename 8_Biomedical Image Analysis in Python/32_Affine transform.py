#Affine transform
#An affine transformation matrix provides directions for up to four types of changes: translating, rotating, rescaling and shearing. The elements of the matrix map the coordinates from the input array to the output.
	#	Affine_transform.png
#For this exercise, use ndi.affine_transform() to apply the following registration matrices to im. Which one does the best job of centering, leveling and enlarging the original image?

#ndi.affine_transform(im ,[[0.8, -0.4, 90], [0.4, 0.8, -6.0], [0, 0, 1]] )

#[[0.8, -0.4, 90], [0.4, 0.8, -6.0], [0, 0, 1]]

#Fantastic. To implement matrix transformations in your workflow, you will likely want to use more advanced tools, such as those in scikit-image. The package's website has some nice tutorials. Also, note that 3D images require different size transformation matrices.

