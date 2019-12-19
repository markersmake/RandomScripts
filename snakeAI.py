from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os, cv2, pickle
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

#Base directory
spectacled_cobra_dir = "D:/Users/bmag2/Documents/Python/Indian-Snakes-Dataset-master/Indian-Snakes-Dataset-master/Venomous/"
#Folders/categories of our images
categories           = ["Spectacled Cobra", "Russell's Viper"]
trainingData         = []
IMG_SIZE             = 200

def createTrainingData():
    #This function is used to create the training data that will later be used in our CNN
    for category in categories:
        #Links the base directory to folders with different types snakes specified
        path     = os.path.join(spectacled_cobra_dir, category)
        classNum = categories.index(category)
        
        for img in os.listdir(path):
            #Converts all images to grayscale and resizes them for processing later
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                newArray  = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                trainingData.append([newArray, classNum])
            except Exception as e:
                pass

    # Save the dataset        
    print("Beginning saving function.")
    x = []
    y = []
    for features, label in trainingData:
        x.append(features)
        y.append(label)
    print(x[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))
    x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    #using pickle package, saves both X and Y for our data set where x is the image and y the label
    pickle_out = open("x.pickle", "wb")
    pickle.dump(x, pickle_out)
    pickle_out.close()
    pickle_out = open("y.pickle", "wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

def neuralNet():

    #load previously saved datasets
    pickle_in = open("x.pickle", "rb")
    X = pickle.load(open("x.pickle", "rb"))
    pickle_in = open("y.pickle", "rb")
    Y = pickle.load(open("x.pickle", "rb"))
    X = X/255.0

    model = Sequential()
    model.add(Conv2D(256,(3,3), input_shape = X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(256,(3,3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation("relu"))

    model.add(Dense(1))
    model.add(Activation("sigmoid"))
    
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="adam",
                  metrics=['accuracy'])
    model.fit(X,Y, batch_size=32,validation_split=0.3)
    
createTrainingData()
neuralNet()
