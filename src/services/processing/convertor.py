import matplotlib.pyplot as plt
import numpy as np
import wavio
from scipy import signal
from scipy.io import wavfile
from pydub import AudioSegment
import py_midicsv
import pandas as pd
import numpy as np
import librosa

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
    midi_csv = __get_midi_csv(midi_strings)
    note_on_events = __get_note_events(midi_csv)
    conversion_factor = __get_conversion_factor(midi_csv)
    note_on_events = __calc_absolute_times(note_on_events, conversion_factor)
    label, midi_start = __generate_blank_label(note_on_events)
    abs_label = __generate_absolute_label(note_on_events)
    __insert_abs_events(abs_label, note_on_events)
    __insert_note_events(label, note_on_events, midi_start)

    return abs_label


def __get_midi_csv(midi_strings):
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


def __get_note_events(midi_csv):
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


def __generate_blank_label(note_on_events):
    """find the min and max time values. These are the times
    of the first and last hit in the pattern. Use these values
    to generate a blank label with the correct dimensions.
    Arguments:
        note_on_events {dataframe} -- dataframe of note-on events
    """
    midi_start = 0
    midi_end = note_on_events['time'].max()
    n_timesteps = midi_end 
    n_instruments = note_on_events['note'].nunique()
    label = np.zeros(shape=(n_timesteps + 1, n_instruments))

    print('first note:', midi_start, 'last note:', midi_end)
    print('timesteps:', n_timesteps, 'instruments:', n_instruments)

    return label, midi_start


def __generate_absolute_label(note_on_events):
    """find the min and max time values. These are the times
    of the first and last hit in the pattern. Use these values
    to generate a blank label with the correct dimensions.
    Arguments:
        note_on_events {dataframe} -- dataframe of note-on events
    """
    midi_start = 0
    last_note_position = note_on_events['abs_time'].max()

    n_timesteps = last_note_position 
    n_instruments = note_on_events['note'].nunique()
    abs_label = np.zeros(shape=(n_timesteps + 1, n_instruments))

    print('first note:', midi_start, 'last note:', last_note_position)
    print('timesteps:', n_timesteps, 'instruments:', n_instruments)

    return abs_label


def __insert_note_events(label, note_on_events, midi_start=0):
    """insert the velocity of each note at time(row)
    and instrument(col) coordinates. 
    
    Arguments:
        label {array} -- empty array of correct size
        note_on_events {dataframe} -- note-on event data
        midi_start {int} -- time of first note in seq
    
    Returns:
        array -- array to be used as label
    """
    note_on_events = np.asarray(note_on_events)
    for event in note_on_events:
        position = event[0] # note event in midi ticks
        note = event[1] # midi note number
        velocity = event[2]
        label[position][note] = velocity


def __insert_abs_events(abs_label, note_on_events, midi_start=0):
    """insert the velocity of each note at time(row)
    and instrument(col) coordinates. 
    
    Arguments:
        label {array} -- empty array of correct size
        note_on_events {dataframe} -- note-on event data
        midi_start {int} -- [time of first note in seq]
    
    Returns:
        array -- array to be used as label
    """
    note_on_events = np.asarray(note_on_events)
    for event in note_on_events:
        position = event[3] # absolute position in time
        note = event[1] # midi note number
        velocity = event[2]
        abs_label[position][note] = velocity


def __get_conversion_factor(midi_csv):
    """compute conversion factor for finding microseconds per 
    midi tick.
    
    Arguments:
        midi_csv {array} -- full midi data
    
    Returns:
        int -- factor used for calculation
    """
    resolution = int(midi_csv[0][5]) # pulses/quarter beat
    tempo = int(midi_csv[7][3]) # ms/quarter beat
    conversion_factor = round(tempo/resolution) 

    return conversion_factor


def __calc_absolute_times(note_on_events, conversion_factor):
    """calculates the absolute time of a midi event. Returns 
    a dataframe that includes the event times in microseconds.
    
    Arguments:
        note_on_events {dataframe} -- note event data
        conversion_factor {numeric} -- factor to convert to microsecs
    
    Returns:
        dataframe -- dataframe with added abs time columns
    """
    note_on_events['abs_time'] = note_on_events.time * conversion_factor
    
    return note_on_events


# label = process_midi(".\\data_mini\\rock beat 2\\rock beat 2 label.mid")
midi_path = "C:\\Users\\Christian\\Documents\\GitHub\\automatic-drum-transcription\\data\\drum-data-mvp\\rb1.mid"
audio_path = "C:\\Users\\Christian\\Documents\\GitHub\\automatic-drum-transcription\\data\\drum-data-mvp\\rb1.1.wav"
rb1 = process_midi(midi_path)

# export abs_label as csv
np.savetxt("drum-data-mvp\\rb1.csv", rb1, delimiter=',')
np.savetxt("drum-data-mvp\\rb2.csv", rb2, delimiter=',')

# convert file to mono  
sound = AudioSegment.from_wav('.\\drum-data-mvp\\rb1.1.wav')
sound = sound.set_channels(1)
sound.export('.\\drum-data-mvp\\rb1.1mono.wav', format="wav"

np.savetxt('.\\drum-data-mvp\\rb1.1.spec.csv', spectrogram.transpose(), delimiter = ',')
spectrogram.transpose().shape
