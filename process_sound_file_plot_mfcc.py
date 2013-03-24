# To see the plot window, run this program in interactive mode:
# python -i <name of this .py file>
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
print data_float.shape

import MFCC
# data_float is a wave signal saved in a 1-D numpy array
# mfcc is a 2-D numpy array, where each row is the
# MFCC of a frame in data_float
mfcc = MFCC.extract(data_float, show = True)
# This will also plot the MFCC and the spectrogram
# reconstructed from MFCC by inverse DCT

