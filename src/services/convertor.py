import matplotlib.pyplot as plt
import numpy as np
import wavio
from scipy import signal
from scipy.io import wavfile
from pydub import AudioSegment
import py_midicsv
import pandas as pd
import numpy as np

'''
Transform a .mid file into a .csv label for
ADT supervised learning network
'''


def process_midi(midipath):
    """returns dataframe of midi note-on events.
    
    Arguments:
        midipath {pathto.mid} -- path to .mid file
    """
    midi_strings = py_midicsv.midi_to_csv(midipath)
    midi_csv = get_midi_csv(midi_strings)
    note_on_events = get_note_events(midi_csv)
    label, midi_start = generate_blank_label(note_on_events)
    insert_note_events(label, note_on_events, midi_start)

    return label


def get_midi_csv(midi_strings):
    """split comma seperated strings into csv file

    Arguments:
        midi_strings {list} -- list of comma separated strings

    Returns:
        csv -- midi data in csv format
    """
    midi_csv = []
    for row in midi_strings:
        midi_data = row.split(",")
        midi_csv.append(midi_data)

    return midi_csv


def get_note_events(midi_csv):
    """make list of only note-on events and truncate all other data.
    
    Arguments:
        midi_csv {csv} -- midi data in csv format
    
    Returns:
        dataframe -- data frame of note-on events 
    """
    note_on_events = []
    for event in midi_csv:
        if ('Note_on_c' in event[2]):
            note_on_events.append(event)

    note_on_events = pd.DataFrame(note_on_events,
                                  columns=['track', 'time', 'type', 'channel', 'note', 'velocity'])
    note_on_events.drop(labels=['track', 'type', 'channel'],
                        inplace=True, axis=1)
    note_on_events['note'].replace({' 36': 0, ' 38': 1, ' 42': 2},
                                   inplace=True)

    note_on_events['time'] = note_on_events['time'].str.strip().astype(int)

    return note_on_events


def generate_blank_label(note_on_events):
    """find the min and max time values. These are the times
    of the first and last hit in the pattern. Use these values
    to generate a blank label with the correct dimensions.

    Arguments:
        note_on_events {dataframe} -- dataframe of note-on events
    """
    midi_start = note_on_events['time'].min()
    midi_end = note_on_events['time'].max()

    n_timesteps = midi_end
    n_instruments = note_on_events['note'].nunique()
    label = np.zeros(shape=(n_timesteps + 1, n_instruments))

    print('first note:', midi_start, 'last note:', midi_end)
    print('timesteps:', n_timesteps, 'instruments:', n_instruments)

    return label, midi_start


def insert_note_events(label, note_on_events, midi_start=0):
    """insert the velocity of each note at time(row)
    and instrument(col) coordinates. 
    
    Arguments:
        label {array} -- empty array of correct size
        note_on_events {dataframe} -- note-on event data
        midi_start {int} -- [time of first note in seq]
    
    Returns:
        [array] -- [array to be used as label]
    """
    note_on_events = np.asarray(note_on_events)
    for event in note_on_events:
        # position = int(event[0]) - midi_start
        position = event[0]
        note = event[1]
        velocity = event[2]
        label[position][note] = velocity


# label = process_midi(".\\data_mini\\rock beat 2\\rock beat 2 label.mid")
rb1 = process_midi(".\\drum-data-mvp\\rb1.mid")
rb2 = process_midi(".\\drum-data-mvp\\rb2.mid")

np.savetxt("drum-data-mvp\\rb1.csv", rb1, delimiter=',')
np.savetxt("drum-data-mvp\\rb2.csv", rb2, delimiter=',')





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