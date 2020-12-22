#Generate subplots
#You can draw multiple images in one figure to explore data quickly. Use plt.subplots() to generate an array of subplots.
#
#fig, axes = plt.subplots(nrows=2, ncols=2)
#
#
#To draw an image on a subplot, call the plotting method directly from the subplot object rather than through PyPlot: axes[0,0].imshow(im) rather than plt.imshow(im).
#
#For this exercise, draw im1 and im2 on separate subplots within the same figure.

# Import PyPlot
import matplotlib.pyplot as plt

# Initialize figure and axes grid
fig, axes = plt.subplots(nrows=2, ncols=1)

# Draw an image on each subplot
axes[0].imshow(im1,cmap='gray')
axes[1].imshow(im2,cmap='gray')

# Remove ticks/labels and render
axes[0].axis('off')
axes[1].axis('off')
plt.show()


#Answer
#Great work! For even more rapid visualization, you can use a large number of subplots and loop through your axes and images.
