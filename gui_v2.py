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
        
        # Atributos:
        self.lista_de_variaveis = []
                
        # Frame de Variaveis
        self._frame_de_variaveis = Frame(self._tela,relief='groove',borderwidth=2,width=100, height=50)
        self._frame_de_variaveis.pack(anchor='nw')
        
        
        self.bt_adicionar_variavel = Button(self._tela, text='Editar', command=lambda: self.Cria_variavel(self.lista_de_variaveis)).pack()
        
        
    # Metodos
    
    def Cria_tela(self):
        self._tela.mainloop()
        
    def Cria_variavel(self,lista):
        lista.append(variaveis(self._frame_de_variaveis, 'Teste'))
        
        
class variaveis():
    def __init__(self, frame, nome) -> None:
        self.contener = Frame(frame)
        self.contener.pack()
        self._name_var = Label(self.contener, text=nome).grid(row=0, column=0)
        self.var1 = Entry(self.contener, width=10)
        self.var1.grid(row=0,column=1)
        self.bott = Button(self.contener, text='Editar').grid(row=0, column=2)
        self.bott = Button(self.contener, text='Deletar', command=lambda: self.Destroi_frame()).grid(row=0, column=3)
        self.var1.insert(0, 'vixi')
        self.var1['state'] ='disabled'

    def Destroi_frame(self):
        self.contener.pack_forget()