# example of auto music transcription for polyphonic piano that has useful python libraries for audio and midi manipulation. It is a fundamentally different ML architecture than our approach (cnn vs rcc) but has many links to relevant signal processing resources. Need to investigate the structure of the example data in this repository.
https://github.com/jsleep/wav2mid


# Blogpost on a keras seq-to-seq neural network for machine translation (english -> french). Uses encoder decoder approach which is what we want but data type and shape is very different. 
https://blog.keras.io/a-ten-minute-introduction-to-sequence-to-sequence-learning-in-keras.html


# Stanford study published on automatic music transcription. Again # more concerned with pitch more so than instrument classification # and and correct placement in time. Tries both CNN and RNN architectures but prefers CNN ( I think this is not the  correct approach in principle and our network using an embedding will work better) Useful discussion on data preparation and more sources.
http://cs229.stanford.edu/proj2017/final-reports/5242716.pdf

# resource for understanding the structure of midi data in CSV. NEEDS REVIEWING. Need to figure out time mapping issue.  
https://www.fourmilab.ch/webtools/midicsv/