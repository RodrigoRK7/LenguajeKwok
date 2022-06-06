from Error import Error
import matplotlib.pyplot as plt
import ply.lex as lex
import ply.yacc as yacc

class MaquinaVirtual:
    def __init__(self, cuadruplos, directorioFunciones, constantes):
        self.cuadruplos = cuadruplos
        self.directorioFunciones = directorioFunciones
        self.constantes = constantes
        self.datos = {}

    def getName(self, contexto, name):
        tablaVar = self.directorioFunciones.get(contexto[0])
        print(contexto)
        data = 0
        if tablaVar.getName(name):
            data = tablaVar.getName(name)
        elif self.constantes.getName(name):
            data = self.constantes.getName(name)
            #self.datos[data] = data
        else:
            name = int(name)
            if name >= 15000 and name < 16000:
                data = name - 15000 #temporal int
                data = "Ti"+str(data+1)
            elif name >= 16000 and name < 17000:
                data = name - 16000 #temporal float
                data = "Tf"+str(data+1)
            elif name >= 17000 and name < 18000:
                data = name - 17000 #temporal char
                data = "Tc"+str(data+1)
            elif name >= 18000 and name < 19000:
                data = name - 18000 #temporal bool
                data = "Tb"+str(data+1)
        return data

    def start(self):
        print("Iniciando maquina...")
        contexto = []
        for index, i in enumerate(self.directorioFunciones.funciones):
            contexto.append(i)
        print(contexto)
        contexto.pop(0)
        for index, i in enumerate(self.cuadruplos):
            index = index + 1
            print(str(index)+".-", i.get())
            if i.getOperador() == "+":
                operandoIzq = i.getOperandoIzq()
                operandoDer = i.getOperandoDer()
                resultado = i.getTemporal()
                
                print(operandoIzq, operandoDer, resultado)
                
                izq = self.getName(contexto, operandoIzq)
                der = self.getName(contexto, operandoDer)
                resul = self.getName(contexto, resultado)
                print(resul, "=", izq, "+", der)

            elif i.getOperador() == "-":
                print("Resta")
            elif i.getOperador() == "&&":
                print("And")
            elif i.getOperador() == "||":
                print("Or")
            elif i.getOperador() == ">":
                print("Mayor que")
            elif i.getOperador() == "<":
                print("Menor que")
            elif i.getOperador() == "==":
                print("Igual a")
            elif i.getOperador() == "!=":
                print("Diferente que")
            elif i.getOperador() == "<=":
                print("Menor igual")
            elif i.getOperador() == ">=":
                print("Mayor igual")
            elif i.getOperador() == "*":
                print("Multiplica")
            elif i.getOperador() == "/":
                print("Divide")
            elif i.getOperador() == "read":
                x = input()
            elif i.getOperador() == "print":
                print(i.getTemporal())
            elif i.getOperador() == "GOTO":
                print("goto")
            elif i.getOperador() == "ENDFUNC":
                contexto.pop(0)
            elif i.getOperador() == "=":
                print("Es un igual")
                valor = i.getOperandoIzq()
                variable = i.getTemporal()

                print(variable, valor)
                
                izq = self.getName(contexto, variable)
                der = self.getName(contexto, valor)
                
                print(izq, "=", der)


        

