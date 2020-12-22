#PCA doesn't learn parts
#Unlike NMF, PCA doesn't learn the parts of things. Its components do not correspond to topics (in the case of documents) or to parts of images, when trained on images. Verify this for yourself by inspecting the components of a PCA model fit to the dataset of LED digit images from the previous exercise. The images are available as a 2D array samples. Also available is a modified version of the show_as_image() function which colors a pixel red if the value is negative.
#
#After submitting the answer, notice that the components of PCA do not represent meaningful parts of images of LED digits!

# Import PCA
from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)

# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)
    
	
#Answer

#muestra una figura segun lograficado por la funcion show_as_image en el loop, parece que se moviera la imagen,

#Great work! Notice that the components of PCA do not represent meaningful parts of images of LED digits!