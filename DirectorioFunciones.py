import logging
from SymbolTable import SymbolTable

class Singleton(type):
    _instances = {}
    def __call__(clase, *args: any, **kwds: any):
        if clase not in clase._instances:
            instance = super().__call__(*args, **kwds)
            clase._instances[clase] = instance
        return clase._instances[clase]

class DirectorioFunciones(metaclass=Singleton):
    def __init__(self):
        self.funciones = {}
    
    def get(self, moduleName):
        if(moduleName in self.funciones):
            return self.funciones[moduleName]
        logging.warning("NO EXISTE ESE MODULO")
    
    def add(self, moduleName):
        if(moduleName in self.funciones):
            logging.warning("YA EXISTE EL MODULO")
        self.funciones[moduleName] = SymbolTable()
