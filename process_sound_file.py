import numpy as np
import os
import pickle
from scikits.audiolab import Sndfile
import pdb
#TODO(irvin) make the directory of sound files a parameter to this script
SOUND_DIRECTORY = 'small_data_sample/right_whale'


def convert_aiff_to_array(file_name):
    f = Sndfile(file_name, 'r')

    # Sndfile instances can be queried for the audio file meta-data
    fs = f.samplerate
    nc = f.channels
    enc = f.encoding

    # Reading is straightfoward
    data = f.read_frames(1000)

    # This reads the next 1000 frames, e.g. from 1000 to 2000, but as single precision
    data_float = f.read_frames(1000, dtype=np.float32)
    return data_float


whale_data = np.array([])
all_whale_sounds = [convert_aiff_to_array('%s/%s' % (SOUND_DIRECTORY, sound_file_name)) for
                    sound_file_name in os.listdir(SOUND_DIRECTORY)]

whale_data = np.array(all_whale_sounds)

output = open('whale_data.pkl', 'wb')

pickle.dump(whale_data, output)
