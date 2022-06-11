'''
Rodrigo de Jesús Ruíz Kwok A00824488

Maquina.py:

En este archivo se lleva acabo el manejo de codigo intermedio e implementación de la máquina virtual.

'''
from tkinter.messagebox import NO
from Error import Error
import matplotlib.pyplot as plt
import numpy as np

saltos = []
contexto = []
class Maquina:
    def __init__(self, cuadruplos, vars, constantes):
        self.cuadruplos = cuadruplos
        self.vars = vars
        self.constantes = constantes #6,000 - 9,999

        self.globales_int = [] #10,000 - 19,999
        self.globales_float = [] #20,000 - 29,999
        self.globales_char = [] #30,000 - 39,999

        self.local_int = [] #40,000 - 49,999
        self.local_float = [] #50,000 - 59,999
        self.local_char = [] #60,000 - 69,999

        self.temporal_int = [] #1,000 - 1,999
        self.temporal_float = [] #2,000 - 2,999
        self.temporal_char = [] #3,000 - 3,999
        self.temporal_bool = [] #4,000 - 4,999
    
    def getValue(self, direction):
        if direction >= 1000 and direction <= 4999: #Temporales
            #print("Es temporal")
            if direction >= 1000 and direction <= 1999: #Temporales Int
                #print("Es temporal int")
                valor = self.temporal_int[direction-1000]
            elif direction >= 2000 and direction <= 2999:#Temporales float
                #print("Es temporal float")
                valor = self.temporal_float[direction-2000]
            elif direction >= 3000 and direction <= 3999: #Temporales char
                #print("Es temporal char")
                valor = self.temporal_char[direction-3000]
            elif direction >= 4000 and direction <= 4999: #Temporales bool
                #print("Es temporal bool")
                valor = self.temporal_bool[direction-4000]
        elif direction >= 6000 and direction <= 9999: #Es constante
            #print("Es constante")
            if direction >= 6000 and direction <= 6999: #Constante int
                #print("Es constante int")
                valor = self.constantes.getName(direction)
            elif direction >= 7000 and direction <= 7999: #Constante float
                #print("Es constante flotante")
                valor = self.constantes.getName(direction)
            elif direction >= 8000 and direction <= 8999: #Constante char
                #print("Es constante char")
                valor = self.constantes.getName(direction)
            elif direction >= 9000 and direction <= 9999: #Constante print
                #print("Es constante print")
                valor = self.constantes.getName(direction)
        elif direction >= 10000 and direction <= 39999: #Es global
            #print("Es global")
            if direction >= 10000 and direction <= 19999: #Global int
                #print("Es global entera")
                valor = self.globales_int[direction-10000]
            elif direction >= 20000 and direction <= 29999: #Global float
                #print("Es global float")
                valor = self.globales_float[direction-20000]
            elif direction >= 30000 and direction <= 39999: #Global char
                #print("Es global char")
                valor = self.globales_char[direction-30000]
        elif direction >= 40000 and direction <= 69999: #Es local
            #print("Es local")
            if direction >= 40000 and direction <= 49999: #Local int
                #print("Es local entera")
                valor = self.local_int[direction-40000]
            elif direction >= 50000 and direction <= 59999: #Local float
                #print("Es local float")
                valor = self.local_float[direction-50000]
            elif direction >= 60000 and direction <= 69999: #Local char
                #print("Es local char")
                valor = self.local_char[direction-60000]
        if valor == None:
            raise Error("DATO CON VALOR NONE")
        else:
            return valor
    
    def start(self):
        print("Inicializando maquina...")
        self.globales_int = [None] * self.vars[0]
        self.globales_float = [None] * self.vars[1]
        self.globales_char = [None] * self.vars[2]
        self.local_int = [None] * self.vars[3]
        self.local_float = [None] * self.vars[4]
        self.local_char = [None] * self.vars[5]
        self.temporal_int = [None] * self.vars[6]
        self.temporal_float = [None] * self.vars[7]
        self.temporal_char = [None] * self.vars[8]
        self.temporal_bool = [None] * self.vars[9]

        index = 0
        while self.cuadruplos[index].getOperador() != "END":
            #print(index, self.cuadruplos[index].get())
            checked = False
            goto = False
            gotoF = False
            gosub = False
        
            if self.cuadruplos[index].getOperador() == "PLOT" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                #print(valor1)
                plt.plot(valor1, valor2)
                plt.show()
                checked = True
            
            if self.cuadruplos[index].getOperador() == "POISSON" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                print(np.random.poisson(valor1, valor2))
                checked = True

            if self.cuadruplos[index].getOperador() == "BINOMIAL"and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor3 = self.getValue(self.cuadruplos[index].getTemporal())
                print(np.random.binomial(valor1, valor2, valor3))
                checked = True

            if self.cuadruplos[index].getOperador() == "UNIFORME" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor3 = self.getValue(self.cuadruplos[index].getTemporal())
                print(np.random.uniform(valor1, valor2, valor3))
                checked = True
            
            if self.cuadruplos[index].getOperador() == "NORMAL" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor3 = self.getValue(self.cuadruplos[index].getTemporal())
                print(np.random.normal(valor1, valor2, valor3))
                checked = True
                
            if self.cuadruplos[index].getOperador() == "=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor = self.getValue(self.cuadruplos[index].getOperandoIzq())
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor

                checked = True
                
            if self.cuadruplos[index].getOperador() == "+" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 + valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True
            
            if self.cuadruplos[index].getOperador() == "*" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 * valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor

                checked = True

            if self.cuadruplos[index].getOperador() == "/" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 / valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor

                checked = True

            if self.cuadruplos[index].getOperador() == "-" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 - valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor

                checked = True
            
            if self.cuadruplos[index].getOperador() == "||" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 or valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True

            if self.cuadruplos[index].getOperador() == "&&" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 and valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                
                checked = True

            if self.cuadruplos[index].getOperador() == "!=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 != valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True

            if self.cuadruplos[index].getOperador() == "==" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 == valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True

            if self.cuadruplos[index].getOperador() == ">=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 >= valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True
            
            if self.cuadruplos[index].getOperador() == "<=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 <= valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True

            if self.cuadruplos[index].getOperador() == "<" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 < valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True

            if self.cuadruplos[index].getOperador() == ">" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 > valor2
                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True

            if self.cuadruplos[index].getOperador() == "print" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        print(self.temporal_int[direction-1000]) 
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        print(self.temporal_float[direction-2000]) 
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        print(self.temporal_char[direction-3000])
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        print(self.temporal_bool[direction-4000])
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    if direction >= 6000 and direction <= 6999: #Constante int
                        #print("Es constante int")
                        print(self.constantes.getName(direction))
                    elif direction >= 7000 and direction <= 7999: #Constante float
                        #print("Es constante flotante")
                        print(self.constantes.getName(direction))
                    elif direction >= 8000 and direction <= 8999: #Constante char
                        #print("Es constante char")
                        print(self.constantes.getName(direction))
                    elif direction >= 9000 and direction <= 9999: #Constante print
                        #print("Es constante print")
                        var = self.constantes.getName(direction)
                        print(var[1:-1])
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        print(self.globales_int[direction-10000])
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        print(self.globales_float[direction-20000])
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        print(self.globales_char[direction-30000])
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        print(self.local_int[direction-40000])
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        print(self.local_float[direction-50000])
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        print(self.local_char[direction-60000])

                checked = True

            if self.cuadruplos[index].getOperador() == "read" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                #print(direction)
                valor = input()
                try:
                    valor = int(valor)
                except ValueError:
                    try:
                        valor = float(valor)
                    except ValueError:
                        try:
                            valor = chr(valor)
                        except ValueError:
                            raise Error("INPUT INVALIDO")

                #print(valor)
                if direction >= 1000 and direction <= 4999: #Temporales
                    #print("Es temporal")
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        #print("Es temporal int")
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        #print("Es temporal float")
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        #print("Es temporal char")
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        #print("Es temporal bool")
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    #print("Es constante")
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    #print("Es global")
                    if direction >= 10000 and direction <= 19999: #Global int
                        #print("Es global entera")
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        #print("Es global float")
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        #print("Es global char")
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    #print("Es local")
                    if direction >= 40000 and direction <= 49999: #Local int
                        #print("Es local entera")
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        #print("Es local float")
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        #print("Es local char")
                        self.local_char[direction-60000] = valor
                checked = True

            if self.cuadruplos[index].getOperador() == "GOTO" and checked == False:
                index = self.cuadruplos[index].getTemporal()
                goto = True
                checked = True
            
            if self.cuadruplos[index].getOperador() == "GOTOF" and (checked == False or goto):
                valor = self.getValue(self.cuadruplos[index].getOperandoIzq())
                if valor == False:
                    index = self.cuadruplos[index].getTemporal()
                    gotoF = True
                else:
                    pass
            
            if self.cuadruplos[index].getOperador() == "ERA" and checked == False:
                saltos.append(self.cuadruplos[index].getTemporal())
                checked = True
            
            if self.cuadruplos[index].getOperador() == "GOSUB" and checked == False:
                saltos.append(index)
                index = saltos.pop(-2)
                checked = True
                gosub = True
            
            if self.cuadruplos[index].getOperador() == "ENDFUNC" and checked == False:
                index = saltos.pop()
                checked = True
            
            if goto == False and gotoF == False and gosub == False:
                index = index + 1
    