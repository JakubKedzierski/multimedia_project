import train_voice.learn as learn
import pickle
import recorder

class VoiceRecognizer():
    whatever = None
    def __init__(self):
        self.whatever = ""

    def decide(self, who):
        model = pickle.load(open('../train_voice/models/' + who + '.sav', 'rb'))
        learn.decide(model=model, who=who)

    def record_live_sample(self):
        recorder.record_audio('../output')

    def train_voice_recognition(self, who):
        learn.train_on_test(who=who)

    def decide_for_test(self, who):
        model = pickle.load(open('../train_voice/models/' + who + '.sav', 'rb'))
        learn.decide(model=model, who=who)
