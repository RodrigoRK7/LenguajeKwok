'''
Rodrigo de Jesús Ruíz Kwok A00824488

Clase Singleton:

Clase utilizada para la implementación del patrón de diseño Singleton para generar solo 
una instancia de una clase.

'''
from SymbolTable import SymbolTable

class Singleton(type):
    _instances = {}
    def __call__(clase, *args: any, **kwds: any):
        if clase not in clase._instances:
            instance = super().__call__(*args, **kwds)
            clase._instances[clase] = instance
        return clase._instances[clase]

'''
Rodrigo de Jesús Ruíz Kwok A00824488

Clase DirectorioFunciones:

Clase que implementa el patron de diseño Singleton para que solo exista un directorio de funciones.
Se implementa un metodo get para obtener el nombre de una función, verify para validar si existe una función
y add para agregar una instancia de SymbolTable a cada función.

'''
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
        
