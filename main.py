from SymbolTable import SymbolTable
from DirectorioFunciones import DirectorioFunciones
import logging 

def main():
    """
    symbolTable = SymbolTable()
    symbolTable.search("var")
    symbolTable.add("a","int")
    print (symbolTable.search("a"))"""

    directorioFunciones = DirectorioFunciones()
    directorioFunciones1 = DirectorioFunciones()
    directorioFunciones.add("global")
    directorioFunciones.add("funcion1")
    tablaGlobal = directorioFunciones.get("global")
    tablaGlobal.add("a", "double")
    print(directorioFunciones.get("global").search("a"))
    print(directorioFunciones.get("funcion1").search("a"))
    print(directorioFunciones1.get("global").search("a"))

if __name__ == "__main__": 
    main()