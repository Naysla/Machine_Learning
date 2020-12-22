#Precision-recall Curve
#When looking at your ROC curve, you may have noticed that the y-axis (True positive rate) is also known as recall. Indeed, in addition to the ROC curve, there are other ways to visually evaluate model performance. One such way is the precision-recall curve, which is generated by plotting the precision and recall for different thresholds. As a reminder, precision and recall are defined as:
#
#Precision=TP/(TP+FP)
#Recall=TP/(TP+FN)
#
#On the right, a precision-recall curve has been generated for the diabetes dataset. The classification report and confusion matrix are displayed in the IPython Shell.
#
#Study the precision-recall curve and then consider the statements given below. Choose the one statement that is not true. Note that here, the class is positive (1) if the individual has diabetes.

#Analisis

precision    recall  f1-score   support

          0       0.83      0.85      0.84       206
          1       0.69      0.66      0.67       102

avg / total       0.79      0.79      0.79       308

[[176  30]
 [ 35  67]]
 
 #Respuesta
 
 Precision and recall take true negatives into consideration.
 Great work! True negatives do not appear at all in the definitions of precision and recall.
