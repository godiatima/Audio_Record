import simpleaudio as simpleaudio

filename = 'meek mill - Youtube.mp3'
wave_obj = a.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done() # Wait until sound has finished playing