#Transform the data
#Hooray, now you're finally ready to pass your data through the Pipeline you created!

# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)

#Great work! Your pipeline chewed right through that data!