#Early stopping: Optimizing the optimization
#Now that you know how to monitor your model performance throughout optimization, you can use early stopping to stop optimization when it isn't helping any more. Since the optimization stops automatically when it isn't helping, you can also set a high value for epochs in your call to .fit(), as Dan showed in the video.
#
#The model you'll optimize has been specified as model. As before, the data is pre-loaded as predictors and target.

# Import EarlyStopping
from keras.callbacks import EarlyStopping

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# Fit the model
model.fit(predictors, target, validation_split=0.3, epochs=30,
callbacks = [early_stopping_monitor])


#Answer

Train on 623 samples, validate on 268 samples
Epoch 1/30

 32/623 [>.............................] - ETA: 1s - loss: 0.7713 - acc: 0.5625
384/623 [=================>............] - ETA: 0s - loss: 0.8193 - acc: 0.5781
623/623 [==============================] - 0s - loss: 0.7515 - acc: 0.6035 - val_loss: 0.8040 - val_acc: 0.6493
Epoch 2/30

 32/623 [>.............................] - ETA: 0s - loss: 0.9735 - acc: 0.5625
512/623 [=======================>......] - ETA: 0s - loss: 0.6983 - acc: 0.6504
623/623 [==============================] - 0s - loss: 0.7164 - acc: 0.6324 - val_loss: 0.6303 - val_acc: 0.7090
Epoch 3/30

 32/623 [>.............................] - ETA: 0s - loss: 0.5596 - acc: 0.7188
384/623 [=================>............] - ETA: 0s - loss: 0.6505 - acc: 0.6849
623/623 [==============================] - 0s - loss: 0.7011 - acc: 0.6677 - val_loss: 0.6848 - val_acc: 0.6493
Epoch 4/30

 32/623 [>.............................] - ETA: 0s - loss: 0.5542 - acc: 0.6875
544/623 [=========================>....] - ETA: 0s - loss: 0.6613 - acc: 0.6526
623/623 [==============================] - 0s - loss: 0.6654 - acc: 0.6565 - val_loss: 0.6451 - val_acc: 0.7201
Epoch 5/30

 32/623 [>.............................] - ETA: 0s - loss: 0.8276 - acc: 0.6250
384/623 [=================>............] - ETA: 0s - loss: 0.6402 - acc: 0.6615
623/623 [==============================] - 0s - loss: 0.6244 - acc: 0.6790 - val_loss: 0.5165 - val_acc: 0.7388
Epoch 6/30

 32/623 [>.............................] - ETA: 0s - loss: 0.6729 - acc: 0.5625
416/623 [===================>..........] - ETA: 0s - loss: 0.5727 - acc: 0.6995
623/623 [==============================] - 0s - loss: 0.6048 - acc: 0.6966 - val_loss: 0.5793 - val_acc: 0.7425
Epoch 7/30

 32/623 [>.............................] - ETA: 0s - loss: 0.7018 - acc: 0.7188
512/623 [=======================>......] - ETA: 0s - loss: 0.5849 - acc: 0.7148
623/623 [==============================] - 0s - loss: 0.5878 - acc: 0.7079 - val_loss: 0.5136 - val_acc: 0.7537
Epoch 8/30

 32/623 [>.............................] - ETA: 0s - loss: 0.5653 - acc: 0.7188
448/623 [====================>.........] - ETA: 0s - loss: 0.5507 - acc: 0.7165
623/623 [==============================] - 0s - loss: 0.5597 - acc: 0.7255 - val_loss: 0.4775 - val_acc: 0.7687
Epoch 9/30

 32/623 [>.............................] - ETA: 0s - loss: 0.6003 - acc: 0.7500
256/623 [===========>..................] - ETA: 0s - loss: 0.5851 - acc: 0.6797
512/623 [=======================>......] - ETA: 0s - loss: 0.5669 - acc: 0.7090
623/623 [==============================] - 0s - loss: 0.5552 - acc: 0.7095 - val_loss: 0.4926 - val_acc: 0.7500
Epoch 10/30

 32/623 [>.............................] - ETA: 0s - loss: 0.5519 - acc: 0.7188
320/623 [==============>...............] - ETA: 0s - loss: 0.5044 - acc: 0.7594
608/623 [============================>.] - ETA: 0s - loss: 0.5418 - acc: 0.7286
623/623 [==============================] - 0s - loss: 0.5430 - acc: 0.7303 - val_loss: 0.4590 - val_acc: 0.7649
Epoch 11/30

 32/623 [>.............................] - ETA: 0s - loss: 0.5240 - acc: 0.7188
416/623 [===================>..........] - ETA: 0s - loss: 0.5192 - acc: 0.7668
623/623 [==============================] - 0s - loss: 0.5285 - acc: 0.7528 - val_loss: 0.4836 - val_acc: 0.7910
Epoch 12/30

 32/623 [>.............................] - ETA: 0s - loss: 0.5558 - acc: 0.8125
256/623 [===========>..................] - ETA: 0s - loss: 0.5287 - acc: 0.7500
608/623 [============================>.] - ETA: 0s - loss: 0.5361 - acc: 0.7500
623/623 [==============================] - 0s - loss: 0.5316 - acc: 0.7512 - val_loss: 0.4608 - val_acc: 0.8097
Epoch 13/30

 32/623 [>.............................] - ETA: 0s - loss: 0.4560 - acc: 0.8750
320/623 [==============>...............] - ETA: 0s - loss: 0.5731 - acc: 0.7656
623/623 [==============================] - 0s - loss: 0.6122 - acc: 0.7287 - val_loss: 0.6161 - val_acc: 0.7127
Out[5]: <keras.callbacks.History at 0x7f68177bb160>


#Wonderful work! Because optimization will automatically stop when it is no longer helpful, it is okay to specify the maximum number of epochs as 30 rather than using the default of 10 that you've used so far. Here, it seems like the optimization stopped after 7 epochs.