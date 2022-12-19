import os.path as path
import wx

class UI(wx.Frame):
    panel = []
    text_learn = []
    text_verify = []
    text_mode = []

    def __init__(self):
        super().__init__(parent=None, title="Weryfikacja")
        self.panel = wx.Panel(self)

        self.text_learn = wx.StaticText(self.panel, pos=(5, 5), label="Naucz algorytm")
        self.text_verify = wx.StaticText(self.panel, pos=(5, 105), label="Weryfikuj")
        self.text_mode = wx.StaticText(self.panel, pos=(5, 205), label="")

        if path.isfile("../models/kacper"):
            kacper_btn = wx.Button(self.panel, label='Kacper', pos=(5, 35))
            kacper_btn.Bind(wx.EVT_BUTTON, self.train_kacper)
        else:
            jakub_btn = wx.Button(self.panel, label='Kacper', pos=(5, 135))
            jakub_btn.Bind(wx.EVT_BUTTON, self.verify_kacper)

        if path.isfile("../models/jakub"):
            jakub_btn = wx.Button(self.panel, label='Jakub', pos=(105, 35))
            jakub_btn.Bind(wx.EVT_BUTTON, self.train_jakub)
        else:
            jakub_btn = wx.Button(self.panel, label='Jakub', pos=(105, 135))
            jakub_btn.Bind(wx.EVT_BUTTON, self.verify_jakub)

        self.Show()

    def train_kacper(self, event):
        self.text_mode.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_mode.SetLabel("Uczenie algorytmu dla: Kacper")

    def train_jakub(self, event):
        self.text_mode.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_mode.SetLabel("Uczenie algorytmu dla: Jakub")

    def verify_kacper(self, event):
        self.text_mode.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_mode.SetLabel("Weryfikacja dla: Kacper")
    def verify_jakub(self, event):
        self.text_mode.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_mode.SetLabel("Weryfikacja dla: Jakub")

if __name__ == '__main__':
    app = wx.App()
    frame = UI()
    app.MainLoop()