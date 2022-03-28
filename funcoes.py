from tkinter import *
from opcua import Server
import socket

# Retorna Ip primario de conecção Lan
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return str(s.getsockname()[0])

# Inicia Servidor OPC-UA
class Servidor():
    def __init__(self):
    
        self.ip_OPC = get_ip()
        self.porta_OPC = '4840'
    
        self.servidor = Server()
        self.servidor.name = 'Hub - OPC_UA'
        self.servidor.set_endpoint(f'opc.tcp://{self.ip_OPC}:{self.porta_OPC}')

        self.spaceNome = 'Flexsim'
        self.space = self.servidor.register_namespace(self.spaceNome)

        self.objetos = self.servidor.get_objects_node()
        self.grupo_objetos = self.objetos.add_object(self.space, 'Grupo Objetos')
    

        self.estado01 =  self.grupo_objetos.add_variable(self.space, 'Estado 01', 2)
    
    
        self.estado01.set_writable()
        self.servidor.start()

        #tela = Tk()
'''

    def get_valor_variavel(self, tela, variavel):
        w1['text'] = str(self.estado01.get_value())
        tela.after(500,self.get_valor_variavel)    

    
    try:
        
        w1 = Label(tela)
        w1.pack()
        teste()
        tela.mainloop()    
    
    finally:
        self.servidor.stop()
  
    '''