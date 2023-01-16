import numpy as np
import librosa

def extract_features(path):
    # odczytaj plik
    librosa_audio, librosa_sample_rate = librosa.load(path, res_type='kaiser_fast')
    # usuń ciszę z nagrania
    trimmed_audio, index = librosa.effects.trim(librosa_audio, top_db=15, frame_length=20)
    # ekstrakcja wektora cech melowych, częst. próbkowania 441000, liczba współczynników cepstralnych w częstotliwości melowej w wektorze - 39
    mfccs = librosa.feature.mfcc(y=trimmed_audio, sr=44100, n_mfcc=39)
    mfccs_processed = np.mean(mfccs.T, axis=0)
    return mfccs_processed