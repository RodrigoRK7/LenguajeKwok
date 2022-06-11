'''
Rodrigo de Jesús Ruíz Kwok A00824488

Clase CuboSemantico:

Clase que implementa un diccionario de diccionarios de diccionarios para 
hacer las validaciones entre las relaciones de los tipos de datos dependiendo del operador.

'''
class CuboSemantico:
    def __init__(self):
        self.cuboSemantico = {
            'int': {
                'int': {
                    "+": 'int',
                    "-": 'int',
                    "*": 'int',
                    "/": 'int',
                    ">": 'bool',
                    "<": 'bool',
                    ">=": 'bool',
                    "<=": 'bool',
                    "==": 'bool',
                    "!=": 'bool',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'int'
                },
                'float': {
                    "+": 'float',
                    "-": 'float',
                    "*": 'float',
                    "/": 'float',
                    ">": 'bool',
                    "<": 'bool',
                    ">=": 'bool',
                    "<=": 'bool',
                    "==": 'bool',
                    "!=": 'bool',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'char': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'bool': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                }
            },
            'float': {
                'int': {
                    "+": 'float',
                    "-": 'float',
                    "*": 'float',
                    "/": 'float',
                    ">": 'bool',
                    "<": 'bool',
                    ">=": 'bool',
                    "<=": 'bool',
                    "==": 'bool',
                    "!=": 'bool',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'float': {
                    "+": 'float',
                    "-": 'float',
                    "*": 'float',
                    "/": 'float',
                    ">": 'bool',
                    "<": 'bool',
                    ">=": 'bool',
                    "<=": 'bool',
                    "==": 'bool',
                    "!=": 'bool',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'float'
                },
                'char': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'bool': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                }
            },
            'char': {
                'int': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'float': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'char': {
                    "+": 'char',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'bool',
                    "!=": 'bool',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'char'
                },
                'bool': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                }
            },
            'bool': {
                'int': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'float': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'char': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'Error',
                    "!=": 'Error',
                    "&&": 'Error',
                    "||": 'Error',
                    "=": 'Error'
                },
                'bool': {
                    "+": 'Error',
                    "-": 'Error',
                    "*": 'Error',
                    "/": 'Error',
                    ">": 'Error',
                    "<": 'Error',
                    ">=": 'Error',
                    "<=": 'Error',
                    "==": 'bool',
                    "!=": 'bool',
                    "&&": 'bool',
                    "||": 'bool',
                    "=": 'Error'
                }
            }
        }

    def get(self, tipoIzq, tipoDer, operator):
        return self.cuboSemantico[tipoIzq][tipoDer][operator]