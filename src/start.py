from services.configuration import config, argument_parser
import os
from services.processing import pre_processing, prepare_data, model, process_raw_data
from services.file_system import file_service
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
    argument_parser.handle_args()
    config.read_conf()

    # Gather all png files for all subfolders in root directory
    file_service.gather_wav_files()

    if config.Config.CONVERT_TO_PNG:
        pre_processing.create_png_files()

    # Gather all png files for the root directory and all included subfolders
    file_service.gather_png_files()
    # All png file names loaded, sorted per subfolder. Use at will^^

    # png to array 
    # prepare_data.prepare()
    # model.build_datasets()
    model.build_model()
    exit(0)
