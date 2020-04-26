from pathlib import Path
from collections import defaultdict

# The current root directory one provided. Like /drums
CURRENT_EVALUATED_ROOT_DIRECTORY = Path()
# The current evaluated sub directory. This changes according the directory the algorithm is evaluating.
# e.g. /drums/hi-hat
CURRENT_EVALUATED_SUB_DIRECTORY = Path()
# Is a list with a key and a value. The key, is the subdirectory, the value, are all png files paths.
# Used for the training process
CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_WAV_DATA = defaultdict(list)
# This is list with subfolders as key and all files available in this subfolder as value.
# Example usage:
# for folder, files in runtime_directories.CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_PNG_DATA.items():
# folder is the single folder per iteration aka a string.
# files is a list which can be iterated again, to get every single file name
# Used example in Preprocessing.py
CURRENT_EVALUATED_ROOT_DIRECTORY_SUB_FOLDER_PNG_DATA = defaultdict(list)


# Both defaultdict variable are filled automatically. You dont have to take care about that.
