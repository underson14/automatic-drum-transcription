import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from runtime_constants import runtime_file


def transform_audio():
    """takes in a raw wav file and returns
    a melspectrogram of fixed length
    
    Arguments:
        path {path/to/wav} -- path to wav
    
    Returns:
        array -- melspectrogram of wav file
    """
    spec = __get_spectrogram()
    spec = __reshape_spec(spec)

    return spec


def __get_spectrogram():
    """convert wav to spectrogram
    
    Arguments:
        path {path/to/wav} -- pat to wav
    
    Returns:
        array -- mel spectrogram
    """
    wav, sr = librosa.load(runtime_file.CURRENT_EVALUATED_FILE_PATH)
    spec = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=166,
                                          fmax=20000)

    return spec


def __reshape_spec(spec: np.ndarray, time=1.5):
    """reshape mel spectrogram to have fixed
    length t. Either truncate at cutoff if too long
    or add silence if too short.
    
    Arguments:
        spec {array} -- mel spectrogram
    
    Keyword Arguments:
        time {float} -- sample length (default: {1.5})
    
    Returns:
        array -- fixed length mel spectrogram
    """
    cutoff = librosa.time_to_frames(time)
    last_frame = len(spec[1])
    if cutoff < last_frame:
        spec = np.delete(spec, slice(cutoff, last_frame), 1)
    elif cutoff > last_frame:
        spec = np.pad(spec, ((0, 0), (0, cutoff)))
    else:
        pass

    return spec


def __melspec_to_jpg(spec: np.ndarray):
    # export plot as jpg
    # plt.interactive(False)
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.legend('', frameon=False)

    spec_dB = librosa.power_to_db(spec, ref=np.max)
    librosa.display.specshow(spec_dB, x_axis='time',
                             y_axis='mel', sr=sr,
                             fmax=20000)
    plt.tight_layout()
    # plt.close()    
    # fig.clf()
    # plt.close(fig)
    # plt.close('all')
    # del fig, ax, spec_dB

    return fig


def __get_file_name(path):
    # use path to retrieve string for filename
    # return name, target_path
    # filename  = '/path/to/dir/' + name + '.jpg'
    pass


def __plot_spec(spec: np.ndarray):
    """plots for testing purposes.
    
    Arguments:
        spec {array} -- mel spectrogram
    """
    fig = plt.figure(figsize=(10, 10))
    spec_dB = librosa.power_to_db(spec, ref=np.max)
    librosa.display.specshow(spec_dB, x_axis='time',
                             y_axis='mel', sr=sr,
                             fmax=20000)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')

    return fig


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
