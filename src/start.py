from services import config, cli, file, process_raw_data
from runtime_constants import runtime_directories

if __name__ == '__main__':
    print("Starting...")
    config.read_conf()
    cli.handle_args()
    print(config.Config.DATA_RAW_DIRECTORY)
    print(runtime_directories.ARG_FOLDER)
    file.read_folder(runtime_directories.ARG_FOLDER)

    for file in runtime_directories.FILE_PATHS:
        spectrogram = process_raw_data.transform_audio(file)
        process_raw_data.__plot_spec(spectrogram)
    input()
    #start()
    # wave to spectrogram logic
    #
    exit(0)
