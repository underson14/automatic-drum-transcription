import os
import imageio
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from runtime_constants import runtime_file, runtime_directories
from services.file_system import file_service
from pathlib import Path
from PIL import Image
from skimage import color
from skimage import io
from services.configuration.config import Config


def prepare():
    """
    converts .png files into numpy arrays. Prepares 
    returns: features, label tuple
    """
    dataset = []

    print('Preparing training data')
    label = 0
    for folder, files in runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_PNG_DATA.items():
        try:
            print(f"Preparing sub directory {folder}.")
            for file in files:
                print('isFile:', os.path.isfile(runtime_file.CURRENT_EVALUATED_FILE_PATH))
                try:
                    runtime_file.CURRENT_EVALUATED_FILE_PATH = Path.joinpath(
                        Config.ROOT_FOLDER, folder, file)

                    # using imageio to read in RGBA img data
                    # img_array = imageio.imread(runtime_file.CURRENT_EVALUATED_FILE_PATH)
                    # dataset.append([img_array,class_num])

                    # use skimage to read in Grayscale img data
                    img_array = color.rgb2gray(io.imread(runtime_file.CURRENT_EVALUATED_FILE_PATH))
                    dataset.append([img_array, label])

                    # print('img array:', img_array)
                    # print('array shape:', img_array.shape)
                    print(f'Sucessfully prepared {file}.')
                except:
                    print(f'could not prepare file {file}')

            label += 1
        except:
            print(f'could not prepare folder {folder}')

    try:
        # randomize data order
        np.random.shuffle(dataset)

        img_arrays = []
        labels = []

        for img_array, label in dataset:
            img_arrays.append(img_array)
            labels.append(label)

        print('Sucessfully prepared dataset')
        print('X:', len(img_arrays), 'y:', len(labels))

        # convert list objects to np array
        img_arrays = np.asarray(img_arrays)
        labels = np.asarray(labels)

        # convert integer labels to one-hot-encoded variables
        y_df = pd.Series(labels)
        y_df = pd.get_dummies(y_df)
        labels = np.asarray(y_df)

        return img_arrays, labels

    except:
        print('Could not prepare dataset')
