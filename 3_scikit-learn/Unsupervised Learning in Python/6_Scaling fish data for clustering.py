#Scaling fish data for clustering
#You are given an array samples giving measurements of fish. Each row represents an individual fish. The measurements, such as weight in grams, length in centimeters, and the percentage ratio of height to length, have very different scales. In order to cluster this data effectively, you'll need to standardize these features first. In this exercise, you'll build a pipeline to standardize and cluster the data.
#
#These fish measurement data were sourced from the Journal of Statistics Education.
#http://jse.amstat.org/jse_data_archive.htm

#Para agrupar estos datos de manera efectiva
#primero deberá estandarizar estas características


# Perform the necessary imports
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Create scaler: scaler
scaler = StandardScaler()

# Create KMeans instance: kmeans
kmeans = KMeans(n_clusters=4)

# Create pipeline: pipeline
pipeline = make_pipeline(scaler,kmeans)

#Great work! Now that you've built the pipeline, you'll use it in the next exercise to cluster the fish by their measurements.