'''
Rodrigo de Jesús Ruíz Kwok A00824488

MaquinaVirtual.py:

En este archivo se lleva acabo el manejo de codigo intermedio e implementación de la máquina virtual.

'''
from Error import Error
import matplotlib.pyplot as plt
import ply.lex as lex
import ply.yacc as yacc
import matplotlib.pyplot as plt
import numpy as np

#Clase maquina virtual que lee los cuadruplos y dependiendo del operador realiza una operacion
class MaquinaVirtual:
    def __init__(self, cuadruplos, directorioFunciones, constantes):
        self.cuadruplos = cuadruplos
        self.directorioFunciones = directorioFunciones
        self.constantes = constantes
        self.datos = {}

    #Metodo para obtener el nombre
    def getName(self, contexto, name):
        tablaVar = self.directorioFunciones.get(contexto[0])
        #print(contexto)
        data = 0
        if tablaVar.getName(name):
            data = tablaVar.getName(name)
        elif self.constantes.getName(name):
            data = self.constantes.getName(name)
            self.datos[data] = data
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
        
        contexto.pop(0)
        for index, i in enumerate(self.cuadruplos):
            index = index + 1
            #print(str(index)+".-", i.get())
            if i.getOperador() == "+":
                operandoIzq = i.getOperandoIzq()
                operandoDer = i.getOperandoDer()
                resultado = i.getTemporal()
                izq = self.getName(contexto, operandoIzq)
                der = self.getName(contexto, operandoDer)
                resul = self.getName(contexto, resultado)

            elif i.getOperador() == "-":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "&&":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "||":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == ">":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "<":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "==":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "!=":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "<=":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == ">=":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "*":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "/":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "read":
                x = input()
            elif i.getOperador() == "print":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()
                print(i.getTemporal())               
            elif i.getOperador() == "GOTO":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                
            elif i.getOperador() == "ENDFUNC":
                contexto.pop(0)
            elif i.getOperador() == "=":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()
            elif i.getOperador() == "GOSUB":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()  
            elif i.getOperador() == "GOTOF":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()  
            elif i.getOperador() == "PARAM":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()
            elif i.getOperador() == "":
                valor = i.getOperandoIzq()
                variable = i.getTemporal()                    
            elif i.getOperador() == "PLOT":
                plt.plot(i.getTemporal())
                plt.show()
            elif i.getOperador() == "BINOMIAL":
                print(np.random.binomial(i.getOperandoIzq(), i.getOperandoDer(), i.getTemporal()))
            elif i.getOperador() == "NORMAL":
                print(np.random.normal(i.getOperandoIzq(), i.getOperandoDer(), i.getTemporal()))
            elif i.getOperador() == "POISSON":
                print(np.random.poisson(i.getOperandoIzq(), i.getOperandoDer()))
            elif i.getOperador() == "UNIFORME":
                print(np.random.normal(i.getOperandoIzq(), i.getOperandoDer(), i.getTemporal()))


        

