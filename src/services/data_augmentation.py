from pydub import AudioSegment

def __get_multiclass_wav(path: str, path2: str):
    wav1 = AudioSegment.from_file(path)
    wav2 = AudioSegment.from_file(path2)

    combined = wav1.overlay(wav2)

    combined.export("/path/to/combined.wav", format='wav')


def __select_wavs(directory: list):
    # randomly select two wavs of different class type.
    # assign discrete probabilty of class selection to reflect
    # prevalance. 
    pass