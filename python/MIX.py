import numpy as np
import librosa
import librosa.output

y, sr = librosa.load("test.mp3")
y=-y
librosa.output.write_wav("-"+".wav", y=y, sr=sr)
