'''
Rodrigo de Jesús Ruíz Kwok A00824488

Clase Constantes:

Clase utilizada para manejar las constantes, su tipo y su espacio de memoria.

'''
class Constantes:
    def __init__(self):
        self.constantes = {}
        self.memoria = {}

        #Direcciones para las constantes
        self.constantes_int = 6000
        self.constantes_float = 7000
        self.constantes_char = 8000
        self.constantes_print = 9000

        self.contador_int = 0
        self.contador_float = 0
        self.contador_char = 0
        self.contador_prints = 0
        
    #Se agrega una constante al diccionario con su tipo y en otro diccionario con su dirección de memoria
    def add(self, name, type):
        self.constantes[name] = type
        if type == "int":
            self.memoria[self.constantes_int] = name
            self.constantes_int = self.constantes_int + 1
            self.contador_int = self.contador_int + 1
        elif type == "float":
            self.memoria[self.constantes_float] = name
            self.constantes_float = self.constantes_float + 1
            self.contador_float = self.contador_float + 1
        elif type == "char":
            self.memoria[self.constantes_char] = name
            self.constantes_char = self.constantes_char + 1
            self.contador_char = self.contador_char + 1
        elif type == "print":
            self.memoria[self.constantes_print] = name
            self.constantes_print = self.constantes_print + 1
            self.contador_prints = self.contador_prints + 1

    #Verificar si una constante ya ha sido declarada o no    
    def verify(self, name):
        if(name in self.memoria.values()):
            return True
        else:
            return False
    
    #Regresar el tipo de la constante
    def getType(self, name):
        return self.constantes[name]
    
    #Regresar la dirección de memoria asignada a la constante
    def getMemory(self, name):
        for key, value in self.memoria.items():
            if name == value:
                return key

    #Regresar el nombre de una constante dada la dirección de memoria
    def getName(self,direction):
        return self.memoria[direction]
    
    #Verificar si una direccion de memoria existe o no    
    def verifyDirection(self, direction):
        if(direction in self.memoria.keys()):
            return True
        else:
            return False