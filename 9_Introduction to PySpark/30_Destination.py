#Destination
#Now you'll encode the dest column just like you did in the previous exercise.

# Create a StringIndexer
dest_indexer = StringIndexer(inputCol="dest",outputCol="dest_index")

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol="dest_index",outputCol="dest_fact")

#Perfect! You're all done messing with factors