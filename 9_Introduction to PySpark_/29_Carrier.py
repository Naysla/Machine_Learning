#Carrier
#In this exercise you'll create a StringIndexer and a OneHotEncoder to code the carrier column. To do this, you'll call the class constructors with the arguments inputCol and outputCol.
#
#The inputCol is the name of the column you want to index or encode, and the outputCol is the name of the new column that the Transformer should create.

# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier",outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index",outputCol="carrier_fact")

#Fantastic work! You're ready to include this column in your model now!