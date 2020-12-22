# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))


# it returns the following

                                 CountryName CountryCode  ...  Year      Value
0                                 Arab World         ARB  ...  1960  31.285384
1                     Caribbean small states         CSS  ...  1960  31.597490
2             Central Europe and the Baltics         CEB  ...  1960  44.507921
3    East Asia & Pacific (all income levels)         EAS  ...  1960  22.471132
4      East Asia & Pacific (developing only)         EAP  ...  1960  16.917679
5                                  Euro area         EMU  ...  1960  62.096947
6  Europe & Central Asia (all income levels)         ECS  ...  1960  55.378977
7    Europe & Central Asia (developing only)         ECA  ...  1960  38.066129
8                             European Union         EUU  ...  1960  61.212898
9   Fragile and conflict affected situations         FCS  ...  1960  17.891972

[10 rows x 6 columns]
                                      CountryName CountryCode  ...  Year      Value
10         Heavily indebted poor countries (HIPC)         HPC  ...  1960  12.236046
11                                    High income         HIC  ...  1960  62.680332
12                           High income: nonOECD         NOC  ...  1960  56.107863
13                              High income: OECD         OEC  ...  1960  64.285435
14  Latin America & Caribbean (all income levels)         LCN  ...  1960  49.284688
15    Latin America & Caribbean (developing only)         LAC  ...  1960  44.863308
16   Least developed countries: UN classification         LDC  ...  1960   9.616261
17                            Low & middle income         LMY  ...  1960  21.272894
18                                     Low income         LIC  ...  1960  11.498396
19                            Lower middle income         LMC  ...  1960  19.810513

[10 rows x 6 columns]
