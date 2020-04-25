# import keras
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np

DATADIR = 'D:\\raw-drum-data\\raw-data'
CATEGORIES = ['hihat-closed', 'hihat-open', 'kick', 'snare']
# model = keras.applications.resnet_v2.ResNet50V2(include_top=False, weights='imagenet', input_tensor=None, input_shape=(224, 224, 3), pooling=None, classes=4) 

training_data = []

def prepare_data(dir: str):
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        
        for img in os.listdir(path):
            print(img)
            name, ext = os.path.splitext(img)
            if ext == '.png':
                img_array = cv2.imread(os.path.join(path, img))
                training_data.append([img_array,class_num])
                
    X = [] 
    y = []

    for features, labels in training_data:
        X.append(features)
        y.append(labels)

    return X, y

