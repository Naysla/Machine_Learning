#Privacy protection
#Let's look at a real-world application of what you have learned in the course.
#
#In this exercise, you will detect human faces in the image and for the sake of privacy, you will anonymize data by blurring people's faces in the image automatically.
#	Image preloaded as group_image.
#You can use the gaussian filter for the blurriness.
#
#The face detector is ready to use as detector and all packages needed have been imported.


# Detect the faces
detected = detector.detect_multi_scale(img=group_image, 
                                       scale_factor=1.2, step_ratio=1, 
                                       min_size=(10,10), max_size=(100, 100))
# For each detected face
for d in detected:  
    # Obtain the face rectangle from detected coordinates
    face = getFaceRectangle(d)
    
    # Apply gaussian filter to extracted face
    blurred_face = gaussian(face, multichannel=True, sigma = 8)
    
    # Merge this blurry face to our final image and show it
    resulting_image = mergeBlurryFace(group_image, blurred_face) 
show_image(resulting_image, "Blurred faces")

#You solved this important issue by applying what you have learned in the course.

#reconoce los rostros de una fotografia y con el algoritmo gaussian distorciona los rostros por privacidad