import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def auto_slice(path):
    wav, sr = librosa.load(path)
    wav, event_start_positions, event_end_positions = get_slice_positions(wav, sr)
    slices = get_audio_slices(wav, event_start_positions, event_end_positions)

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

    last_sample_position = len(wav) - 1  # for end position of last slice
    event_end_positions = event_start_positions

    event_end_positions = np.append(event_end_positions, last_sample_position)
    event_end_positions = np.delete(event_end_positions, [0])

    return wav, event_start_positions, event_end_positions


def get_audio_slices(wav, event_start_positions, event_end_positions):
    slices = []
    for position in range(event_start_positions.shape[0]):
        start = event_start_positions[position]
        stop = event_end_positions[position] - 800  # trim end point by fixed amount
        slices.append(wav[start:stop])

    return slices


def get_spectrograms(slices):
    specs = []
    for slice in slices:
        spec = np.abs(librosa.stft(slice))
        specs.append(spec)

    return specs


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
    librosa.display.waveplot(slice)
    spec = np.abs(librosa.stft(slice))
    plt.figure()
    librosa.display.specshow(librosa.amplitude_to_db(spec, ref=np.max),
                             x_axis='time', y_axis='log')
    plt.title('Power spectrogram')
    plt.show()
