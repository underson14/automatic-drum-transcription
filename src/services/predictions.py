# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
# from keras.preprocessing.image import ImageDataGenerator
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

DATADIR = 'D:\\raw-drum-data\\raw-data'
CATEGORIES = ['hihat-closed', 'hihat-open', 'kick', 'snare']

def prepare_data(dir: str):
    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        
        for img in os.listdir(path)[0:10]:
            name, ext = os.path.splitext(img)
            if ext == '.png':
                img_array = cv2.imread(os.path.join(path, img))
                training_data.append([img_array,class_num])

    np.random.shuffle(training_data)            
    
    X = [] 
    y = []

    for features, labels in training_data:
        X.append(features)
        y.append(labels)
    
    return X, y


 
# def build_model():
#     model = Sequential()
#     model.add(Conv2D(input_shape=(224,224,3),filters=64,kernel_size=(3,3),padding="same", activation="relu"))
#     model.add(Conv2D(filters=64,kernel_size=(3,3),padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))

#     return model


X, y = prepare_data(DATADIR)
# model = build_model()