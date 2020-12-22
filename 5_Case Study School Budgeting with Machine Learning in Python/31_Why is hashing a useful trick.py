#Why is hashing a useful trick?
#In the video, Peter explained that a hash function takes an input, in your case a token, and outputs a hash value. For example, the input may be a string and the hash value may be an integer.
#
#We've loaded a familiar python datatype, a dictionary called hash_dict, that makes this mapping concept a bit more explicit. In fact, python dictionaries ARE hash tables!
#
#Print hash_dict in the IPython Shell to get a sense of how strings can be mapped to integers.
#
#By explicitly stating how many possible outputs the hashing function may have, we limit the size of the objects that need to be processed. With these limits known, computation can be made more efficient and we can get results faster, even on large datasets.
#
#Using the above information, answer the following:
#
#Why is hashing a useful trick?

print(hash_dict)
{'petro': 354, 'vend': 785, 'fuel': 895, 'and': 780, 'fluids': 354}

#Answer
Some problems are memory-bound and not easily parallelizable, and hashing enforces a fixed length computation instead of using a mutable datatype (like a dictionary).

#Yes! Enforcing a fixed length can speed up calculations drastically, especially on large datasets!