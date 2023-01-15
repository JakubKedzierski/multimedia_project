import os.path as path
import wx
from face_recognition import FaceRecognizer

class UI(wx.Frame):
    panel = []
    text_learn = []
    text_verify = []
    verification_label = []
    input_label = []
    log_label = []
    input_type = "brak"
    class_type = "brak"
    face_recognizer = FaceRecognizer()

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

        live_button = wx.Button(self.panel, label='Live', pos=(205, 135))
        live_button.Bind(wx.EVT_BUTTON, self.live_face_verification)

        test_dir_button = wx.Button(self.panel, label='Dane Testowe', pos=(55, 135))
        test_dir_button.Bind(wx.EVT_BUTTON, self.test_dir_face_verification)


        start_button = wx.Button(self.panel, label='START', pos=(140, 380))
        start_button.Bind(wx.EVT_BUTTON, self.run_verification)

        self.Show()

    def train_face_recognition(self, event):
        self.log_label.SetLabel("")
        self.verification_label.SetForegroundColour(wx.Colour(0, 0, 0))
        self.log_label.SetLabel("Uczenie rozpoznawania twarzy ...")
        self.Show()

        self.face_recognizer.train_face_recognition()
        # progressin ...
        self.log_label.SetLabel("Algorytm rozpoznawania nauczony ")

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
        self.input_type = "Live"
        self.input_label.SetLabel(self.input_type)

    def test_dir_face_verification(self, event):
        self.input_type = "Testowe dane"
        self.input_label.SetLabel(self.input_type)


    def run_verification(self, event):
        if self.input_type == "brak" or self.class_type == "brak":
            self.log_label.SetLabel("Ustaw odpowiednie parametry (wejście, osoba do rozpoznania ...) !")
            wx.MessageBox('Ustaw odpowiednie parametry (wejście, osoba do rozpoznania ...) !', 'Uwaga', wx.OK | wx.ICON_ERROR)
            return
        else:
            self.log_label.SetLabel("")
            
            if self.input_type == "Live":
                msg = 'Pierwszy krok weryfikacji to rozpoznanie twarzy. Ustaw twarz odpowiednio do kamery ' + \
                'a następnie kliknij spacje. Algorytm wskaże wynik rozpoznania, aby przejść dalej konieczne będzie wciśnięcie dowolnego klawisza'

                if wx.MessageBox(msg, 'Informacja', wx.OK | wx.ICON_INFORMATION) == wx.OK:  
                    predicions = self.face_recognizer.live_recognition()
                    
                    # predicions[0] - klasa : 0-> tło, brak  1->Kuba, 2->Kacper
                    # predicions[1] - prawdopodobienstwo


                    # tutaj rozpozawanie głosu



                    # łączenie wyników (twarz + głos)
                    total_result = predicions

                    # if probability < 50 change result to unrecognized 
                    if total_result[1] < 50:
                        total_result[0] = 0

                    msg = 'Prawdopodobieństwo: ' + "{:.2f}".format(total_result[1]) + '\n'
                    if total_result[0] == 1 and 'Jakub' in self.class_type:
                        msg = msg + "Weryfikacja poprawna. Użytkownika Jakub autoryzowany !"
                    elif total_result[0] == 2 and 'Kacper' in self.class_type:
                        msg = msg + "Weryfikacja poprawna. Użytkownika Kacper autoryzowany !"
                    else:
                        msg = msg + "Weryfikacja niepowiodła się."

                    if wx.MessageBox(msg, 'Informacja', wx.OK | wx.ICON_INFORMATION) == wx.OK:  
                        pass
            elif self.input_type == "Testowe dane":
                predicions = self.face_recognizer.test_image_recognition()

                # predicions[0] - klasa
                # predicions[1] - prawdopodobienstwo

                # tutaj rozpozawanie głosu

                # łączenie wyników (twarz + głos)
                total_result = predicions

                msg = ''
                if total_result[0] == 1 and 'Jakub' in self.class_type:
                    msg = "Weryfikacja poprawna. Użytkownik Jakub autoryzowany !"
                elif total_result[0] == 2 and 'Kacper' in self.class_type:
                    msg = "Weryfikacja poprawna. Użytkownik Kacper autoryzowany !"
                else:
                    msg = "Weryfikacja nie powiodła się."

                if wx.MessageBox(msg, 'Informacja', wx.OK | wx.ICON_INFORMATION) == wx.OK:  
                    pass


if __name__ == '__main__':
    app = wx.App()
    frame = UI()
    app.MainLoop()