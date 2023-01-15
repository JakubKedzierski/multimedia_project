import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(output_file_name):
    fs = 44100  # Sample rate
    seconds = 2  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write(output_file_name+'.wav', fs, myrecording)  # Save as WAV file
