from services import config, cli, file, process_raw_data
import constants

if __name__ == '__main__':
    print("Starting...")
    config.read_conf()
    cli.handle_args()
    print(config.Config.DATA_RAW_DIRECTORY)
    print(constants.ARG_FOLDER)
    file.read_folder(constants.ARG_FOLDER)

    for file in constants.FILE_PATHS:
        spectrogram = process_raw_data.transform_audio(file)
        process_raw_data.__plot_spec(spectrogram)
    input()
    #start()
    # wave to spectrogram logic
    #
    exit(0)
