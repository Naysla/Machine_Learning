#Intersection of the union
#Another cost function is the intersection of the union (IOU). The IOU is the number of pixels filled in both images (the intersection) out of the number of pixels filled in either image (the union).
#
#For this exercise, determine how best to transform im1 to maximize the IOU cost function with im2. We have defined the following function for you:
#
#	def intersection_of_union(im1, im2):
#    i = np.logical_and(im1, im2)
#    u = np.logical_or(im1, im2)
#    return i.sum() / u.sum()
#	
#Note: When using ndi.rotate(), remember to pass reshape=False, so that array shapes match.

#Shift (-10, -10), rotar -15 grados

#Great job. Remember, the core principle is that a cost function must produce a single summary value across all elements in the image. MAE and IOU are just two of the many possible ways you might compare images.