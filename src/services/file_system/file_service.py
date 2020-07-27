import os
from runtime_constants import runtime_directories
from services.configuration.config import Config
import pandas as pd
from pathlib import Path


def gather_wav_files():
    """
    Initiate the dictionary for wav files per sub directory
    Returns:

    """
    for root, dirs, files in os.walk(Config.ROOT_FOLDER):
        for sub_folder in dirs:
            runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_WAV_DATA[
                sub_folder] = wav_files_per_sub(sub_folder)


def gather_png_files():
    """
      Initiate the dictionary for png files per sub directory
    Returns:

    """
    for root, dirs, files in os.walk(Config.ROOT_FOLDER):
        for sub_folder in dirs:
            runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_PNG_DATA[
                sub_folder] = png_files_per_sub(sub_folder)


def wav_files_per_sub(sub_directory_path: str):
    """
    Get all file names from the given folder. Used to save memory and later iterate through the matching files
    Args:
        sub_directory_path:

    Returns:

    """
    try:
        path = Path(f"{Config.ROOT_FOLDER}/{sub_directory_path}")
        files = []
        for file in os.listdir(path):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                files.append(file)
            else:
                continue

        return files
    except BaseException as ex:
        print('Error in wav_files_per_sub')
        print(ex)


def png_files_per_sub(sub_directory_path: str):
    """
      Get all file names from the given folder. Used to save memory and later iterate through the matching files
    Args:
        sub_directory_path:

    Returns:

    """
    try:
        path = Path(f"{Config.ROOT_FOLDER}/{sub_directory_path}")
        files = []
        for file in os.listdir(path):
            filename = os.fsdecode(file)
            if filename.endswith(".png"):
                files.append(file)
            else:
                continue

        return files
    except BaseException as ex:
        print('Error in png_files_per_sub')
        print(ex)


def write_file(path: str):
    pass


def read_file(path: str):
    """
    Reads the content of a file and return the data set
    Args:
        path:

    Returns:

    """
    try:
        path = Path.joinpath(Config.ROOT_FOLDER, path)
        print(path)
        df = pd.read_csv(path)
        return df

    except BaseException as ex:
        print("error in read_file")
        print(ex)


def get_file_name(file_path: str):
    return os.path.splitext(file_path)[0]
