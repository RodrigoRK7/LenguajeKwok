'''
Rodrigo de Jesús Ruíz Kwok A00824488

Clase SymbolTable:

Clase utilizada para manejar el tipo de funcion, las variables con su tipo y memoria,
la direccion en la que inicia la funcion, el orden de los tipos de parámetros que recibe y 
la cantidad de parámetros.

'''
class SymbolTable:
    def __init__(self):
        self.variables = {}
        self.memoria = {}
        self.type = ""
        self.numParam = 0
        self.tipos_Param = []
        self.dirV = 0

        #Direcciones de los valores globales
        self.global_int = 10000
        self.global_float = 20000
        self.global_char = 30000

        self.contador_global_int = 0
        self.contador_global_float = 0
        self.contador_global_char = 0

        #Direcciones de los valores locales
        self.local_int = 40000
        self.local_float = 50000
        self.local_char = 60000

        self.contador_local_int = 0
        self.contador_local_float = 0
        self.contador_local_char = 0

    #Se agrega una variable local a un diccionario de memoria y a otro de tipos
    def add(self, name, type):
        self.variables[name] = type
        if type == "int":
            self.memoria[self.local_int] = name
            self.local_int = self.local_int + 1
            self.contador_local_int = self.contador_local_int + 1
        elif type == "float":
            self.memoria[self.local_float] = name
            self.local_float = self.local_float + 1
            self.contador_local_float = self.contador_local_float + 1
        elif type == "char":
            self.memoria[self.local_char] = name
            self.local_char = self.local_char + 1
            self.contador_local_char = self.contador_local_char + 1

    #Se agrega una variable global a un diccionario de memoria y a otro de tipos
    def addGlobal(self, name, type):
        self.variables[name] = type
        if type == "int":
            self.memoria[self.global_int] = name
            self.global_int = self.global_int + 1
            self.contador_global_int = self.contador_global_int + 1
        elif type == "float":
            self.memoria[self.global_float] = name
            self.global_float = self.global_float + 1
            self.contador_global_float = self.contador_global_float + 1
        elif type == "char":
            self.memoria[self.global_char] = name
            self.global_char = self.global_char + 1
            self.contador_global_char = self.contador_global_char + 1

    #Verificar si ya ha sido agregada o no una variable al diccionario
    def verify(self, name):
        if(name in self.memoria.values()):
            return True
        else:
            return False
    
    #Regresa el tipo de la variable
    def getType(self, name):
        return self.variables[name]
    
    #Guarda el tipo de la funcion
    def setFuncType(self, type):
        self.type = type

    #Guarda el numero de parámetros
    def setNumParam(self, num):
        self.numParam = num
    
    #Guarda el orden de los tipos de los parámetros
    def setTiposParam(self, tipos_Param):
        self.tipos_Param = tipos_Param
    
    #Guarda la dirección en la que empieza la función
    def setDirV(self, dirV):
        self.dirV = dirV
    
    #Regresa el valor de memoria asignado a la variable
    def getMemory(self, name):
        for key, value in self.memoria.items():
            if name == value:
                return key

    #Regresa el nombre de la variable dada una dirección
    def getName(self,direction):
        return self.memoria[direction]
     #return [key for key in self.memoria if (self.memoria[key] == direction)]
    
    #Verificar si una direccion de memoria existe o no    
    def verifyDirection(self, direction):
        if(direction in self.memoria.keys()):
            return True
        else:
            return False