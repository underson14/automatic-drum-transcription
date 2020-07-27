import argparse
from services.configuration.config import Config
from pathlib import Path


def handle_args():
    """
    Parse the given arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='Creates models to create midi files out of wav files',
                                     epilog='Accepts tsv and csv files')
    parser.add_argument('--folder', dest='folder', action='store', required=True, type=Path)
    args = parser.parse_args()

    Config.ROOT_FOLDER = args.folder
