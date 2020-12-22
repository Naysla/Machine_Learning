#Calculate volume
#
#Quantifying tissue morphology, or shape is one primary objective of biomedical imaging. The size, shape, and uniformity of a tissue can reveal essential health insights.
#
#For this exercise, measure the volume of the left ventricle in one 3D image (vol).
#
#First, count the number of voxels in the left ventricle (label value of 1). Then, multiply it by the size of each voxel in mm3. (Check vol.meta for the sampling rate.)

# Calculate volume per voxel
d0, d1, d2 = vol.meta['sampling']
dvoxel = d0 * d1 * d2
# Count label voxels
nvoxels=ndi.sum(1, vol, index=1)
# Calculate volume of label
volume = ndi.sum(1, label, index=1) * vol.meta['sampling']

volume
120,731

#Answer
#120,731 mm3
#Well done! Volume is a basic but useful measure, and it is a great "reality check" when evaluating your processes.