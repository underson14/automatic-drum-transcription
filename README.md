# Automatic Drum Transcription

## Usage

1. Clone or download the project
2. Rename the start script for your operation system and remove the .dist
    Example for windows users: start.bat.dist should be renamed to shart.bat.
3. Open the start script and change the python3 call to the correct one for your system.  
If you use python3 to call python3.x leave it, if you use python to call python3.x change it.
4. Start the application using the startscript and adding a path as argument.  
Example:  ```.\start.bat .\data\drum-data-mvp\```


---

3/2020
Automatic drum transcription using neural nets

#### Use Case: Replay sample to avoid sample license
Suppose you wrote a song based on a drum break from a popular song. In order to publish the song legally you would need to obtain clearance to use the sample from the copyright holder. A common practice is to re-record the drum loop instead. The essence of the pattern is the same but now there is no problem with ownership of the recording. This package could automate that process. Given an audio file, it will return the midi file you would need to have a sampler replay the file.

#### Use case: Right rhythm, wrong sounds
Suppose you have a library of drum loops in .wav format. There may be a pattern you would like to use in your song but the sounds aren't suitable. The rhythm is right but the sounds are wrong. With this package, you will be able to transcribe the underlying rhythm as midi and pass that midi to a drum machine or sampler where you can select souds that are more suitable for the song. Furthermore, you can now manipulate the pattern freely and create variations as desired.     
