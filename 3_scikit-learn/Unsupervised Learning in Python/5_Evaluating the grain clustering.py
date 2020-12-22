#Evaluating the grain clustering
#In the previous exercise, you observed from the inertia plot that 3 is a good number of clusters for the grain data. In fact, the grain samples come from a mix of 3 different grain varieties: "Kama", "Rosa" and "Canadian". In this exercise, cluster the grain samples into three clusters, and compare the clusters to the grain varieties using a cross-tabulation.
#
#You have the array samples of grain samples, and a list varieties giving the grain variety for each sample. Pandas (pd) and KMeans have already been imported for you.

#Usted tiene la variedad samplesde muestras de granos y una lista varietiescon la variedad de granos para cada muestra. Pandas ( pd) y KMeansya han sido importados por ti.

# Create a KMeans model with 3 clusters: model
#segun el ejercicio anterior se identifico en la grafica que lo mejor es trabajar con maximo 3 grupos (cluster)
model = KMeans(n_clusters=3)

# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(samples)

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# Create crosstab: ct
#crosstab: tabla de referencias cruzadas
ct = pd.crosstab(df['labels'],df['varieties'])

# Display ct
print(ct)

#Answer

#varieties  Canadian wheat  Kama wheat  Rosa wheat
#labels                                           
#0                      68           9           0
#1                       0           1          60
#2                       2          60          10

#Great work! The cross-tabulation shows that the 3 varieties of grain separate really well into 3 clusters. But depending on the type of data you are working with, the clustering may not always be this good. Is there anything you can do in such situations to improve your clustering? You'll find out in the next video!