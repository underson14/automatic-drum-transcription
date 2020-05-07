import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
from keras.preprocessing.image import ImageDataGenerator
from services import prepare_data 
import numpy as np

def build_model(batch_size = 32, epochs = 100, split = .7):
    """
    performs data preparations, defines and trains model.
    returns model summary
    """
    scores = []

    ## read data, split into train/test
    X, y = prepare_data.prepare()
    training = prepare_data.prepare()
    train_pct_index = int(split * len(X))
    X_train, X_test = X[:train_pct_index], X[train_pct_index:]
    y_train, y_test = y[:train_pct_index], y[train_pct_index:]

#     ## define args
#     batch_size = batch_size
#     num_classes = np.unique(y)
#     epochs = epochs

#     ## define model hyperparams
#     model = Sequential()
#     model.add(Conv2D(input_shape=(224,224,3),filters=64,kernel_size=(88,3),padding="same", activation="relu"))
#     model.add(Conv2D(filters=32,kernel_size=(224,3),padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=64, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=64, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=128, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=128, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=512, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=256, kernel_size=(224,3), padding="same", activation="relu"))
#     # model.add(Conv2D(filters=512, kernel_size=(224,3), padding="same", activation="relu"))
#     model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
#     model.add(Dense(num_classes))

#     model.compile(loss=keras.losses.categorical_crossentropy,
#             optimizer=keras.optimizers.Adadelta(),
#             metrics=['accuracy'])

#     ## fit model to data
#     model.fit(X_train, y_train,
#           batch_size=batch_size,
#           epochs=epochs,
#           verbose=1,
#           validation_data=(X_test, y_test))
   
#     ## evaluate performance on test set
#     evalulate = model.evaluate(X_test, y_test, verbose=0)
#     scores.append('Test loss:', evalulate[0],'Test accuracy:', evalulate[1])

#     return evalulate, scores


    
    



