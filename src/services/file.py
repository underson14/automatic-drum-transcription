from pathlib import Path
import os


def read_folder(path: str):
    try:
        directory = os.fsencode(path)
        data_frames = dict()
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                print(file)
                continue
            else:
                continue

        return data_frames
    except BaseException as ex:
        print(ex)

