import configparser
import sys
import os


# Config.py
class Config:
    VERBOSE = 0
    DEBUG = 0
    DATA_RESULTS_DIRECTORY = ''
    CONVERT_TO_PNG = False


def read_conf():
    """
    Reads the Config.ini File, and stores the values into the Config Class
    :return:
    """
    config = configparser.ConfigParser()
    config.read('src/config.ini')
    try:
        Config.DATA_RESULTS_DIRECTORY = config['DATA']['results_directory']
        Config.CONVERT_TO_PNG = bool(config['GENERAL']['convert_to_png'])

        validate_config()
        return True
    except KeyError as ex:
        print(f"Config Error occurred for key: {ex}")
        print(f"Stopping application.")
        sys.exit()


def reset_config():
    """
    Resets the Config File. In fact the Config.ini file will be rewritten in total.
    :return:
    """
    config = configparser.ConfigParser()
    config['DATA'] = {
        'data_root_directory': 'Data/',
        'data_raw_directory': 'Data/Raw',
        'data_results_directory': 'Data/Results'
    }
    with open('Config.ini', 'w') as configfile:
        try:
            config.write(configfile)
            configfile.close()
            return True
        except FileNotFoundError as ex:
            return ex


def validate_config():
    print("Validation configuration")
    if not Config.DATA_RESULTS_DIRECTORY:
        print("Please specify a valid Results directory")
        sys.exit()

    if not Config.CONVERT_TO_PNG:
        print("Please specify a valid Raw data directory!")
        sys.exit()

    # if not os.path.exists(Config.DATA_RAW_DIRECTORY):
    #   print("Could not find ")

    # if not Config.DATA_ROOT_DIRECTORY:
    #   print("Please specify a valid Root Directory!")
    #  sys.exit()

    print("Configuration validated!")

    # if not Config.FILE_MEMORY_VAR_SUMMARY:
    # print(f"Please specify a valid name for FILE_MEMORY_VAR_SUMMARY ")
    # sys.exit()

    # if not Config.FILE_MEMORY_MEAN_SUMMARY:
    # print(f"Please specify a valid name for FILE_MEMORY_MEAN_SUMMARY")
    # sys.exit()

    # if not Config.FILE_RUNTIME_VAR_SUMMARY:
    # print(f"Please specify a valid name for FILE_RUNTIME_VAR_SUMMARY")
    # sys.exit()

    # if not Config.FILE_RUNTIME_MEAN_SUMMARY:
    # print(f"Please specify a valid name for FILE_RUNTIME_MEAN_SUMMARY")
    # sys.exit()
