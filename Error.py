'''
Rodrigo de Jesús Ruíz Kwok A00824488

Clase Error:

Clase utilizada para desplegar errores utilizando "raise" para parar la ejecución del programa.

'''
class Error(Exception):
    def __init__(self, message):
        self.message = message