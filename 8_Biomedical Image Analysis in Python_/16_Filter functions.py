#Filter functions
#Convolutions rely on a set of weights, but filtering can also be done using functions such as the mean, median and maximum. Just like with convolutions, filter functions will update each pixel value based on its local neighborhood.
#
#Consider the following lines of code:
#
#		im = np.array([[93, 36,  87], 
#					   [18, 49,  51],
#					   [45, 32,  63]])
#
#		im_filt = ____
#
#		assert im_filt[1,1] == 49
#
#Which of the following statements should go in the blank so that the assert statement evaluates to True?

#Answer
#ndi.median_filter(im, size=3)

#Great job! The median filter will return the median value of the 3x3 neighborhood. Note that the values on the edges will vary based on the mode setting of your filter