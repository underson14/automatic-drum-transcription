from runtime_constants import runtime_directories, runtime_file
from pathlib import Path
from services.processing import process_raw_data
from services.configuration.config import Config

def create_png_files():
    """
    Creates png files from wav files
    Returns:

    """
    for folder, files in runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_WAV_DATA.items():
        try:
            print(f"Evaluating sub directory {folder}.")
            for file in files:
                try:
                    runtime_file.CURRENT_EVALUATED_FILE_PATH = Path.joinpath(
                        Config.ROOT_FOLDER, folder, file)
                    runtime_directories.CURRENT_EVALUATED_SUB_DIRECTORY = folder
                    process_raw_data.transform_audio()
                    print(f"File {file} successfully processed!")
                except BaseException as ex:
                    print(ex)
                    print(f"Could not process file {file}.")
                    continue

        except BaseException as ex:
            print(ex)
            print(f"Could not process subfolder {folder}.")
            continue
