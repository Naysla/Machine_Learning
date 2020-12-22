#How many tokens?
#Recall from previous chapters that how you tokenize text affects the n-gram statistics used in your model.
#
#Going forward, you'll use alpha-numeric sequences, and only alpha-numeric sequences, as tokens. Alpha-numeric tokens contain only letters a-z and numbers 0-9 (no other characters). In other words, you'll tokenize on punctuation to generate n-gram statistics.
#
#In this exercise, you'll make sure you remember how to tokenize on punctuation.
#
#Assuming we tokenize on punctuation, accepting only alpha-numeric sequences as tokens, how many tokens are in the following string from the main dataset?
#
#'PLANNING,RES,DEV,& EVAL      '
#If you want, we've loaded this string into the workspace as SAMPLE_STRING, but you may not need it to answer the question.

4, because , and & are not tokens

Yes! Commas, "&", and whitespace are not alpha-numeric tokens. Keep it up!