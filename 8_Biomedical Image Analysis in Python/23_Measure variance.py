#Measure variance
#SciPy measurement functions allow you to tailor measurements to specific sets of pixels:
#
#Specifying labels restricts the mask to non-zero pixels.
#Specifying index value(s) returns a measure for each label value.
#For this exercise, calculate the intensity variance of vol with respect to different pixel sets. We have provided the 3D segmented image as labels: label 1 is the left ventricle and label 2 is a circular sample of tissue.

#After printing the variances, select the true statement from the answers below.

# Variance for all pixels
var_all = ndi.variance(vol, labels=None, index=None)
print('All pixels:', var_all)

# Variance for labeled pixels
var_labels = ndi.variance(vol, labels, index=None)
print('Labeled pixels:', var_labels)

# Variance for each object
var_objects =  ndi.variance(vol, labels, index=[1,2])
print('Left ventricle:', var_objects[0])
print('Other tissue:', var_objects[1])


#Answer

#<script.py> output:
#    All pixels: 840.4457526156154
#    Labeled pixels: 2166.5887761076724
#    Left ventricle: 1123.4641972021984
#    Other tissue: 1972.7151849347783

#--================================

# Variance for all pixels
var_all = ndi.variance(vol)
print('All pixels:', var_all)

# Variance for labeled pixels
var_labels = ndi.variance(vol, labels)
print('Labeled pixels:', var_labels)

# Variance for each object
var_objects = ndi.variance(vol, labels, index=[1,2])
print('Left ventricle:', var_objects[0])
print('Other tissue:', var_objects[1])

#All pixels" has the lowest variance because it has many pixels with 0 values.
#Great thinking. Often, global measurements are only useful for understanding the range and distribution of the data.
