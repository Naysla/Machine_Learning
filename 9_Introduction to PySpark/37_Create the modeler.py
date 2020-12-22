#Create the modeler
#The Estimator you'll be using is a LogisticRegression from the pyspark.ml.classification submodule.

# Import LogisticRegression
from pyspark.ml.classification import LogisticRegression

# Create a LogisticRegression Estimator
lr = LogisticRegression()

#Great work! That's the first step to any modeling in PySpark