#Field of view
#The amount of physical space covered by an image is its field of view, which is calculated from two properties:
#
#Array shape, the number of data elements on each axis. Can be accessed with the shape attribute.
#Sampling resolution, the amount of physical space covered by each pixel. Sometimes available in metadata (e.g., meta['sampling']).
#For this exercise, multiply the array shape and sampling resolution along each axis to calculate the field of view of vol. All values are in millimeters.

In [5]: vol.shape
Out[5]: (25, 512, 512)

In [6]: vol.meta['sampling']
Out[6]: (3.270000000000001, 0.976562, 0.976562)

In [7]: n0, n1, n2 = vol.shape

In [8]: d0, d1, d2 = vol.meta['sampling']

In [9]: n0 * d0, n1 * d1, n2 * d2
Out[9]: (81.75000000000003, 499.999744, 499.999744)

#Great job! You should always investigate your image's metadata to get a complete understanding of its origins.