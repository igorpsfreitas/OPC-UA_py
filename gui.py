from cgitb import text
from tkinter import *
from turtle import title

from ipStuff import ip_ethernet

class Tela_main():
    
    def __init__(self):
        
        self._tela = Tk()
        self._tela.geometry('500x500')
        self._tela.title('Servidor OPC UA - HUB')
        
        
        
        self.frame_01 = Frame(self._tela,relief='groove',borderwidth=2,width=100, height=50)
        self.frame_01.pack(anchor='ne')
        
        self.ip_text = Label(self.frame_01, text='IP: ')
        self.ip_text.grid(row=1,column=1, sticky='w')       
        self._test = Label(self.frame_01, text=ip_ethernet())
        self._test.grid(row=1, column=2, sticky='w')
        
        self.porta_text = Label (self.frame_01, text='Porta: ')
        self.porta_text.grid(row=2, column=1, sticky='w')
        self.porta_var = Label(self.frame_01, text='4840')
        self.porta_var.grid(row=2, column=2, sticky='w')
    
    
    def Cria_tela(self):
        self._tela.mainloop()
        
        

