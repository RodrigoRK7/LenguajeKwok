from tarfile import SYMTYPE
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
                 
    def verify(self, name):
        if(name in self.funciones.keys()):
            return True
        else:
            return False
    
    def add(self, moduleName):
        self.funciones[moduleName] = SymbolTable()
        ''' self.funciones = {
            moduleName:{
                "Type": type, 
                "Direction": direction, 
                "Parameters": [],
                "NumberParameters": 0,
                "SymbolTable": SymbolTable()
                }
            }
            '''
        
