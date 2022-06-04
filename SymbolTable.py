class SymbolTable:
    def __init__(self):
        self.variables = {}
        
    def add (self, name, type):
        self.variables[name] = type

    def verify(self, name):
        if(name in self.variables):
            return True
        else:
            return False

class Constantes:
    def __init__(self):
        self.constantes = {}
        
    def add (self, name):
        self.constantes[name] = 1000

    def verify(self, name):
        if(name in self.constantes):
            return True
        else:
            return False

