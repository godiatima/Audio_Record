from pydub import AudioSegment
sound = AudioSegment.from_wav('myfile.wav')

sound.export('myfile.mp3', format='mp3')