import numpy as np
from scikits.audiolab import Sndfile

SOUND_DIRECTORY = 'small_data_sample/right_whale'

test_file = '%s/train12.aiff' % SOUND_DIRECTORY

f = Sndfile(test_file, 'r')

# Sndfile instances can be queried for the audio file meta-data
fs = f.samplerate
nc = f.channels
enc = f.encoding

# Reading is straightfoward
data = f.read_frames(1000)

# This reads the next 1000 frames, e.g. from 1000 to 2000, but as single precision
data_float = f.read_frames(1000, dtype=np.float32)
