#Clustering stocks using KMeans
#In this exercise, you'll cluster companies using their daily stock price movements (i.e. the dollar difference between the closing and opening prices for each trading day). You are given a NumPy array movements of daily price movements from 2010 to 2015 (obtained from Yahoo! Finance), where each row corresponds to a company, and each column corresponds to a trading day.
#
#Some stocks are more expensive than others. To account for this, include a Normalizer at the beginning of your pipeline. The Normalizer will separately transform each company's stock price to a relative scale before the clustering begins.
#
#Note that Normalizer() is different to StandardScaler(), which you used in the previous exercise. While StandardScaler() standardizes features (such as the features of the fish data from the previous exercise) by removing the mean and scaling to unit variance, Normalizer() rescales each sample - here, each company's stock price - independently of the other.

#KMeansy make_pipelineya han sido importados para ti.

# Import Normalizer
from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer,kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)

#Answer

#ERROR! Session/line number was not unique in database. History logging moved to new session 13
#Out[1]: 
#Pipeline(memory=None,
#         steps=[('normalizer', Normalizer(copy=True, norm='l2')),
#                ('kmeans',
#                 KMeans(algorithm='auto', copy_x=True, init='k-means++',
#                        max_iter=300, n_clusters=10, n_init=10, n_jobs=None,
#                        precompute_distances='auto', random_state=None,
#                        tol=0.0001, verbose=0))],
#         verbose=False)
		 
#Great work - you're really getting the hang of this. Now that your pipeline has been set up, you can find out which stocks move together in the next exercise!