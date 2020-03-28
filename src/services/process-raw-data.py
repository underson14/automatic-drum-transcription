import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def transform_audio(path: str):
    """takes in a raw wav file and returns
    a melspectrogram of fixed length
    
    Arguments:
        path {path/to/wav} -- path to wav
    
    Returns:
        array -- melspectrogram of wav file
    """
    spec = __get_spectrogram(path)
    spec =__reshape_spec(spec)

    return spec
    
def __get_spectrogram(path: str):
    """convert wav to spectrogram
    
    Arguments:
        path {path/to/wav} -- pat to wav
    
    Returns:
        array -- mel spectrogram
    """
    wav, sr = librosa.load(path)
    spec = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=166,
                                   fmax=20000)

    return spec

def __reshape_spec(spec: np.ndarray, t = 1.5):
    """reshape mel spectrogram to have fixed
    length t. Either truncate at cutoff if too long
    or add silence if too short.
    
    Arguments:
        spec {array} -- mel spectrogram
    
    Keyword Arguments:
        t {float} -- sample length (default: {1.5})
    
    Returns:
        array -- fixed length mel spectrogram
    """
    cutoff = librosa.time_to_frames(t)
    last_frame = len(spec[1])
    if cutoff < last_frame:
        spec = np.delete(spec,slice(cutoff,last_frame),1)
    elif cutoff > last_frame:
        spec = np.pad(spec,((0,0),(0,cutoff)))
    else:
        pass   
    
    return spec
    
def __plot_spec(spec: np.ndarray):
    """plots for testing purposes.
    
    Arguments:
        spec {array} -- mel spectrogram
    """
    plt.figure(figsize=(10, 4))
    S_dB = librosa.power_to_db(spec, ref=np.max)
    librosa.display.specshow(S_dB, x_axis='time',
                            y_axis='mel', sr=sr,
                            fmax=20000)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout() 


path = "C:\\Users\\Christian\\Documents\\GitHub\\automatic-drum-transcription\\data\\drum-data-mvp\\rb1.1.wav"
spec = transform_audio(path)
wav, sr = librosa.load(path)
__plot_spec(spec)