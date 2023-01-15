import numpy as np
import librosa

def extract_features(path):

    librosa_audio, librosa_sample_rate = librosa.load(path, res_type='kaiser_fast')

    mfccs = librosa.feature.mfcc(y=librosa_audio, sr=44100, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    return mfccs_processed