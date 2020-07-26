from services import config, cli, fileservice, process_raw_data
import os
from services import PreProcessing, prepare_data, model
import sys
import signal

dirname = os.path.dirname(__file__)


def signal_handler(sig, frame):
    print('Shutting down gracefully!')
    print("Deleting working directory")
    print("Done")
    print("Bye")
    raise SystemExit


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    cli.handle_args()
    config.read_conf()

    # Gather all png files for all subfolders in root directory
    fileservice.gather_wav_files()

    if config.Config.CONVERT_TO_PNG:
        PreProcessing.create_png_files()

    # Gather all png files for the root directory and all included subfolders
    fileservice.gather_png_files()
    # All png file names loaded, sorted per subfolder. Use at will^^

    # png to array 
    # prepare_data.prepare()
    # model.build_datasets()
    model.build_model()
    exit(0)
