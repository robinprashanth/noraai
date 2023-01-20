import sounddevice as sd
import wavio as wv
import datetime
import os
import time

freq = 44100
duration = 10 # in seconds

print('Recording')
print(os.path.join(os.getcwd(), 'recordings'))

while True:

    ts = datetime.datetime.now()
    # filename = ts.strftime("%Y-%m-%d%H:%M:%S")
    # filename = ts.strftime("%Y-%m-%d%H%M%S")
    t = time.localtime()
    filename = time.strftime('%b-%d-%Y_%H%M', t)
    print('started Recording')

    # Start recorder with the given values of duration and sample frequency
    # PTL Note: I had to change the channels value in the original code to fix a bug
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    # Record audio for the given number of seconds
    sd.wait()

    recording_file = os.path.join(os.getcwd(), 'recordings', f"{filename}.wav")
    # f = open(f"{filename}.wav", "x")
    # f.close()

    # Convert the NumPy array to audio file
    wv.write(recording_file, recording, freq, sampwidth=2)
    print('saved Recording')