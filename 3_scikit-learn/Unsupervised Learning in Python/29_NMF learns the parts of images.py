#NMF learns the parts of images
#Now use what you've learned about NMF to decompose the digits dataset. You are again given the digit images as a 2D array samples. This time, you are also provided with a function show_as_image() that displays the image encoded by any 1D array:
#
#def show_as_image(sample):
#    bitmap = sample.reshape((13, 8))
#    plt.figure()
#    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
#    plt.colorbar()
#    plt.show()
#	
#After you are done, take a moment to look through the plots and notice how NMF has expressed the digit as a sum of the components!


# Import NMF
from sklearn.decomposition import NMF

# Create an NMF model: model
model = NMF(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)

# Assign the 0th row of features: digit_features
digit_features = features[0,:]

# Print digit_features
print(digit_features)

#Answer

#muestra varias graficas segun se hace el recorrido por el componenteen el loop, parece que la imagen se mueve

[4.76823559e-01 0.00000000e+00 0.00000000e+00 5.90605054e-01
 4.81559442e-01 0.00000000e+00 7.37535093e-16]
 
 #Great work! Take a moment to look through the plots and notice how NMF has expressed the digit as a sum of the components!