#Fitting the model
#You're at the most fun part. You'll now fit the model. Recall that the data to be used as predictive features is loaded in a NumPy matrix called predictors and the data to be predicted is stored in a NumPy matrix called target. Your model is pre-written and it has been compiled with the code from the previous exercise.

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Specify the model
n_cols = predictors.shape[1]
model = Sequential()
model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Fit the model
model.fit(predictors, target)

#Answer

Epoch 1/10

 32/534 [>.............................] - ETA: 1s - loss: 146.0927
480/534 [=========================>....] - ETA: 0s - loss: 80.5114 
534/534 [==============================] - 0s - loss: 78.1496     
Epoch 2/10

 32/534 [>.............................] - ETA: 0s - loss: 85.0840
416/534 [======================>.......] - ETA: 0s - loss: 30.9422
534/534 [==============================] - 0s - loss: 30.3254     
Epoch 3/10

 32/534 [>.............................] - ETA: 0s - loss: 21.0493
534/534 [==============================] - 0s - loss: 27.0848     
Epoch 4/10

 32/534 [>.............................] - ETA: 0s - loss: 16.8331
534/534 [==============================] - 0s - loss: 25.1190     
Epoch 5/10

 32/534 [>.............................] - ETA: 0s - loss: 23.2067
416/534 [======================>.......] - ETA: 0s - loss: 22.0163
534/534 [==============================] - 0s - loss: 24.0181     
Epoch 6/10

 32/534 [>.............................] - ETA: 0s - loss: 13.3981
448/534 [========================>.....] - ETA: 0s - loss: 23.5140
534/534 [==============================] - 0s - loss: 23.1979     
Epoch 7/10

 32/534 [>.............................] - ETA: 0s - loss: 28.1686
224/534 [===========>..................] - ETA: 0s - loss: 21.8893
534/534 [==============================] - 0s - loss: 22.4486     
Epoch 8/10

 32/534 [>.............................] - ETA: 0s - loss: 11.3846
534/534 [==============================] - 0s - loss: 22.0785     
Epoch 9/10

 32/534 [>.............................] - ETA: 0s - loss: 21.9376
384/534 [====================>.........] - ETA: 0s - loss: 19.5797
534/534 [==============================] - 0s - loss: 21.7457     
Epoch 10/10

 32/534 [>.............................] - ETA: 0s - loss: 5.4751
352/534 [==================>...........] - ETA: 0s - loss: 18.0023
534/534 [==============================] - 0s - loss: 21.5531
Out[1]: <keras.callbacks.History at 0x7f683d3760b8>


#Superb! You now know how to specify, compile, and fit a deep learning model using keras!