'''
Defining a schema
Creating a defined schema helps with data quality and import performance. As mentioned during the lesson, we'll create a simple schema to read in the following columns:

Name
Age
City
The Name and City columns are StringType() and the Age column is an IntegerType().
'''

# Import the pyspark.sql.types library
from pyspark.sql.types import *

# Define a new schema using the StructType method
people_schema = StructType([
  # Define a StructField for each field
  StructField('name', StringType(), False),
  StructField('age', IntegerType(), False),
  StructField('city', StringType(),False)
])