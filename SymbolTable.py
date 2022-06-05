class SymbolTable:
    def __init__(self):
        self.variables = {}
        self.memoria = {}
        self.type = ""
        self.numParam = 0
        self.tipos_Param = []
        self.dirV = 0

        self.global_int = 0
        self.global_float = 1000
        self.global_char = 2000

        self.local_int = 3000
        self.local_float = 4000
        self.local_char = 5000


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

class Constantes:
    def __init__(self):
        self.constantes = {}
        self.memoria = {}
        self.constantes_int = 10000
        self.constantes_float = 11001
        self.constantes_char = 12001
        
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
            
    def verify(self, name):
        if(name in self.constantes.keys()):
            return True
        else:
            return False
    
    def getType(self, name):
        return self.constantes[name]
    
    def getMemory(self, name):
        return self.memoria[name]
