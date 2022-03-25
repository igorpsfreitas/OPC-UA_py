from cgitb import text
from tkinter import *

Tela = Tk()
li = []

def Cria_label(lista):
    print(li)
    return lista.append(Label(Tela, text='casa'))
    
def tipo(lista):
    for i in lista:
        i.pack()
def alterar(lista):
    lista[0]['text'] = 'vixi!!!!'
    
botao_01 = Button(Tela,text='Click', command=lambda: Cria_label(li)).pack()
botao_02 = Button(Tela,text='Click', command=lambda: tipo(li)).pack()
botao_03 = Button(Tela,text='Click', command=lambda: alterar(li)).pack()


Tela.mainloop()