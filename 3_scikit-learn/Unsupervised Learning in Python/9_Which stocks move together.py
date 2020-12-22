#Which stocks move together?
#In the previous exercise, you clustered companies by their daily stock price movements. So which company have stock prices that tend to change in the same way? You'll now inspect the cluster labels from your clustering to find out.
#
#Your solution to the previous exercise has already been run. Recall that you constructed a Pipeline pipeline containing a KMeans model and fit it to the NumPy array movements of daily stock movements. In addition, a list companies of the company names is available.

# Import pandas
import pandas as pd

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))

#Answer

    labels                           companies
47       0                            Symantec
33       0                           Microsoft
22       1                                  HP
53       1                       Valero Energy
44       1                        Schlumberger
23       1                                 IBM
52       1                            Unilever
58       1                               Xerox
30       1                          MasterCard
32       1                                  3M
49       1                               Total
35       1                            Navistar
37       1                            Novartis
42       1                   Royal Dutch Shell
43       1                                 SAP
20       1                          Home Depot
19       1                     GlaxoSmithKline
46       1                      Sanofi-Aventis
14       1                                Dell
13       1                   DuPont de Nemours
12       1                             Chevron
11       1                               Cisco
57       1                               Exxon
10       1                      ConocoPhillips
8        1                         Caterpillar
6        1            British American Tobacco
31       2                           McDonalds
41       2                       Philip Morris
38       2                               Pepsi
28       2                           Coca Cola
9        2                   Colgate-Palmolive
1        3                                 AIG
3        3                    American express
5        3                     Bank of America
18       3                       Goldman Sachs
26       3                      JPMorgan Chase
55       3                         Wells Fargo
16       3                   General Electrics
2        4                              Amazon
59       4                               Yahoo
54       5                            Walgreen
27       5                      Kimberly-Clark
25       5                   Johnson & Johnson
39       5                              Pfizer
40       5                      Procter Gamble
56       5                            Wal-Mart
0        6                               Apple
17       6                     Google/Alphabet
36       7                    Northrop Grumman
4        7                              Boeing
29       7                     Lookheed Martin
48       8                              Toyota
34       8                          Mitsubishi
21       8                               Honda
15       8                                Ford
7        8                               Canon
45       8                                Sony
50       9  Taiwan Semiconductor Manufacturing
51       9                   Texas instruments
24       9                               Intel

#Fantastic job - you have completed Chapter 1! Take a look at the clusters. Are you surprised by any of the results? In the next chapter, you'll learn about how to communicate results such as this through visualizations.

