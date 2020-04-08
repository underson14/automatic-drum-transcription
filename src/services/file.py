import os
from runtime_constants import runtime_directories, cli_args
import pandas as pd
from pathlib import Path


def get_file_names_from_folder(path: str):
    try:
        path = Path(f"{path}")
        data_frames = dict()
        for file in os.listdir(path):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                runtime_directories.FILE_PATHS.append(filename)
                continue
            else:
                continue

        return data_frames
    except BaseException as ex:
        print('Error in get_file_names_from_folder')
        print(ex)


def read_file(path: str):
    try:
        path = Path.joinpath(cli_args.CLI_ARG_FOLDER, path)
        print(path)
        df = pd.read_csv(path)
        return df

    except BaseException as ex:
        print("error in read_file")
        print(ex)
