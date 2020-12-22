#Inspect your clustering
#Let's now inspect the clustering you performed in the previous exercise!
#
#A solution to the previous exercise has already run, so new_points is an array of points and labels is the array of their cluster labels.

# Import pyplot
import matplotlib.pyplot as plt

# Assign the columns of new_points: xs and ys
xs =new_points[:,0]
ys =new_points[:,1]

# Make a scatter plot of xs and ys, using labels to define the colors
# the c means colors , the color are in the array labels
plt.scatter(xs, ys, c=labels,alpha=0.5)

# Assign the cluster centers: centroids
centroids = model.cluster_centers_

# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:,0]
centroids_y = centroids[:,1]

# Make a scatter plot of centroids_x and centroids_y
plt.scatter(centroids_x, centroids_y, marker='D',s=50)
plt.show()

#Answer
#Ddevuelve una grafica mostrando tres agrupaciones (clustering) con colores distintos y en cada uno definiendo un punto central.

#Fantastic! The clustering looks great! But how can you be sure that 3 clusters is the correct choice? In other words, how can you evaluate the quality of a clustering? Tune into the next video in which Ben will explain how to evaluate a clustering!