import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
# from pydub import AudioSegment
from runtime_constants import runtime_file, runtime_directories
from services import fileservice


def transform_audio():
    """reads in a raw wav file and returns
    a melspectrogram of fixed length
    
    Returns:
        array -- melspectrogram of wav file
        image -- matplotlib image of spec
    """
    path = runtime_file.CURRENT_EVALUATED_FILE_PATH
    spec, sr = __get_spec(path)
    spec = __reshape_spec(spec)
    fig = __get_spec_fig(spec, sr)
    # new_path = __get_new_path(path)
    # plot_spec() for testing only
    # fig = __plot_spec(spec, sr)
    __save_fig(path, fig)


def __get_spec(path: str):
    """convert wav to spectrogram
    
    Arguments:
        path {path/to/wav} -- pat to wav
    
    Returns:
        array -- mel spectrogram
    """
    wav, sr = librosa.load(path, sr=None)
    spec = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=88,
                                          fmax=20000)

    return spec, sr


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


def __get_spec_fig(spec: np.ndarray, sr: int):
    """takes in spec data and plots to an image.
    
    Arguments:
        spec {np.ndarray} -- spectrogram data
        sr {int} -- sample rate
    
    Returns:
        image -- image of spectrogram event
    """
    fig = plt.figure(figsize=(2.34, 2.34))
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.legend('', frameon=False)

    spec_db = librosa.power_to_db(spec, ref=np.max)
    librosa.display.specshow(spec_db, x_axis='time',
                             y_axis='mel', sr=sr,
                             fmax=20000)
    plt.tight_layout()

    return fig


def __plot_spec(spec: np.ndarray, sr: int):
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


def __save_fig(file: str, fig):
    fig.savefig(fileservice.get_file_name(file), bbox_inches='tight')
    plt.close(fig)
