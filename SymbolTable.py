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

    def getType(self, name):
        return self.variables[name]

class Constantes:
    def __init__(self):
        self.constantes = []
        
    def add (self, name):
        self.constantes.append(name)

    def verify(self, name):
        if(name in self.constantes):
            return True
        else:
            return False

