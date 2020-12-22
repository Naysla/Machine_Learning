#Loading the data
#Now it's time to check out the dataset! You'll use pandas (which has been pre-imported as pd) to load your data into a DataFrame and then do some Exploratory Data Analysis (EDA) of it.
#
#The training data is available as TrainingData.csv. Your first task is to load it into a DataFrame in the IPython Shell using pd.read_csv() along with the keyword argument index_col=0.
#
#Use methods such as .info(), .head(), and .tail() to explore the budget data and the properties of the features and labels.
#
#Some of the column names correspond to features - descriptions of the budget items - such as the Job_Title_Description column. The values in this column tell us if a budget item is for a teacher, custodian, or other employee.
#
#Some columns correspond to the budget item labels you will be trying to predict with your model. For example, the Object_Type column describes whether the budget item is related classroom supplies, salary, travel expenses, etc.
#
#Use df.info() in the IPython Shell to answer the following questions:
#
#How many rows are there in the training data?
#How many columns are there in the training data?
#How many non-null entries are in the Job_Title_Description column?


import pandas as pd
pd.read_csv('TrainingData.csv',index_col=0)

                                               Function  ...                          Text_1
198                                            NO_LABEL  ...              TITLE I CARRYOVER 
209                              Student Transportation  ...                             NaN
750                                Teacher Compensation  ...                             NaN
931                                            NO_LABEL  ...                             NaN
1524                                           NO_LABEL  ...             TITLE I PI+HOMELESS
1770                                         Enrichment  ...                             NaN
1951                           Professional Development  ...  SCHOOL OPERATING ACCOUNT      
2542                         Physical Health & Services  ...               SPECIAL EDUCATION
2640                                Facilities Planning  ...                             NaN
2939                                 Social & Emotional  ...               EMPLOYEE BENEFITS
3029                           Extended Time & Tutoring  ...               EMPLOYEE BENEFITS
3395                            Substitute Compensation  ...             REGULAR INSTRUCTION
4490                                 Other Compensation  ...               EMPLOYEE BENEFITS
4593                               Teacher Compensation  ...               SPECIAL EDUCATION
5050                               Teacher Compensation  ...             REGULAR INSTRUCTION
5066                                           NO_LABEL  ...                      CHILD CARE
5370                                 Student Assignment  ...                         CENTRAL
5916                               Teacher Compensation  ...                             NaN
6029                         Physical Health & Services  ...                             NaN
6054                                         Enrichment  ...                       GAME WORK
6730                                           NO_LABEL  ...              PARENT INVOLVEMENT
6794         Finance, Budget, Purchasing & Distribution  ...                             NaN
7041                                           NO_LABEL  ...                   EXTENDED YEAR
7151                         Physical Health & Services  ...               SPECIAL EDUCATION
8384                 Instructional Materials & Supplies  ...                             NaN
8468                           Professional Development  ...                             NaN
8815                                         Enrichment  ...                             NaN
8960                             Student Transportation  ...                   EXTENDED DAYS
9722                                 Other Compensation  ...                             NaN
10876                          Extended Time & Tutoring  ...                   EXTENDED DAYS
...                                                 ...  ...                             ...
444647                             Teacher Compensation  ...       CRITICAL NEEDS SUPPLEMENT
444719                                    Food Services  ...                             NaN
444808                       Physical Health & Services  ...               SPECIAL EDUCATION
445206                         Professional Development  ...              RTTT ASIA SOCIETY 
445678                                Security & Safety  ...                             NaN
445947                               Aides Compensation  ...             REGULAR INSTRUCTION
445981                                        Utilities  ...                         CENTRAL
446032                            School Administration  ...           SCHOOL ADMINISTRATION
446102                       Untracked Budget Set-Aside  ...  TITLE I                       
446199                                        Utilities  ...    OPERATION AND MAINT OF PLANT
446528                            School Administration  ...           SCHOOL ADMINISTRATION
446628                           Student Transportation  ...          STUDENT TRANSPORTATION
446668                                  Library & Media  ...                             NaN
447383                             Teacher Compensation  ...               SPECIAL EDUCATION
447387                                       Enrichment  ...                             NaN
447492                            School Administration  ...                             NaN
447887                         Facilities & Maintenance  ...  MAINTENANCE                   
448122                         Facilities & Maintenance  ...                        OVERTIME
448298                                   Communications  ...                         CENTRAL
448628                                   Communications  ...                             NaN
448733               Instructional Materials & Supplies  ...                             NaN
448959  Special Population Program Management & Support  ...                             NaN
449761               Instructional Materials & Supplies  ...                             NaN
450067                            School Administration  ...           SCHOOL ADMINISTRATION
450277               Instructional Materials & Supplies  ...                             NaN
344986                          Substitute Compensation  ...             REGULAR INSTRUCTION
384803                                         NO_LABEL  ...                         CENTRAL
224382                          Substitute Compensation  ...                             NaN
305347                         Facilities & Maintenance  ...   ADDL REGULAR PAY-NOT SMOOTHED
101861                             Teacher Compensation  ...             REGULAR INSTRUCTION

[1560 rows x 25 columns]


sample_df =pd.read_csv('TrainingData.csv',index_col=0)
sample_df.info()

<class 'pandas.core.frame.DataFrame'>
Int64Index: 1560 entries, 198 to 101861
Data columns (total 25 columns):
Function                  1560 non-null object
Use                       1560 non-null object
Sharing                   1560 non-null object
Reporting                 1560 non-null object
Student_Type              1560 non-null object
Position_Type             1560 non-null object
Object_Type               1560 non-null object
Pre_K                     1560 non-null object
Operating_Status          1560 non-null object
Object_Description        1461 non-null object
Text_2                    382 non-null object
SubFund_Description       1183 non-null object
Job_Title_Description     1131 non-null object
Text_3                    296 non-null object
Text_4                    193 non-null object
Sub_Object_Description    364 non-null object
Location_Description      874 non-null object
FTE                       449 non-null float64
Function_Description      1340 non-null object
Facility_or_Department    252 non-null object
Position_Extra            1026 non-null object
Total                     1542 non-null float64
Program_Description       1192 non-null object
Fund_Description          819 non-null object
Text_1                    1132 non-null object
dtypes: float64(2), object(23)
memory usage: 356.9+ KB

sample_df.head()

                    Function          Use  ...                                   Fund_Description                Text_1
198                 NO_LABEL     NO_LABEL  ...  Title I - Disadvantaged Children/Targeted Assi...    TITLE I CARRYOVER 
209   Student Transportation     NO_LABEL  ...                                       General Fund                   NaN
750     Teacher Compensation  Instruction  ...                             General Purpose School                   NaN
931                 NO_LABEL     NO_LABEL  ...                             General Operating Fund                   NaN
1524                NO_LABEL     NO_LABEL  ...  Title I - Disadvantaged Children/Targeted Assi...   TITLE I PI+HOMELESS

[5 rows x 25 columns]

sample_df.describe()

              FTE         Total
count  449.000000  1.542000e+03
mean     0.493532  1.446867e+04
std      0.452844  7.916752e+04
min     -0.002369 -1.044084e+06
25%      0.004310  1.108111e+02
50%      0.440000  7.060299e+02
75%      1.000000  5.347760e+03
max      1.047222  1.367500e+06


sample_df.tail()

                        Function          Use  ...                Fund_Description                         Text_1
344986   Substitute Compensation  Instruction  ...                             NaN            REGULAR INSTRUCTION
384803                  NO_LABEL     NO_LABEL  ...                             NaN                        CENTRAL
224382   Substitute Compensation  Instruction  ...  GENERAL FUND                                              NaN
305347  Facilities & Maintenance          O&M  ...          General Operating Fund  ADDL REGULAR PAY-NOT SMOOTHED
101861      Teacher Compensation  Instruction  ...                             NaN            REGULAR INSTRUCTION

[5 rows x 25 columns]


#Answer
#1560 rows, 25 columns, 1131 non-null entries in Job_Title_Description.
#Yes! Looks like there are a lot of missing values. You will need to keep your eyes on those.