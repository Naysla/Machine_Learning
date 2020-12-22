#Clustering Wikipedia part II
#It is now time to put your pipeline from the previous exercise to work! You are given an array articles of tf-idf word-frequencies of some popular Wikipedia articles, and a list titles of their titles. Use your pipeline to cluster the Wikipedia articles.

#A solution to the previous exercise has been pre-loaded for you, so a Pipeline pipeline chaining TruncatedSVD with KMeans is available.

# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))


#
    label                                        article
29      0                               Jennifer Aniston
28      0                                  Anne Hathaway
27      0                                 Dakota Fanning
26      0                                     Mila Kunis
25      0                                  Russell Crowe
24      0                                   Jessica Biel
23      0                           Catherine Zeta-Jones
22      0                              Denzel Washington
21      0                             Michael Fassbender
20      0                                 Angelina Jolie
0       1                                       HTTP 404
7       1                                  Social search
1       1                                 Alexa Internet
2       1                              Internet Explorer
3       1                                    HTTP cookie
4       1                                  Google Search
5       1                                         Tumblr
6       1                    Hypertext Transfer Protocol
8       1                                        Firefox
9       1                                       LinkedIn
58      2                                         Sepsis
59      2                                    Adam Levine
51      2                                     Nate Ruess
52      2                                     The Wanted
53      2                                   Stevie Nicks
54      2                                 Arctic Monkeys
55      2                                  Black Sabbath
56      2                                       Skrillex
57      2                          Red Hot Chili Peppers
50      2                                   Chad Kroeger
37      3                                       Football
39      3                                  Franck Ribéry
38      3                                         Neymar
36      3              2014 FIFA World Cup qualification
35      3                Colombia national football team
33      3                                 Radamel Falcao
32      3                                   Arsenal F.C.
31      3                              Cristiano Ronaldo
30      3                  France national football team
34      3                             Zlatan Ibrahimovic
10      4                                 Global warming
12      4                                   Nigel Lawson
13      4                               Connie Hedegaard
14      4                                 Climate change
15      4                                 Kyoto Protocol
16      4                                        350.org
17      4  Greenhouse gas emissions by the United States
18      4  2010 United Nations Climate Change Conference
19      4  2007 United Nations Climate Change Conference
11      4       Nationally Appropriate Mitigation Action
48      5                                     Gabapentin
46      5                                     Prednisone
45      5                                    Hepatitis C
44      5                                           Gout
43      5                                       Leukemia
42      5                                    Doxycycline
41      5                                    Hepatitis B
40      5                                    Tonsillitis
49      5                                       Lymphoma
47      5                                          Fever


#
Fantastic! Take a look at the cluster labels and see if you can identify any patterns!