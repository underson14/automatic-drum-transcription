import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def prepare_data(path):
    wav, sr = librosa.load(path)
    wav, event_start_positions, event_end_positions = get_slice_positions(wav, sr)
    slices = get_audio_slices(wav,event_start_positions, event_end_positions)
    specs = get_spectrograms(slices, sr)
    specs = reshape_specs(specs)

    return specs

def auto_slice(path):
    wav, sr = librosa.load(path)
    wav, event_start_positions, event_end_positions = get_slice_positions(wav, sr)
    slices = get_audio_slices(wav,event_start_positions, event_end_positions)

    return slices

def get_slice_positions(wav, sr):
    """automatically detects peaks in wav and chops it into 
    individual note events"
    
    Arguments:
        wav {wav} -- drum loop
        sr {numeric} -- sampling rate of wav file
    """
    onset_frames = librosa.onset.onset_detect(wav, sr=sr)
    event_start_positions = librosa.frames_to_samples(onset_frames)
    # event_start_positions = event_start_positions.reshape((len(event_start_positions),1))
    
    last_sample_position = len(wav)-1 # for end position of last slice
    event_end_positions = event_start_positions
    
    event_end_positions = np.append(event_end_positions, last_sample_position)
    event_end_positions = np.delete(event_end_positions,[0])

    return wav, event_start_positions, event_end_positions


def get_audio_slices(wav, event_start_positions, event_end_positions):
    slices = []
    for position in range(event_start_positions.shape[0]):
        start = event_start_positions[position]
        stop = event_end_positions[position] - 800 # trim end point by fixed amount
        slices.append(wav[start:stop])

    return slices


def get_spectrograms(slices, sr):
    specs = []
    for slice in slices:
        spec = librosa.feature.melspectrogram(y=slice, sr=sr, n_mels=88,
                                   fmax=20000)
        specs.append(spec)

    return specs

def reshape_specs(specs):
    reshaped = []
    for spec in specs:
        spec = __reshape_spec(spec)
        reshaped.append(spec)

    return reshaped

def __reshape_spec(spec, t = 1):
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
        spec = np.pad(spec,((0,0),(0,cutoff-last_frame)))
    else:
        pass   

    print(cutoff, spec.shape)
    
    return spec


def plot_slices(path):
    wav, sr = librosa.load(path)
    librosa.display.waveplot(wav)
    o_env = librosa.onset.onset_strength(wav, sr=sr)
    times = librosa.times_like(o_env, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)
    D = np.abs(librosa.stft(wav))
    plt.figure()
    ax1 = plt.subplot(2, 1, 1)
    librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max),
                            x_axis='time', y_axis='log')
    plt.title('Power Spectrogram')
    plt.subplot(2, 1, 2, sharex=ax1)
    plt.plot(times, o_env, label='Onset strength')
    plt.vlines(times[onset_frames], 0, o_env.max(), color='r', alpha=0.9,
            linestyle='--', label='Onsets')
    plt.axis('tight')
    plt.legend(frameon=True, framealpha=0.75)
    plt.show()


def plot_slice(slice):
    # librosa.display.waveplot(slice)
    # spec = np.abs(librosa.stft(slice))
    plt.figure()
    librosa.display.specshow(librosa.amplitude_to_db(ref=np.max, S = slice),
                            x_axis='time', y_axis='log')
    plt.title('Power spectrogram')
    plt.show()

path = "C:\\Users\\Christian\\Documents\\GitHub\\automatic-drum-transcription\\data\\drum-data-mvp\\rb2.3.wav"
# wav, sr = librosa.load(path)
# slices = auto_slice(path)
plot_slices(path)
slices = prepare_data(path)

for slice in slices:
    print(slice.shape)