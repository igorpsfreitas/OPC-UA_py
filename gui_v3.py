from tkinter import *
from funcoes import Servidor

class Tela_main():
    
    def __init__(self):
        # Propriedades da tela principal
        self._tela = Tk()
        self._tela.geometry('500x500')
        self._tela.title('Servidor OPC UA - HUB')
        self._tela.iconbitmap('favicon.ico')
        
    def Cria_tela(self):
        self._tela.mainloop()
       
       
class Menu_bar():
    def __init__(self,tela,frame):
        self._menuBar = Menu(tela)
        self._menuBar.add_command(label='Add', command=lambda: self.Add_var(frame))
        
        tela.config(menu=self._menuBar)
    
    def Add_var(self,frame):
        
        frame._listaDeVariaveis.append(Variavel(frame._frame))        
        
                
class Frame_root():
    def __init__(self, tela):
        self._listaDeVariaveis = []
        self._frame = LabelFrame(tela, text='Variaveis')
        self._frame.pack()                               #####<<<<<<<<<<<<<<<<


class Variavel():
    def __init__(self, frame_root):
        self._frame_variavel = Frame(frame_root)
        self._nome = Label(self._frame_variavel, text='Variavel 01')
        self._valor = Entry(self._frame_variavel, width=5)
        self._editar = Button(self._frame_variavel, text='Editar', command=lambda: self.Habilitar_e_desabilitar())
        self._deletar = Button(self._frame_variavel, text='Deletar',command=lambda: self.Destroi_frame())
        
        self._frame_variavel.pack()
        self._nome.grid(row=0,column=0)
        self._valor.grid(row=0,column=1)
        self._editar.grid(row=0,column=2)
        self._deletar.grid(row=0,column=3)
        
        self.Habilitar_e_desabilitar()
        

    def Habilitar_e_desabilitar(self):
        match self._valor['state']:
            case 'normal':
                self._valor['state'] = 'disabled'
                self._editar['text'] = 'Editar'
            case 'disabled':
                self._valor['state'] = 'normal'
                self._editar['text'] = 'Salvar'
        
    def Set_valor(self, valor):
        self._valor['state'] = 'normal'
        self._valor.insert(0, valor)
        self._valor['state'] = 'disabled'   
        
    def Destroi_frame(self):
        self._frame_variavel.pack_forget()
        
    def auto_valor_variavel(self, servidor, tela):
        self.Set_valor(str(servidor.estado01.get_value()))
        #tela.after(500, self.auto_valor_variavel)
        
## Testes:        
if __name__ == "__main__":
    servidor = Servidor()
    root = Tela_main()
    frame_root = Frame_root(root._tela)
    menu = Menu_bar(root._tela, frame_root)
    botao = Variavel(frame_root._frame)
    botao.auto_valor_variavel(servidor,root)
    root.Cria_tela()