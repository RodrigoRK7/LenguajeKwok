class SymbolTable:
    def __init__(self):
        self.variables = {}
        self.memoria = {}

        self.global_int = 0
        self.global_float = 1001
        self.global_char = 2001

        self.local_int = 3001
        self.local_float = 4001
        self.local_char = 5001

        self.espacio_temp_i = 6000
        self.espacio_temp_f = 7001
        self.espacio_temp_c = 8001
        self.espacio_temp_b = 9001

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
