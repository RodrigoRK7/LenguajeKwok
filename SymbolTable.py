import logging

class SymbolTable:
    def __init__(self):
        self.variables = {}
        
    def add (self, name, type):
        self.variables[name] = type

    def verify(self, name):
        if(name in self.variables):
            return 1
        else:
            return 0

    def search (self, name):
        if(name in self.variables):
            return self.variables[name]
        DirectorioGlobal.getGlobal(name)

class DirectorioGlobal:

    @staticmethod
    def getGlobal(name):
        from DirectorioFunciones import DirectorioFunciones

        symbolTableGlobal = DirectorioFunciones()

        symbolTableGlobal= symbolTableGlobal.get("global")
        if(symbolTableGlobal.search(name)):
            print("ESTA EN EL SCOPE GLOBAL")
        else:    
            logging.warning("NO EXISTE ESA VARIABLE")
