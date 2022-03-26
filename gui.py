from cgitb import text
from tkinter import *
from turtle import title

from ipStuff import ip_ethernet

class Tela_main():
    
    def __init__(self):
        # Propriedades da tela principal
        self._tela = Tk()
        self._tela.geometry('500x500')
        self._tela.title('Servidor OPC UA - HUB')
        self._tela.iconbitmap('favicon.ico')
        
        # MenuBar
        menu_bar  = Menu(self._tela)
        self._tela.config(menu=menu_bar)
        
        item_01 = Menu(menu_bar)
        menu_bar.add_cascade(label='Teste', menu=item_01)
        
        
        # Frame de Variaveis
        
        self._frame_variavel = Frame(self._tela,relief='groove',borderwidth=2,width=100, height=50)
        self._frame_variavel.pack(anchor='nw')
        
        listato = []
        
        self.bott = Button(self._tela, text='Editar', command=lambda: self.Cria_variavel(listato) ).pack()
        
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
    
    # Metodo para criar variaveis
    
    
    
    
    def Cria_tela(self):
        self._tela.mainloop()
        
    def Cria_variavel(self,lista):
        lista.append(variaveis(self._frame_variavel, 't01'))
        for i in lista:
            i.pack()
        
        
class variaveis():
    def __init__(self, frame, nome) -> None:
        self.contener = Frame(frame).pack()
        self._name_var = Label(self.contener, text=nome).grid(row=0, column=0)
        self.var1 = Entry(self.contener, width=10)
        self.var1.grid(row=0,column=1)
        self.bott = Button(self.contener, text='Editar').grid(row=0, column=2)
        self.var1.insert(0, 'vixi')
        self.var1['state'] ='disabled'
