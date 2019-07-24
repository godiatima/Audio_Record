import soundfile as sound
 # Extract audio data and sampling rate from file 
 data. fs = sf.read('myfile.wav')
 # Save as FLAC file at correct sampling rate
 sf.write('myfile.flac', data, fs)