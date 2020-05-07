import os
import imageio
from matplotlib import pyplot as plt
import numpy as np
from runtime_constants import runtime_file, runtime_directories
from services import fileservice
from pathlib import Path

def prepare():
    """
    converts .png files into numpy arrays. Prepares 
    returns: features, label tuple
    """
    training_data = []

    print('Preparing training data')
    for folder, files in runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_PNG_DATA.items(): 
        try:
            print(f"Preparing sub directory {folder}.")
            class_num = 0
            for file in files:
                print('isFile:', os.path.isfile(runtime_file.CURRENT_EVALUATED_FILE_PATH))
                try:
                    runtime_file.CURRENT_EVALUATED_FILE_PATH = Path.joinpath(
                        runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY, folder, file)

                    img_array = imageio.imread(r'runtime_file.CURRENT_EVALUATED_FILE_PATH')
                    training_data.append([img_array,class_num])
                    print(img_array)
                    print(f'Sucessfully prepared {file}.')
                except:
                    print(f'could not prepare file {file}')
                    
            class_num += 1
        except:
            print(f'could not prepare folder {folder}')
    

    try:
        np.random.shuffle(training_data)            
        
        X = [] 
        y = []

        for features, labels in training_data:
            X.append(features)
            y.append(labels)
        
        print('Sucessfully prepared dataset')
        print('X:', len(X), 'y:', len(y))
        
        return X, y

    except:
        print('Could not prepare dataset')


