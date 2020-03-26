from services import config, cli
import constants

if __name__ == '__main__':
    print("Starting...")
    config.read_conf()
    cli.handle_args()
    print(config.Config.DATA_RAW_DIRECTORY)
    print(constants.ARG_FOLDER)
    input()
    #start()
    # wave to spectrogram logic
    #
    exit(0)
