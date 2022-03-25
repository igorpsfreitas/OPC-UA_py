from tkinter import *

class Application:
    def __init__(self, master=None):
        self._tela = master
        if master == None:
            self._tela = Tk()
        self.widget1 = Frame(self._tela)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack ()
    
    def loop(self):
        self._tela.mainloop()
        
    def Cria_tela(self):
        self._tela.mainloop()
        
    


i = Application()
i.Cria_tela()