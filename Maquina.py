'''
Rodrigo de Jesús Ruíz Kwok A00824488

Maquina.py:

En este archivo se lleva acabo el manejo de codigo intermedio e implementación de la máquina virtual.

'''
from Error import Error
import matplotlib.pyplot as plt
import numpy as np

#Creacion de pilas auxiliares
saltos = []
contexto = []

#Definicion de la maquina virtual
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
    
    #Funcion para obtener el valor de una direccion de memoria, para obtener el indice se resta la direccion que se recibe como parametro - la base del tipo
    def getValue(self, direction):
        if direction >= 1000 and direction <= 4999: #Temporales
            if direction >= 1000 and direction <= 1999: #Temporales Int
                valor = self.temporal_int[direction-1000]
            elif direction >= 2000 and direction <= 2999:#Temporales float
                valor = self.temporal_float[direction-2000]
            elif direction >= 3000 and direction <= 3999: #Temporales char
                valor = self.temporal_char[direction-3000]
            elif direction >= 4000 and direction <= 4999: #Temporales bool
                valor = self.temporal_bool[direction-4000]
        elif direction >= 6000 and direction <= 9999: #Es constante
            if direction >= 6000 and direction <= 6999: #Constante int
                valor = self.constantes.getName(direction)
            elif direction >= 7000 and direction <= 7999: #Constante float
                valor = self.constantes.getName(direction)
            elif direction >= 8000 and direction <= 8999: #Constante char
                valor = self.constantes.getName(direction)
            elif direction >= 9000 and direction <= 9999: #Constante print
                valor = self.constantes.getName(direction)
        elif direction >= 10000 and direction <= 39999: #Es global
            if direction >= 10000 and direction <= 19999: #Global int
                valor = self.globales_int[direction-10000]
            elif direction >= 20000 and direction <= 29999: #Global float
                valor = self.globales_float[direction-20000]
            elif direction >= 30000 and direction <= 39999: #Global char
                valor = self.globales_char[direction-30000]
        elif direction >= 40000 and direction <= 69999: #Es local
            if direction >= 40000 and direction <= 49999: #Local int
                valor = self.local_int[direction-40000]
            elif direction >= 50000 and direction <= 59999: #Local float
                valor = self.local_float[direction-50000]
            elif direction >= 60000 and direction <= 69999: #Local char
                valor = self.local_char[direction-60000]
        if valor == None:
            raise Error("DATO CON VALOR NONE")
        else:
            return valor
    
    #Funcion para inicializar la maquina
    def start(self):
        print("Inicializando maquina...")
        #Reservar los espacios en los arreglos de cada tipo
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

        #Recorrer los cuadruplos hasta encontrar el END
        index = 0
        while self.cuadruplos[index].getOperador() != "END":
            #print(index, self.cuadruplos[index].get())
            
            #Flags para saber hacia donde irnos dirigiendo
            checked = False
            goto = False
            gotoF = False
            gosub = False

            #Si el operador es un PLOT
            if self.cuadruplos[index].getOperador() == "PLOT" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                plt.plot(valor1, valor2)
                plt.show()
                checked = True
            
            #Si el operador es un POISSON
            if self.cuadruplos[index].getOperador() == "POISSON" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                print(np.random.poisson(valor1, valor2))
                checked = True

            #Si el operador es un BINOMIAL
            if self.cuadruplos[index].getOperador() == "BINOMIAL"and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor3 = self.getValue(self.cuadruplos[index].getTemporal())
                print(np.random.binomial(valor1, valor2, valor3))
                checked = True

            #Si el operador es un UNIFORME
            if self.cuadruplos[index].getOperador() == "UNIFORME" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor3 = self.getValue(self.cuadruplos[index].getTemporal())
                print(np.random.uniform(valor1, valor2, valor3))
                checked = True
            
            #Si el operador es un NORMAL
            if self.cuadruplos[index].getOperador() == "NORMAL" and checked == False:
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor3 = self.getValue(self.cuadruplos[index].getTemporal())
                print(np.random.normal(valor1, valor2, valor3))
                checked = True
            
            #Si el operador es un =
            if self.cuadruplos[index].getOperador() == "=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor = self.getValue(self.cuadruplos[index].getOperandoIzq())
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True
            
            #Si el operador es un +
            if self.cuadruplos[index].getOperador() == "+" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 + valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante    
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char    
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float    
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True
            
            #Si el operador es un *
            if self.cuadruplos[index].getOperador() == "*" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 * valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool    
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global    
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un /
            if self.cuadruplos[index].getOperador() == "/" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 / valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un -
            if self.cuadruplos[index].getOperador() == "-" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 - valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR UNA CONSTANTE A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True
            
            #Si el operador es un ||
            if self.cuadruplos[index].getOperador() == "||" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 or valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un &&
            if self.cuadruplos[index].getOperador() == "&&" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 and valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un !=
            if self.cuadruplos[index].getOperador() == "!=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 != valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un ==
            if self.cuadruplos[index].getOperador() == "==" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 == valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un >=
            if self.cuadruplos[index].getOperador() == ">=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 >= valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool    
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True
            
            #Si el operador es un <=
            if self.cuadruplos[index].getOperador() == "<=" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 <= valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un <
            if self.cuadruplos[index].getOperador() == "<" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 < valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un >
            if self.cuadruplos[index].getOperador() == ">" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor1 = self.getValue(self.cuadruplos[index].getOperandoIzq())
                valor2 = self.getValue(self.cuadruplos[index].getOperandoDer())
                valor = valor1 > valor2
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un print
            if self.cuadruplos[index].getOperador() == "print" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        print(self.temporal_int[direction-1000]) 
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        print(self.temporal_float[direction-2000]) 
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        print(self.temporal_char[direction-3000])
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        print(self.temporal_bool[direction-4000])
                elif direction >= 6000 and direction <= 9999: #Es constante
                    if direction >= 6000 and direction <= 6999: #Constante int
                        print(self.constantes.getName(direction))
                    elif direction >= 7000 and direction <= 7999: #Constante float
                        print(self.constantes.getName(direction))
                    elif direction >= 8000 and direction <= 8999: #Constante char
                        print(self.constantes.getName(direction))
                    elif direction >= 9000 and direction <= 9999: #Constante print
                        var = self.constantes.getName(direction)
                        print(var[1:-1]) #Eliminar comillas
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        print(self.globales_int[direction-10000])
                    elif direction >= 20000 and direction <= 29999: #Global float
                        print(self.globales_float[direction-20000])
                    elif direction >= 30000 and direction <= 39999: #Global char
                        print(self.globales_char[direction-30000])
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        print(self.local_int[direction-40000])
                    elif direction >= 50000 and direction <= 59999: #Local float
                        print(self.local_float[direction-50000])
                    elif direction >= 60000 and direction <= 69999: #Local char
                        print(self.local_char[direction-60000])
                checked = True

            #Si el operador es un read
            if self.cuadruplos[index].getOperador() == "read" and checked == False:
                direction = self.cuadruplos[index].getTemporal()
                valor = input()
                #Validar que sea un tipo de dato que se puede manejar
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

                if direction >= 1000 and direction <= 4999: #Temporales
                    if direction >= 1000 and direction <= 1999: #Temporales Int
                        self.temporal_int[direction-1000] = valor
                    elif direction >= 2000 and direction <= 2999:#Temporales float
                        self.temporal_float[direction-2000] = valor
                    elif direction >= 3000 and direction <= 3999: #Temporales char
                        self.temporal_char[direction-3000] = valor
                    elif direction >= 4000 and direction <= 4999: #Temporales bool
                        self.temporal_bool[direction-4000] = valor
                elif direction >= 6000 and direction <= 9999: #Es constante
                    raise Error("NO PUEDES ASIGNAR A UNA CONSTANTE")
                elif direction >= 10000 and direction <= 39999: #Es global
                    if direction >= 10000 and direction <= 19999: #Global int
                        self.globales_int[direction-10000] = valor
                    elif direction >= 20000 and direction <= 29999: #Global float
                        self.globales_float[direction-20000] = valor
                    elif direction >= 30000 and direction <= 39999: #Global char
                        self.globales_char[direction-30000] = valor
                elif direction >= 40000 and direction <= 69999: #Es local
                    if direction >= 40000 and direction <= 49999: #Local int
                        self.local_int[direction-40000] = valor
                    elif direction >= 50000 and direction <= 59999: #Local float
                        self.local_float[direction-50000] = valor
                    elif direction >= 60000 and direction <= 69999: #Local char
                        self.local_char[direction-60000] = valor
                checked = True

            #Si el operador es un GOTO
            if self.cuadruplos[index].getOperador() == "GOTO" and checked == False:
                index = self.cuadruplos[index].getTemporal()
                goto = True
                checked = True
            
            #Si el operador es un GOTOF
            if self.cuadruplos[index].getOperador() == "GOTOF" and (checked == False or goto):
                valor = self.getValue(self.cuadruplos[index].getOperandoIzq())
                if valor == False:
                    index = self.cuadruplos[index].getTemporal()
                    gotoF = True
                else:
                    pass
            
            #Si el operador es un ERA
            if self.cuadruplos[index].getOperador() == "ERA" and checked == False:
                saltos.append(self.cuadruplos[index].getTemporal())
                checked = True
            
            #Si el operador es un GOSUB
            if self.cuadruplos[index].getOperador() == "GOSUB" and checked == False:
                saltos.append(index)
                index = saltos.pop(-2)
                checked = True
                gosub = True
            
            #Si el operador es un ENDFUNC
            if self.cuadruplos[index].getOperador() == "ENDFUNC" and checked == False:
                index = saltos.pop()
                checked = True
            
            #Leer el siguiente cuadruplo en la lista
            if goto == False and gotoF == False and gosub == False:
                index = index + 1
    