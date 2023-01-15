import numpy as np
import librosa

def extract_features(path):

    librosa_audio, librosa_sample_rate = librosa.load(path, res_type='kaiser_fast')
    trimmed_audio, index = yt, index = librosa.effects.trim(librosa_audio, top_db=15, frame_length=20)

    mfccs = librosa.feature.mfcc(y=trimmed_audio, sr=44100, n_mfcc=40)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    return mfccs_processed