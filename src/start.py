from services import config, cli, file, process_raw_data
from runtime_constants import runtime_directories, cli_args, runtime_file
import os

dirname = os.path.dirname(__file__)
from pathlib import Path

if __name__ == '__main__':
    print("Starting...")
    cli.handle_args()
    config.read_conf()
    file.get_file_names_from_folder(cli_args.CLI_ARG_FOLDER)
    for file in runtime_directories.FILE_PATHS:
        runtime_file.CURRENT_EVALUATED_FILE_PATH = Path.joinpath(cli_args.CLI_ARG_FOLDER, file)
        print(runtime_file.CURRENT_EVALUATED_FILE_PATH)
        print(str(cli_args.CLI_ARG_FOLDER))
        process_raw_data.transform_audio()
    input()
    # wave to spectrogram logic
    #
    exit(0)
