import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
# from pydub import AudioSegment
from runtime_constants import runtime_file

def transform_audio(path = None):
    """reads in a raw wav file and returns
    a melspectrogram of fixed length
    
    Returns:
        array -- melspectrogram of wav file
        image -- matplotlib image of spec
    """
    # path = runtime_file.CURRENT_EVALUATED_FILE_PATH
    path = path
    spec, sr = __get_spec(path)
    path = path
    spec, sr = __get_spec(path)
    spec = __reshape_spec(spec)
    img = __get_spec_img(spec, sr)
    img = __plot_spec(spec, sr)

    return spec, img


def __get_spec(path: str):
    """convert wav to spectrogram
    
    Arguments:
        path {path/to/wav} -- pat to wav
    
    Returns:
        array -- mel spectrogram
    """
    wav, sr = librosa.load(path, sr = None)
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


def __get_spec_img(spec: np.ndarray, sr: int):
    """takes in spec data and plots to an image.
    
    Arguments:
        spec {np.ndarray} -- spectrogram data
        sr {int} -- sample rate
    
    Returns:
        image -- image of spectrogram event
    """
    fig = plt.figure(figsize=(5, 5))
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


def _save_img(path, img: np.ndarray):
    pass

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

def __get_new_path(path: str):
    filename = os.path.basename(path)
    dir_path = os.path.dirname(os.path.abspath(path))   
    new_path = dir_path + filename
    
    return new_path

path = "C:\\Users\\Christian\\Documents\\GitHub\\automatic-drum-transcription\\data\\raw-data-test\\kick\\BK1-KICK 8.wav"
spec, img = transform_audio(path)