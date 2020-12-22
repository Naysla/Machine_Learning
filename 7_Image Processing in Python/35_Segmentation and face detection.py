#Segmentation and face detection
#Previously, you learned how to make processes more computationally efficient with unsupervised superpixel segmentation. In this exercise, you'll do just that!
#
#Using the slic() function for segmentation, pre-process the image before passing it to the face detector.
#
#Image preloaded as profile_image.
#The Cascade class, the slic() function from segmentation module, and the show_detected_face() function for visualization have already been imported. The detector is already initialized and ready to use as detector.

# Obtain the segmentation with default 100 regions
segments = slic(profile_image, n_segments= 100)

# Obtain segmented image using label2rgb
segmented_image = label2rgb(segments, profile_image, kind='avg')

# Detect the faces with multi scale method
detected = detector.detect_multi_scale(img=segmented_image, 
                                       scale_factor=1.2, 
                                       step_ratio=1, 
                                       min_size=(10, 10), max_size=(1000, 1000))

# Show the detected faces
show_detected_face(segmented_image, detected)

# {'r': 110, 'c': 169, 'width': 340, 'height': 340}
#Hurray!
#You applied segementation to the image before passing it to the face detector and it's finding the face even when the image is relatively large.
#This time you used 1000 by 1000 pixels as the maximum size of the searching window because the face in this case was indeed rather larger in comparison to the image.