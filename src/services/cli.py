import argparse
from runtime_constants import cli_args
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
    cli_args.CLI_ARG_FOLDER = args.folder
