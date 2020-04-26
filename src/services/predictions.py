# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
# from keras.preprocessing.image import ImageDataGenerator
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np
from runtime_constants import runtime_file, runtime_directories
from services import fileservice
from pathlib import Path

def prepare_data():  
    training_data = []
    class_num = 0
    print('Preparing training data')
    for folder, files in runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_PNG_DATA.items(): 
        try:
            print(f"Preparing sub directory {folder}.")
            for file in files:
                try:
                    runtime_file.CURRENT_EVALUATED_FILE_PATH = Path.joinpath(
                        runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY, folder, file)
                    img_array = cv2.imread(runtime_file.CURRENT_EVALUATED_FILE_PATH)
                    training_data.append([img_array,class_num])
                    print(f'Sucessfully prepared {file}.')
                except:
                    print(f'could not perpare file {file}')
                    
            class_num += 1
        except:
            print(f'could not prepare folder {folder}')

    # np.random.shuffle(training_data)            
    
    # X = [] 
    # y = []

    # for features, labels in training_data:
    #     X.append(features)
    #     y.append(labels)
    
    # return X, y
 

# def build_model():
#     model = Sequential()
#     model.add(Conv2D(input_shape=(224,224,3),filters=64,kernel_size=(88,3),padding="same", activation="relu"))
#     model.add(Conv2D(filters=32,kernel_size=(88,3),padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=64, kernel_size=(88,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=64, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=128, kernel_size=(88,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=128, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=256, kernel_size=(88,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=512, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=256, kernel_size=(88,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=512, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))

#     return model

# X, y = prepare_data(DATADIR)
# model = build_model()


# model.summary()