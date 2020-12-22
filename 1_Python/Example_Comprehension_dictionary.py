#Practice from datacamp course: Phyton Data Science Tollbox
# Create a list of strings: fellowship
fellowship = ['hi', 'this', 'is', 'an', 'example']

# Create dict comprehension: new_fellowship
new_fellowship = {member:len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)


#Result
#{'hi': 2, 'this': 4, 'is': 2, 'an': 2, 'example': 7}