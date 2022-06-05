import ply.lex as lex
import ply.yacc as yacc

class MaquinaVirtual:
    def __init__(self, cuadruplos, directorioFunciones, constantes):
        self.cuadruplos = cuadruplos
        self.directorioFunciones = directorioFunciones
        self.constantes = constantes

    def start(self):
        print("Iniciando maquina...")
        for index, i in enumerate(self.cuadruplos):
            print(str(index+1)+".-", i.get())
            if i.getOperador() == "+":
                print("ES UNA SUMA WUJUU")
        

