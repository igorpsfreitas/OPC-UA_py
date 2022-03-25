from cgitb import text
from opcua import Server
from time import sleep
import os
from tkinter import *

os.system('cls' if os.name == 'nt' else 'clear')

ip_OPC = '192.168.0.104'
porta_OPC = '4840'

    

def main():
    servidor = Server()
    servidor.set_endpoint(f'opc.tcp://{ip_OPC}:{porta_OPC}')

    spaceNome = 'Flexsim'
    space = servidor.register_namespace(spaceNome)

    objetos = servidor.get_objects_node()
    grupo_objetos = objetos.add_object(space, 'Grupo Objetos')

    estado01 = grupo_objetos.add_variable(space, 'Estado 01', 0)
    
    
    estado01.set_writable()
    
    
    servidor.start()
    
    tela = Tk()
    
    def teste():
        w1['text'] = str(estado01.get_value())
        tela.after(500,teste)    

    try:
        
        w1 = Label(tela)
        w1.pack()
        teste()
        tela.mainloop()    
    
    finally:
        servidor.stop()

if __name__ == "__main__":
    main()
    
