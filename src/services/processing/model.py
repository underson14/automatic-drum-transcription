import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from keras.preprocessing.image import ImageDataGenerator
from services.processing import prepare_data
import numpy as np
from collections import Counter


def build_dataset(split=.7):
    """
    performs data preparaations. Split data into train/test and reshape into tensors
    """
    # init scores list for recording model performance
    X, y = prepare_data.prepare()

    #     Remove Alpha Channel from RGBA img. Not needed for grayscale
    #     X = X[:,:,:,:3]

    # split inputs into train/test sets and reshape into tensor
    train_pct_index = int(split * len(X))
    X_train, X_test = X[:train_pct_index], X[train_pct_index:]
    X_train, X_test = X_train.reshape(
        (X_train.shape[0], 224, 224, 1)), X_test.reshape((X_test.shape[0], 224, 224, 1))

    # split labels into train/test sets
    y_train, y_test = y[:train_pct_index], y[train_pct_index:]

    return X_train, X_test, y_train, y_test


def build_model(batch_size=8, epochs=10):
    """
    build and trains keras network
    """
    X_train, X_test, y_train, y_test = build_dataset()

    # define run params
    batch_size = batch_size
    num_classes = 11
    epochs = epochs

    # MODEL
    # Grayscale input layer
    model = Sequential()
    model.add(Conv2D(input_shape=(224, 224, 1), filters=32,
                     kernel_size=(12, 1), padding="same", activation="relu"))
    # RGB input layer
    # model.add(Conv2D(input_shape=(224, 224, 3), filters=16,
    #                  kernel_size=(88, 1), padding="same", activation="relu"))
    # model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))    
    # HIDDEN LAYERS
    model.add(Conv2D(filters=32, kernel_size=(12, 1),
                     padding="same", activation="relu"))
    # model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(filters=32, kernel_size=(12, 1),
                     padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(filters=32, kernel_size=(12, 1),
                     padding="same", activation="relu"))
    # model.add(Conv2D(filters=64, kernel_size=(224,3), padding="same", activation="relu"))

    # model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
    # model.add(Conv2D(filters=128, kernel_size=(224,3), padding="same", activation="relu"))

    # model.add(Conv2D(filters=128, kernel_size=(224,3), padding="same", activation="relu"))
    # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
    # model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
    # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
    # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
    # model.add(Conv2D(filters=512, kernel_size=(224,3), padding="same", activation="relu"))
    model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(Conv2D(filters=256, kernel_size=(
        224, 3), padding="same", activation="softmax"))
    # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
    # model.add(Conv2D(filters=512, kernel_size=(224,3), padding="same", activation="relu"))
    # model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
    # OUTPUT LAYER
    model.add(Flatten())
    model.add(Dense(num_classes))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])

    print(model.summary())

    # fit model to data
    model.fit(X_train, y_train,
                batch_size=batch_size,
                epochs=epochs,
                verbose=1,
                validation_data=(X_test, y_test))

    # evaluate performance on test set
    scores = []
    evalulate = model.evaluate(X_test, y_test, verbose=0)
    scores.append({'Test loss:', evalulate[0], 'Test accuracy:', evalulate[1]})

    return evalulate, scores