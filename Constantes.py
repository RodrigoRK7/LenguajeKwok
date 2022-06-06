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
        self.constantes_int = 10000
        self.constantes_float = 11000
        self.constantes_char = 12000
        self.constantes_print = 13000
        
    #Se agrega una constante al diccionario con su tipo y en otro diccionario con su dirección de memoria
    def add(self, name, type):
        self.constantes[name] = type
        if type == "int":
            self.memoria[name] = self.constantes_int
            self.constantes_int = self.constantes_int + 1
        elif type == "float":
            self.memoria[name] = self.constantes_float
            self.constantes_float = self.constantes_float + 1
        elif type == "char":
            self.memoria[name] = self.constantes_char
            self.constantes_char = self.constantes_char + 1
        elif type == "print":
            self.memoria[name] = self.constantes_print
            self.constantes_print = self.constantes_print + 1

    #Verificar si una constante ya ha sido declarada o no    
    def verify(self, name):
        if(name in self.constantes.keys()):
            return True
        else:
            return False
    
    #Regresar el tipo de la constante
    def getType(self, name):
        return self.constantes[name]
    
    #Regresar la dirección de memoria asignada a la constante
    def getMemory(self, name):
        return self.memoria[name]
    
    #Regresar el nombre de una constante dada la dirección de memoria
    def getName(self,direction):
     return [key for key in self.memoria if (self.memoria[key] == direction)]