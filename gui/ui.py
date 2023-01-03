import os.path as path
import wx

class UI(wx.Frame):
    panel = []
    text_learn = []
    text_verify = []
    verification_label = []
    input_label = []
    log_label = []
    input_type = "brak"
    class_type = "brak"

    def __init__(self):
        super().__init__(parent=None, title="Weryfikacja użytkownika", size=(400, 500))
        self.panel = wx.Panel(self)

        self.text_label = wx.StaticText(self.panel, pos=(5, 305), label="Weryfikacja dla: ")
        self.verification_label = wx.StaticText(self.panel, pos=(105, 305), label=self.class_type)
        
        self.text_l = wx.StaticText(self.panel, pos=(5, 335), label="Typ wejścia: ")
        self.input_label = wx.StaticText(self.panel, pos=(105, 335), label=self.input_type)

        self.log_label = wx.StaticText(self.panel, pos=(5, 430), label="")

        ### train

        self.text_learn = wx.StaticText(self.panel, pos=(5, 5), label="Naucz algorytm")
        face_btn = wx.Button(self.panel, label='Rozpoznawanie twarzy', pos=(15, 35))
        face_btn.Bind(wx.EVT_BUTTON, self.train_face_recognition)

        voice_btn = wx.Button(self.panel, label='Rozpozawanie głosu', pos=(205, 35))
        voice_btn.Bind(wx.EVT_BUTTON, self.train_voice_recognition)

        ### verification

        self.text_verify = wx.StaticText(self.panel, pos=(5, 195), label="Weryfikowana osoba:")
        kacper_btn = wx.Button(self.panel, label='Kacper', pos=(50, 220))
        kacper_btn.Bind(wx.EVT_BUTTON, self.verify_kacper)

        jakub_btn = wx.Button(self.panel, label='Jakub', pos=(205, 220))
        jakub_btn.Bind(wx.EVT_BUTTON, self.verify_jakub)

        ### input form
        self.text_input = wx.StaticText(self.panel, pos=(5, 105), label="Typ wejścia:")

        live_button = wx.Button(self.panel, label='Kamera Live', pos=(205, 135))
        live_button.Bind(wx.EVT_BUTTON, self.live_face_verification)

        test_dir_button = wx.Button(self.panel, label='Dane Testowe', pos=(55, 135))
        test_dir_button.Bind(wx.EVT_BUTTON, self.test_dir_face_verification)


        start_button = wx.Button(self.panel, label='START', pos=(140, 380))
        start_button.Bind(wx.EVT_BUTTON, self.run_verification)

        self.Show()

    def train_face_recognition(self, event):
        self.verification_label.SetForegroundColour(wx.Colour(0, 0, 0))
        self.log_label.SetLabel("Uczenie rozpoznawania twarzy")
        self.Show()

        # progressin ...
        #self.log_label.SetLabel("")

    def train_voice_recognition(self, event):
        self.verification_label.SetForegroundColour(wx.Colour(0, 0, 0))
        self.log_label.SetLabel("Uczenie rozpoznawania głosu")
        self.Show()

        # progressin ...
        #self.log_label.SetLabel("")

    def verify_kacper(self, event):
        self.class_type = "Kacper"
        self.verification_label.SetLabel(self.class_type)

    def verify_jakub(self, event):
        self.class_type = "Jakub"
        self.verification_label.SetLabel(self.class_type)

    def live_face_verification(self, event):
        self.input_type = "Kamera live"
        self.input_label.SetLabel(self.input_type)

    def test_dir_face_verification(self, event):
        self.input_type = "Testowe dane"
        self.input_label.SetLabel(self.input_type)

    def run_verification(self, event):
        if self.input_type == "brak" or self.class_type == "brak":
            self.log_label.SetLabel("Ustaw odpowiednie parametry (wejście, osoba do rozpoznania ...) !")
            return
        else:
            self.log_label.SetLabel("")


if __name__ == '__main__':
    app = wx.App()
    frame = UI()
    app.MainLoop()