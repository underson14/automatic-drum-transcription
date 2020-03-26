import argparse
import constants


def handle_args():
    """
    Parse the given arguments
    :return:
    """
    parser = argparse.ArgumentParser(description='Creates models to create midi files out of wav files',
                                     epilog='Accepts tsv and csv files')
    parser.add_argument('--folder', dest='folder', action='store', required=True)
    args = parser.parse_args()
    constants.ARG_FOLDER = args.folder
