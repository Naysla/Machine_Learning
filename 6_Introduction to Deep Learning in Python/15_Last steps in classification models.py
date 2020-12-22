#Last steps in classification models
#You'll now create a classification model using the titanic dataset, which has been pre-loaded into a DataFrame called df. You'll take information about the passengers and predict which ones survived.
#
#The predictive variables are stored in a NumPy array predictors. The target to predict is in df.survived, though you'll have to manipulate it for keras. The number of predictive features is stored in n_cols.
#
#Here, you'll use the 'sgd' optimizer, which stands for Stochastic Gradient Descent (https://en.wikipedia.org/wiki/Stochastic_gradient_descent). You'll learn more about this in the next chapter!

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical

# Convert the target to categorical: target
target = to_categorical(df.survived)

# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu',input_shape=(n_cols,)))

# Add the output layer
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(predictors, target)

#Answer

Epoch 1/10

 32/891 [>.............................] - ETA: 2s - loss: 7.6250 - acc: 0.2188
288/891 [========>.....................] - ETA: 0s - loss: 3.9219 - acc: 0.5104
544/891 [=================>............] - ETA: 0s - loss: 2.8209 - acc: 0.5919
891/891 [==============================] - 0s - loss: 3.0193 - acc: 0.5488     
Epoch 2/10

 32/891 [>.............................] - ETA: 0s - loss: 2.4046 - acc: 0.6562
384/891 [===========>..................] - ETA: 0s - loss: 1.6792 - acc: 0.6328
704/891 [======================>.......] - ETA: 0s - loss: 1.6642 - acc: 0.6151
891/891 [==============================] - 0s - loss: 1.6652 - acc: 0.6139     
Epoch 3/10

 32/891 [>.............................] - ETA: 0s - loss: 2.3377 - acc: 0.5000
416/891 [=============>................] - ETA: 0s - loss: 2.1456 - acc: 0.6082
704/891 [======================>.......] - ETA: 0s - loss: 2.1432 - acc: 0.5810
891/891 [==============================] - 0s - loss: 1.9323 - acc: 0.5960     
Epoch 4/10

 32/891 [>.............................] - ETA: 0s - loss: 1.0488 - acc: 0.5625
512/891 [================>.............] - ETA: 0s - loss: 1.0232 - acc: 0.6387
891/891 [==============================] - 0s - loss: 1.0880 - acc: 0.6375     
Epoch 5/10

 32/891 [>.............................] - ETA: 0s - loss: 0.9717 - acc: 0.6250
256/891 [=======>......................] - ETA: 0s - loss: 1.1031 - acc: 0.6328
480/891 [===============>..............] - ETA: 0s - loss: 1.0145 - acc: 0.6542
832/891 [===========================>..] - ETA: 0s - loss: 1.1397 - acc: 0.6130
891/891 [==============================] - 0s - loss: 1.1199 - acc: 0.6195     
Epoch 6/10

 32/891 [>.............................] - ETA: 0s - loss: 1.0438 - acc: 0.7188
384/891 [===========>..................] - ETA: 0s - loss: 1.1003 - acc: 0.6276
736/891 [=======================>......] - ETA: 0s - loss: 1.2345 - acc: 0.5938
891/891 [==============================] - 0s - loss: 1.1626 - acc: 0.6016     
Epoch 7/10

 32/891 [>.............................] - ETA: 0s - loss: 3.5110 - acc: 0.3750
352/891 [==========>...................] - ETA: 0s - loss: 1.6537 - acc: 0.6250
704/891 [======================>.......] - ETA: 0s - loss: 1.8782 - acc: 0.5952
891/891 [==============================] - 0s - loss: 1.8105 - acc: 0.6049     
Epoch 8/10

 32/891 [>.............................] - ETA: 0s - loss: 4.3734 - acc: 0.6250
480/891 [===============>..............] - ETA: 0s - loss: 2.4597 - acc: 0.5938
864/891 [============================>.] - ETA: 0s - loss: 2.7123 - acc: 0.5810
891/891 [==============================] - 0s - loss: 2.7621 - acc: 0.5713     
Epoch 9/10

 32/891 [>.............................] - ETA: 0s - loss: 2.8402 - acc: 0.4688
416/891 [=============>................] - ETA: 0s - loss: 2.6204 - acc: 0.5841
768/891 [========================>.....] - ETA: 0s - loss: 2.7869 - acc: 0.5833
891/891 [==============================] - 0s - loss: 2.7098 - acc: 0.5993     
Epoch 10/10

 32/891 [>.............................] - ETA: 0s - loss: 3.6600 - acc: 0.7500
224/891 [======>.......................] - ETA: 0s - loss: 8.4283 - acc: 0.4509
608/891 [===================>..........] - ETA: 0s - loss: 9.3440 - acc: 0.4079
891/891 [==============================] - 0s - loss: 8.2655 - acc: 0.4433
Out[1]: <keras.callbacks.History at 0x7f6838b30320>

#Fantastic! This simple model is generating an accuracy of 68!