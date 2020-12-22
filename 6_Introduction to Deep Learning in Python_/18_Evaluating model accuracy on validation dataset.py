#Evaluating model accuracy on validation dataset
#Now it's your turn to monitor model accuracy with a validation data set. A model definition has been provided as model. Your job is to add the code to compile it and then fit it. You'll check the validation score in each epoch.

# Save the number of columns in predictors: n_cols
#print(predictors)

n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
hist = model.fit(predictors, target, validation_split=0.3)

#Answer

Train on 623 samples, validate on 268 samples
Epoch 1/10

 32/623 [>.............................] - ETA: 19s - loss: 1.1222 - acc: 0.5312
128/623 [=====>........................] - ETA: 4s - loss: 0.8819 - acc: 0.5938 
384/623 [=================>............] - ETA: 0s - loss: 0.7231 - acc: 0.6615
623/623 [==============================] - 1s - loss: 0.7824 - acc: 0.6244 - val_loss: 0.7497 - val_acc: 0.6716
Epoch 2/10

 32/623 [>.............................] - ETA: 0s - loss: 0.7939 - acc: 0.5000
320/623 [==============>...............] - ETA: 0s - loss: 0.7686 - acc: 0.6406
623/623 [==============================] - 0s - loss: 0.7438 - acc: 0.6260 - val_loss: 0.5736 - val_acc: 0.7164
Epoch 3/10

 32/623 [>.............................] - ETA: 0s - loss: 0.5983 - acc: 0.7188
288/623 [============>.................] - ETA: 0s - loss: 0.6215 - acc: 0.6875
512/623 [=======================>......] - ETA: 0s - loss: 0.6488 - acc: 0.6699
623/623 [==============================] - 0s - loss: 0.6512 - acc: 0.6629 - val_loss: 0.5213 - val_acc: 0.7463
Epoch 4/10

 32/623 [>.............................] - ETA: 1s - loss: 0.5125 - acc: 0.6875
288/623 [============>.................] - ETA: 0s - loss: 0.5826 - acc: 0.6979
416/623 [===================>..........] - ETA: 0s - loss: 0.6010 - acc: 0.6923
512/623 [=======================>......] - ETA: 0s - loss: 0.6185 - acc: 0.6797
623/623 [==============================] - 0s - loss: 0.6404 - acc: 0.6629 - val_loss: 0.5309 - val_acc: 0.7201
Epoch 5/10

 32/623 [>.............................] - ETA: 0s - loss: 0.5278 - acc: 0.7500
288/623 [============>.................] - ETA: 0s - loss: 0.6231 - acc: 0.7083
512/623 [=======================>......] - ETA: 0s - loss: 0.6494 - acc: 0.6797
623/623 [==============================] - 0s - loss: 0.6327 - acc: 0.6886 - val_loss: 0.5039 - val_acc: 0.7612
Epoch 6/10

 32/623 [>.............................] - ETA: 0s - loss: 0.4591 - acc: 0.7812
288/623 [============>.................] - ETA: 0s - loss: 0.5722 - acc: 0.6910
480/623 [======================>.......] - ETA: 0s - loss: 0.5761 - acc: 0.6979
512/623 [=======================>......] - ETA: 0s - loss: 0.5783 - acc: 0.6934
623/623 [==============================] - 0s - loss: 0.5954 - acc: 0.6838 - val_loss: 0.5078 - val_acc: 0.7425
Epoch 7/10

 32/623 [>.............................] - ETA: 0s - loss: 0.5587 - acc: 0.7812
288/623 [============>.................] - ETA: 0s - loss: 0.5786 - acc: 0.7049
544/623 [=========================>....] - ETA: 0s - loss: 0.5729 - acc: 0.7224
623/623 [==============================] - 0s - loss: 0.5780 - acc: 0.7271 - val_loss: 0.5068 - val_acc: 0.7351
Epoch 8/10

 32/623 [>.............................] - ETA: 0s - loss: 0.4824 - acc: 0.7812
160/623 [======>.......................] - ETA: 0s - loss: 0.5938 - acc: 0.6625
384/623 [=================>............] - ETA: 0s - loss: 0.6047 - acc: 0.6849
512/623 [=======================>......] - ETA: 0s - loss: 0.6269 - acc: 0.6719
623/623 [==============================] - 0s - loss: 0.6507 - acc: 0.6645 - val_loss: 0.5367 - val_acc: 0.7351
Epoch 9/10

 32/623 [>.............................] - ETA: 0s - loss: 0.8304 - acc: 0.7188
352/623 [===============>..............] - ETA: 0s - loss: 0.6266 - acc: 0.6733
623/623 [==============================] - 0s - loss: 0.5882 - acc: 0.6950 - val_loss: 0.5074 - val_acc: 0.7687
Epoch 10/10

 32/623 [>.............................] - ETA: 0s - loss: 0.4698 - acc: 0.7500
416/623 [===================>..........] - ETA: 0s - loss: 0.6156 - acc: 0.6731
623/623 [==============================] - 0s - loss: 0.6216 - acc: 0.6950 - val_loss: 0.7432 - val_acc: 0.6455
