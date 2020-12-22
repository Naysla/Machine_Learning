#String to integer
#Now you'll use the .cast() method you learned in the previous exercise to convert all the appropriate columns from your DataFrame model_data to integers!
#
#To convert the type of a column using the .cast() method, you can write code like this:
#
#dataframe = dataframe.withColumn("col", dataframe.col.cast("new_type"))

# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))

#dataframe = dataframe.withColumn("col", dataframe.col.cast("new_type"))

#Awesome! You're a pro at converting columns!