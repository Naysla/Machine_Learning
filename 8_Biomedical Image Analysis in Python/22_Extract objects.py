#Extract objects
#Extracting objects from the original image eliminates unrelated pixels and provides new images that can be analyzed independently.
#
#The key is to crop images so that they only include the object of interest. The range of pixel indices that encompass the object is the bounding box.
#
#For this exercise, use ndi.find_objects() to create a new image containing only the left ventricle.

# Create left ventricle mask
labels, nlabels = ndi.label(mask)
lv_val = labels[128, 128]
lv_mask = np.where(labels = lv_val, 1, 0)

# Find bounding box of left ventricle
bboxes = ndi.find_objects(lv_mask)
print('Number of objects:', len(bboxes))
print('Indices for first box:', bboxes[0])


#Number of objects: 1
#Indices for first box: (slice(107, 149, None), slice(116, 162, None))

# Crop to the left ventricle (index 0)
im_lv = im[bboxes[0]]

# Plot the cropped image
plt.imshow(im_lv)
format_and_render_plot()

#Great work! ndi.find_objects() becomes extremely useful when dealing with 3-dimensional objects that are harder to view at a glance.