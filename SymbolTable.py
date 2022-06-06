class SymbolTable:
    def __init__(self):
        self.variables = {}
        self.memoria = {}
        self.type = ""
        self.numParam = 0
        self.tipos_Param = []
        self.dirV = 0

        self.global_int = 10000
        self.global_float = 20000
        self.global_char = 30000

        self.local_int = 40000
        self.local_float = 50000
        self.local_char = 60000


    def add(self, name, type):
        self.variables[name] = type
        if type == "int":
            self.memoria[name] = self.local_int
            self.local_int = self.local_int + 1
        elif type == "float":
            self.memoria[name] = self.local_float
            self.local_float = self.local_float + 1
        elif type == "char":
            self.memoria[name] = self.local_char
            self.local_char = self.local_char + 1

    def addGlobal(self, name, type):
        self.variables[name] = type
        if type == "int":
            self.memoria[name] = self.global_int
            self.global_int = self.global_int + 1
        elif type == "float":
            self.memoria[name] = self.global_float
            self.global_float = self.global_float + 1
        elif type == "char":
                self.memoria[name] = self.global_char
                self.global_char = self.global_char + 1

    def verify(self, name):
        if(name in self.variables.keys()):
            return True
        else:
            return False
    
    def getType(self, name):
        return self.variables[name]
    
    def setFuncType(self, type):
        self.type = type

    def setNumParam(self, num):
        self.numParam = num
    
    def setTiposParam(self, tipos_Param):
        self.tipos_Param = tipos_Param
    
    def setDirV(self, dirV):
        self.dirV = dirV
    
    def getMemory(self, name):
        return self.memoria[name]

    def getName(self,direction):
     return [key for key in self.memoria if (self.memoria[key] == direction)]

class Constantes:
    def __init__(self):
        self.constantes = {}
        self.memoria = {}
        self.constantes_int = 10000
        self.constantes_float = 11000
        self.constantes_char = 12000
        self.constantes_print = 13000
        
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
            
    def verify(self, name):
        if(name in self.constantes.keys()):
            return True
        else:
            return False
    
    def getType(self, name):
        return self.constantes[name]
    
    def getMemory(self, name):
        return self.memoria[name]
    
    def getName(self,direction):
     return [key for key in self.memoria if (self.memoria[key] == direction)]
