#Building your own digit recognition model
#You've reached the final exercise of the course - you now know everything you need to build an accurate model to recognize handwritten digits!
#
#We've already done the basic manipulation of the MNIST dataset shown in the video, so you have X and y loaded and ready to model with. Sequential and Dense from keras are also pre-imported.
#
#To add an extra challenge, we've loaded only 2500 images, rather than 60000 which you will see in some published results. Deep learning models perform better with more data, however, they also take longer to train, especially when they start becoming more complex.
#
#If you have a computer with a CUDA compatible GPU, you can take advantage of it to improve computation time. If you don't have a GPU, no problem! You can set up a deep learning environment in the cloud that can run your models on a GPU. Here is a blog post by Dan that explains how to do this - check it out after completing this exercise! It is a great next step as you continue your deep learning journey.
#
#Ready to take your deep learning to the next level? Check out Advanced Deep Learning with Keras in Python to see how the Keras functional API lets you build domain knowledge to solve new types of problems. Once you know how to use the functional API, take a look at "Convolutional Neural Networks for Image Processing" to learn image-specific applications of Keras.

#https://www.datacamp.com/community/tutorials/deep-learning-jupyter-aws
#https://learn.datacamp.com/courses/advanced-deep-learning-with-keras-in-python
#https://learn.datacamp.com/courses/convolutional-neural-networks-for-image-processing

# Create the model: model
model = Sequential()

# Add the first hidden layer
model.add(Dense(50, activation='relu', input_shape=(784,)))

# Add the second hidden layer
model.add(Dense(50, activation='relu'))

# Add the output layer
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X,y,validation_split=0.3)




Train on 1750 samples, validate on 750 samples
Epoch 1/10

  32/1750 [..............................] - ETA: 9s - loss: 2.2325 - acc: 0.2500
  64/1750 [>.............................] - ETA: 8s - loss: 2.2860 - acc: 0.1875
 224/1750 [==>...........................] - ETA: 2s - loss: 2.2325 - acc: 0.1875
 384/1750 [=====>........................] - ETA: 1s - loss: 2.1722 - acc: 0.2526
 480/1750 [=======>......................] - ETA: 1s - loss: 2.1410 - acc: 0.2625
 608/1750 [=========>....................] - ETA: 1s - loss: 2.1022 - acc: 0.2747
 864/1750 [=============>................] - ETA: 0s - loss: 1.9915 - acc: 0.3356
1024/1750 [================>.............] - ETA: 0s - loss: 1.9274 - acc: 0.3760
1184/1750 [===================>..........] - ETA: 0s - loss: 1.8473 - acc: 0.4155
1408/1750 [=======================>......] - ETA: 0s - loss: 1.7340 - acc: 0.4645
1664/1750 [===========================>..] - ETA: 0s - loss: 1.6239 - acc: 0.5048
1750/1750 [==============================] - 1s - loss: 1.5902 - acc: 0.5149 - val_loss: 0.9465 - val_acc: 0.7080
Epoch 2/10

  32/1750 [..............................] - ETA: 1s - loss: 0.7742 - acc: 0.7812
 224/1750 [==>...........................] - ETA: 0s - loss: 0.8542 - acc: 0.7545
 384/1750 [=====>........................] - ETA: 0s - loss: 0.8229 - acc: 0.7656
 608/1750 [=========>....................] - ETA: 0s - loss: 0.7797 - acc: 0.7780
 704/1750 [===========>..................] - ETA: 0s - loss: 0.7641 - acc: 0.7855
 800/1750 [============>.................] - ETA: 0s - loss: 0.7651 - acc: 0.7863
1056/1750 [=================>............] - ETA: 0s - loss: 0.7348 - acc: 0.7917
1440/1750 [=======================>......] - ETA: 0s - loss: 0.6947 - acc: 0.8063
1664/1750 [===========================>..] - ETA: 0s - loss: 0.6646 - acc: 0.8155
1750/1750 [==============================] - 0s - loss: 0.6590 - acc: 0.8160 - val_loss: 0.5394 - val_acc: 0.8413
Epoch 3/10

  32/1750 [..............................] - ETA: 0s - loss: 0.5672 - acc: 0.7500
 288/1750 [===>..........................] - ETA: 0s - loss: 0.4190 - acc: 0.8854
 576/1750 [========>.....................] - ETA: 0s - loss: 0.4302 - acc: 0.8785
 864/1750 [=============>................] - ETA: 0s - loss: 0.4447 - acc: 0.8819
1024/1750 [================>.............] - ETA: 0s - loss: 0.4423 - acc: 0.8838
1184/1750 [===================>..........] - ETA: 0s - loss: 0.4328 - acc: 0.8860
1408/1750 [=======================>......] - ETA: 0s - loss: 0.4269 - acc: 0.8828
1568/1750 [=========================>....] - ETA: 0s - loss: 0.4244 - acc: 0.8839
1750/1750 [==============================] - 0s - loss: 0.4231 - acc: 0.8846 - val_loss: 0.4293 - val_acc: 0.8813
Epoch 4/10

  32/1750 [..............................] - ETA: 0s - loss: 0.2753 - acc: 0.9375
 160/1750 [=>............................] - ETA: 0s - loss: 0.2932 - acc: 0.9125
 384/1750 [=====>........................] - ETA: 0s - loss: 0.3337 - acc: 0.8984
 576/1750 [========>.....................] - ETA: 0s - loss: 0.3309 - acc: 0.9010
 832/1750 [=============>................] - ETA: 0s - loss: 0.3281 - acc: 0.9050
1120/1750 [==================>...........] - ETA: 0s - loss: 0.3241 - acc: 0.9080
1312/1750 [=====================>........] - ETA: 0s - loss: 0.3332 - acc: 0.9040
1536/1750 [=========================>....] - ETA: 0s - loss: 0.3262 - acc: 0.9049
1696/1750 [============================>.] - ETA: 0s - loss: 0.3190 - acc: 0.9110
1750/1750 [==============================] - 0s - loss: 0.3190 - acc: 0.9109 - val_loss: 0.3896 - val_acc: 0.8880
Epoch 5/10

  32/1750 [..............................] - ETA: 0s - loss: 0.2987 - acc: 0.9062
 192/1750 [==>...........................] - ETA: 0s - loss: 0.2544 - acc: 0.9219
 320/1750 [====>.........................] - ETA: 0s - loss: 0.2386 - acc: 0.9375
 448/1750 [======>.......................] - ETA: 0s - loss: 0.2831 - acc: 0.9241
 544/1750 [========>.....................] - ETA: 0s - loss: 0.2753 - acc: 0.9283
 800/1750 [============>.................] - ETA: 0s - loss: 0.2896 - acc: 0.9213
 928/1750 [==============>...............] - ETA: 0s - loss: 0.2794 - acc: 0.9246
1056/1750 [=================>............] - ETA: 0s - loss: 0.2683 - acc: 0.9271
1248/1750 [====================>.........] - ETA: 0s - loss: 0.2635 - acc: 0.9271
1440/1750 [=======================>......] - ETA: 0s - loss: 0.2714 - acc: 0.9271
1696/1750 [============================>.] - ETA: 0s - loss: 0.2666 - acc: 0.9281
1750/1750 [==============================] - 0s - loss: 0.2636 - acc: 0.9297 - val_loss: 0.3537 - val_acc: 0.8947
Epoch 6/10

  32/1750 [..............................] - ETA: 0s - loss: 0.1392 - acc: 0.9688
 192/1750 [==>...........................] - ETA: 0s - loss: 0.2530 - acc: 0.9323
 448/1750 [======>.......................] - ETA: 0s - loss: 0.2095 - acc: 0.9420
 608/1750 [=========>....................] - ETA: 0s - loss: 0.2216 - acc: 0.9375
 736/1750 [===========>..................] - ETA: 0s - loss: 0.2166 - acc: 0.9402
 896/1750 [==============>...............] - ETA: 0s - loss: 0.2168 - acc: 0.9397
 960/1750 [===============>..............] - ETA: 0s - loss: 0.2150 - acc: 0.9406
1184/1750 [===================>..........] - ETA: 0s - loss: 0.2122 - acc: 0.9426
1408/1750 [=======================>......] - ETA: 0s - loss: 0.2078 - acc: 0.9439
1568/1750 [=========================>....] - ETA: 0s - loss: 0.2030 - acc: 0.9445
1664/1750 [===========================>..] - ETA: 0s - loss: 0.2020 - acc: 0.9453
1750/1750 [==============================] - 0s - loss: 0.2074 - acc: 0.9440 - val_loss: 0.3473 - val_acc: 0.8907
Epoch 7/10

  32/1750 [..............................] - ETA: 0s - loss: 0.1786 - acc: 0.9375
  96/1750 [>.............................] - ETA: 1s - loss: 0.1653 - acc: 0.9271
 224/1750 [==>...........................] - ETA: 0s - loss: 0.2175 - acc: 0.9330
 320/1750 [====>.........................] - ETA: 0s - loss: 0.2098 - acc: 0.9469
 576/1750 [========>.....................] - ETA: 0s - loss: 0.1856 - acc: 0.9549
 864/1750 [=============>................] - ETA: 0s - loss: 0.1908 - acc: 0.9525
1120/1750 [==================>...........] - ETA: 0s - loss: 0.1809 - acc: 0.9554
1376/1750 [======================>.......] - ETA: 0s - loss: 0.1719 - acc: 0.9600
1600/1750 [==========================>...] - ETA: 0s - loss: 0.1778 - acc: 0.9587
1750/1750 [==============================] - 0s - loss: 0.1775 - acc: 0.9583 - val_loss: 0.3417 - val_acc: 0.8947
Epoch 8/10

  32/1750 [..............................] - ETA: 1s - loss: 0.2642 - acc: 0.9375
 160/1750 [=>............................] - ETA: 0s - loss: 0.1407 - acc: 0.9625
 320/1750 [====>.........................] - ETA: 0s - loss: 0.1581 - acc: 0.9625
 544/1750 [========>.....................] - ETA: 0s - loss: 0.1463 - acc: 0.9688
 736/1750 [===========>..................] - ETA: 0s - loss: 0.1568 - acc: 0.9647
 864/1750 [=============>................] - ETA: 0s - loss: 0.1605 - acc: 0.9664
 960/1750 [===============>..............] - ETA: 0s - loss: 0.1538 - acc: 0.9688
1152/1750 [==================>...........] - ETA: 0s - loss: 0.1492 - acc: 0.9670
1408/1750 [=======================>......] - ETA: 0s - loss: 0.1456 - acc: 0.9688
1696/1750 [============================>.] - ETA: 0s - loss: 0.1451 - acc: 0.9688
1750/1750 [==============================] - 0s - loss: 0.1450 - acc: 0.9686 - val_loss: 0.3343 - val_acc: 0.9000
Epoch 9/10

  32/1750 [..............................] - ETA: 1s - loss: 0.0741 - acc: 0.9688
 192/1750 [==>...........................] - ETA: 0s - loss: 0.1057 - acc: 0.9531
 352/1750 [=====>........................] - ETA: 0s - loss: 0.1105 - acc: 0.9631
 544/1750 [========>.....................] - ETA: 0s - loss: 0.1121 - acc: 0.9651
 576/1750 [========>.....................] - ETA: 0s - loss: 0.1103 - acc: 0.9670
 672/1750 [==========>...................] - ETA: 0s - loss: 0.1145 - acc: 0.9628
 736/1750 [===========>..................] - ETA: 0s - loss: 0.1086 - acc: 0.9647
 832/1750 [=============>................] - ETA: 0s - loss: 0.1169 - acc: 0.9639
 992/1750 [================>.............] - ETA: 0s - loss: 0.1221 - acc: 0.9657
1152/1750 [==================>...........] - ETA: 0s - loss: 0.1187 - acc: 0.9679
1344/1750 [======================>.......] - ETA: 0s - loss: 0.1164 - acc: 0.9710
1504/1750 [========================>.....] - ETA: 0s - loss: 0.1147 - acc: 0.9721
1696/1750 [============================>.] - ETA: 0s - loss: 0.1152 - acc: 0.9711
1750/1750 [==============================] - 0s - loss: 0.1207 - acc: 0.9703 - val_loss: 0.3264 - val_acc: 0.8973
Epoch 10/10

  32/1750 [..............................] - ETA: 1s - loss: 0.0429 - acc: 1.0000
 256/1750 [===>..........................] - ETA: 0s - loss: 0.0912 - acc: 0.9922
 448/1750 [======>.......................] - ETA: 0s - loss: 0.0823 - acc: 0.9911
 704/1750 [===========>..................] - ETA: 0s - loss: 0.0872 - acc: 0.9858
 768/1750 [============>.................] - ETA: 0s - loss: 0.0960 - acc: 0.9857
 832/1750 [=============>................] - ETA: 0s - loss: 0.0962 - acc: 0.9856
 896/1750 [==============>...............] - ETA: 0s - loss: 0.0980 - acc: 0.9855
1088/1750 [=================>............] - ETA: 0s - loss: 0.0961 - acc: 0.9835
1280/1750 [====================>.........] - ETA: 0s - loss: 0.0952 - acc: 0.9828
1472/1750 [========================>.....] - ETA: 0s - loss: 0.0967 - acc: 0.9817
1664/1750 [===========================>..] - ETA: 0s - loss: 0.1015 - acc: 0.9808
1750/1750 [==============================] - 0s - loss: 0.1001 - acc: 0.9811 - val_loss: 0.3287 - val_acc: 0.9040
Out[3]: <keras.callbacks.History at 0x7f68807c6828>

<script.py> output:
    Train on 1750 samples, validate on 750 samples
    Epoch 1/10
    
  32/1750 [..............................] - ETA: 3s - loss: 2.1979 - acc: 0.2188
 384/1750 [=====>........................] - ETA: 0s - loss: 2.2020 - acc: 0.2266
 736/1750 [===========>..................] - ETA: 0s - loss: 2.0607 - acc: 0.3043
1152/1750 [==================>...........] - ETA: 0s - loss: 1.9053 - acc: 0.3620
1664/1750 [===========================>..] - ETA: 0s - loss: 1.7018 - acc: 0.4543
1750/1750 [==============================] - 0s - loss: 1.6709 - acc: 0.4686 - val_loss: 1.0077 - val_acc: 0.7640
    Epoch 2/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.9368 - acc: 0.7500
 448/1750 [======>.......................] - ETA: 0s - loss: 0.7632 - acc: 0.8371
 896/1750 [==============>...............] - ETA: 0s - loss: 0.7488 - acc: 0.8248
1376/1750 [======================>.......] - ETA: 0s - loss: 0.7153 - acc: 0.8227
1750/1750 [==============================] - 0s - loss: 0.6762 - acc: 0.8280 - val_loss: 0.5319 - val_acc: 0.8627
    Epoch 3/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.3694 - acc: 0.9688
 448/1750 [======>.......................] - ETA: 0s - loss: 0.4327 - acc: 0.8973
 832/1750 [=============>................] - ETA: 0s - loss: 0.4117 - acc: 0.8966
1056/1750 [=================>............] - ETA: 0s - loss: 0.4084 - acc: 0.8987
1312/1750 [=====================>........] - ETA: 0s - loss: 0.3990 - acc: 0.8986
1632/1750 [==========================>...] - ETA: 0s - loss: 0.4138 - acc: 0.8897
1750/1750 [==============================] - 0s - loss: 0.4170 - acc: 0.8857 - val_loss: 0.4487 - val_acc: 0.8653
    Epoch 4/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.1837 - acc: 0.9062
 320/1750 [====>.........................] - ETA: 0s - loss: 0.2809 - acc: 0.9281
 672/1750 [==========>...................] - ETA: 0s - loss: 0.3173 - acc: 0.9167
 992/1750 [================>.............] - ETA: 0s - loss: 0.3353 - acc: 0.9073
1344/1750 [======================>.......] - ETA: 0s - loss: 0.3293 - acc: 0.9100
1750/1750 [==============================] - 0s - loss: 0.3234 - acc: 0.9103 - val_loss: 0.3920 - val_acc: 0.8800
    Epoch 5/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.1720 - acc: 0.9375
 544/1750 [========>.....................] - ETA: 0s - loss: 0.2594 - acc: 0.9301
1088/1750 [=================>............] - ETA: 0s - loss: 0.2513 - acc: 0.9311
1632/1750 [==========================>...] - ETA: 0s - loss: 0.2531 - acc: 0.9301
1750/1750 [==============================] - 0s - loss: 0.2593 - acc: 0.9286 - val_loss: 0.3679 - val_acc: 0.8933
    Epoch 6/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.0810 - acc: 1.0000
 448/1750 [======>.......................] - ETA: 0s - loss: 0.1994 - acc: 0.9509
 864/1750 [=============>................] - ETA: 0s - loss: 0.2141 - acc: 0.9479
1184/1750 [===================>..........] - ETA: 0s - loss: 0.2015 - acc: 0.9485
1664/1750 [===========================>..] - ETA: 0s - loss: 0.2069 - acc: 0.9453
1750/1750 [==============================] - 0s - loss: 0.2089 - acc: 0.9457 - val_loss: 0.3474 - val_acc: 0.8920
    Epoch 7/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.1675 - acc: 0.9688
 480/1750 [=======>......................] - ETA: 0s - loss: 0.1567 - acc: 0.9667
 800/1750 [============>.................] - ETA: 0s - loss: 0.1463 - acc: 0.9738
1088/1750 [=================>............] - ETA: 0s - loss: 0.1603 - acc: 0.9678
1344/1750 [======================>.......] - ETA: 0s - loss: 0.1720 - acc: 0.9621
1632/1750 [==========================>...] - ETA: 0s - loss: 0.1726 - acc: 0.9602
1750/1750 [==============================] - 0s - loss: 0.1718 - acc: 0.9594 - val_loss: 0.3274 - val_acc: 0.8947
    Epoch 8/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.0906 - acc: 1.0000
 320/1750 [====>.........................] - ETA: 0s - loss: 0.1458 - acc: 0.9750
 672/1750 [==========>...................] - ETA: 0s - loss: 0.1445 - acc: 0.9762
 928/1750 [==============>...............] - ETA: 0s - loss: 0.1392 - acc: 0.9731
1248/1750 [====================>.........] - ETA: 0s - loss: 0.1389 - acc: 0.9728
1728/1750 [============================>.] - ETA: 0s - loss: 0.1418 - acc: 0.9693
1750/1750 [==============================] - 0s - loss: 0.1411 - acc: 0.9697 - val_loss: 0.3225 - val_acc: 0.9040
    Epoch 9/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.0524 - acc: 1.0000
 480/1750 [=======>......................] - ETA: 0s - loss: 0.0862 - acc: 0.9896
 736/1750 [===========>..................] - ETA: 0s - loss: 0.0932 - acc: 0.9905
1216/1750 [===================>..........] - ETA: 0s - loss: 0.1075 - acc: 0.9844
1472/1750 [========================>.....] - ETA: 0s - loss: 0.1082 - acc: 0.9844
1750/1750 [==============================] - 0s - loss: 0.1145 - acc: 0.9817 - val_loss: 0.3401 - val_acc: 0.8933
    Epoch 10/10
    
  32/1750 [..............................] - ETA: 0s - loss: 0.1675 - acc: 0.9688
 384/1750 [=====>........................] - ETA: 0s - loss: 0.1180 - acc: 0.9714
 672/1750 [==========>...................] - ETA: 0s - loss: 0.1182 - acc: 0.9717
1152/1750 [==================>...........] - ETA: 0s - loss: 0.1021 - acc: 0.9792
1632/1750 [==========================>...] - ETA: 0s - loss: 0.1017 - acc: 0.9786
1750/1750 [==============================] - 0s - loss: 0.1003 - acc: 0.9789 - val_loss: 0.3132 - val_acc: 0.9027

#Congrats! You've done something pretty amazing. You should see better than 90% accuracy recognizing handwritten digits, even while using a small training set of only 1750 images