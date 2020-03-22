from services import config

if __name__ == '__main__':
    print("Starting...")
    config.read_conf()
    print(config.Config.DATA_RAW_DIRECTORY)
    input()
    #start()
    # wave to spectrogram logic
    #
    exit(0)
