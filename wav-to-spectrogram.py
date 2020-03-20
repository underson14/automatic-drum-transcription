import matplotlib.pyplot as plt
import numpy as np
import wavio
from scipy import signal
from scipy.io import wavfile
from pydub import AudioSegment
# %matplotlib inline


# convert file to mono  
sound = AudioSegment.from_wav('.\\drum-data-mvp\\rb1.1.wav')
sound = sound.set_channels(1)
sound.export('.\\drum-data-mvp\\rb1.1mono.wav', format="wav")

# load wav with wavio
wav = wavio.read('.\\drum-data-mvp\\rb1.1mono.wav')

# use scipy to generate spectrogram
sample_rate, samples = wavfile.read('.\\drum-data-mvp\\rb1.1mono.wav')
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)


plt.pcolormesh(times, frequencies, np.log(spectrogram))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

np.savetxt('.\\drum-data-mvp\\rb1.1.spec.csv', spectrogram.transpose(), delimiter = ',')


spectrogram.transpose().shape