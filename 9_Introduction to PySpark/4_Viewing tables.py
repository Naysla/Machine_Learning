#Viewing tables
#Once you've created a SparkSession, you can start poking around to see what data is in your cluster!
#
#Your SparkSession has an attribute called catalog which lists all the data inside the cluster. This attribute has a few methods for extracting different pieces of information.
#
#One of the most useful is the .listTables() method, which returns the names of all the tables in your cluster as a list.

# Print the tables in the catalog
print(spark.catalog.listTables())

#<script.py> output:
 #   [Table(name='flights', database=None, description=None, tableType='TEMPORARY', isTemporary=True)]

	
	#Fantastic! What kind of data do you think is in that table?