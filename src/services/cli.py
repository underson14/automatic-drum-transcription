import argparse
from runtime_constants import runtime_directories


def handle_args():
    """
    Parse the given arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='Creates models to create midi files out of wav files',
                                     epilog='Accepts tsv and csv files')
    parser.add_argument('--folder', dest='folder', action='store', required=True)
    args = parser.parse_args()
    runtime_directories.ARG_FOLDER = args.folder
