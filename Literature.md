#### Automatic Music Transcription: An Overview
Great discussion of SOTA(2019) techniques and challeges for this task. Very useful!
http://www.eecs.qmul.ac.uk/~ewerts/publications/2019_BenetosDixonDuanEwert_AutomaticMusicTranscription_IEEE-SPM.pdf

#### AMT Example CNN and libraries
Example of auto music transcription for polyphonic piano that has useful python libraries for audio and midi manipulation. It is a fundamentally different ML architecture than our approach (cnn vs rcc) but has many links to relevant signal processing resources. Need to investigate the structure of the example data in this repository.
https://github.com/jsleep/wav2mid

#### Keras SEQ2SEQ implementation
Blogpost on a keras seq-to-seq neural network for machine translation (english -> french). Uses encoder decoder approach which is what we want but data type and shape is very different. 
https://blog.keras.io/a-ten-minute-introduction-to-sequence-to-sequence-learning-in-keras.html

#### Study of ML approaches to AMT
Stanford study published on automatic music transcription. Again, concerned with pitch more so than instrument classification. Tries both CNN and RNN architectures but prefers CNN. Useful discussion on data preparation and more sources.
http://cs229.stanford.edu/proj2017/final-reports/5242716.pdf

#### How to interpret midi data for the human
Resource for understanding the structure of midi data in CSV.
https://www.fourmilab.ch/webtools/midicsv/