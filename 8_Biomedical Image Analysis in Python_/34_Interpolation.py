#Interpolation
#Interpolation is how new pixel intensities are estimated when an image transformation is applied. It is implemented in SciPy using sets of spline functions.
#
#Editing the interpolation order when using a function such as ndi.zoom() modifies the resulting estimate: higher orders provide more flexible estimates but take longer to compute.
#
#For this exercise, upsample im and investigate the effect of different interpolation orders on the resulting image.

# Upsample "im" by a factor of 4
up0 = ndi.zoom(im, zoom=(512/128), order=0)
up5 = ndi.zoom(im, zoom=(512/128), order=5)

# Print original and new shape
print('Original shape:', im.shape)
print('Upsampled shape:', up0.shape)

# Plot close-ups of the new images
fig, axes = plt.subplots(1, 2)
axes[0].imshow(up0[128:256, 128:256])
axes[1].imshow(up5[128:256, 128:256])
format_and_render_plots()


<script.py> output:
    Original shape: (128, 128)
    Upsampled shape: (512, 512)
 
 #Mejora y estabiliza la imagen
 #The key trade-off is that more complex interpolation methods require greater computational resources. This can take a heavy toll when analyzing 3D volumes.