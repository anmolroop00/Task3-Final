#!/usr/bin/env python
# coding: utf-8
import os
from keras.datasets import mnist
dataset = mnist.load_data('mymnist.db')
train , test = dataset
X_train , y_train = train
X_test , y_test = test
X_train= X_train.reshape(-1 , 28*28)
X_test= X_test.reshape(-1 , 28*28)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
from keras.utils.np_utils import to_categorical
y_train = to_categorical(y_train)
y_train
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units=512, input_dim=28*28, activation='relu'))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
model.summary()
from keras.optimizers import Adam
model.compile(optimizer=Adam(), loss='categorical_crossentropy', 
             metrics=['accuracy']
             )
epoch=5
model_fit = model.fit(X_train, y_train_cat, epochs=epoch)
text = model_fi.history
for i in range(epoch):
    accuracy = text['accuracy'][i] * 100
    accuracy = int(accuracy)

f = open("accuracy.txt","w+")
f.write(str(accuracy))
f.close()
os.system("mv /accuracy.txt /root/")
