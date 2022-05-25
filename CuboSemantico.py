from enum import Enum
class Operators(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    GREATHERTHAN = ">"
    LESSTHAN = "<"
    GREATHEREQUAL = ">="
    LESSEQUAL = "<="
    EQUAL = "="
    AND = "and"
    OR = "or"
    SAME = "=="
    DIFFERENT = "!="

class CuboSemantico:
    def __init__(self):
        self.cuboSemantico = {
            'int': {
                'int': {
                    Operators.PLUS: 'int',
                    Operators.MINUS: 'int',
                    Operators.MULTIPLY: 'int',
                    Operators.DIVIDE: 'int',
                    Operators.GREATHERTHAN: 'bool',
                    Operators.LESSTHAN: 'bool',
                    Operators.GREATHEREQUAL: 'bool',
                    Operators.LESSEQUAL: 'bool',
                    Operators.SAME: 'bool',
                    Operators.DIFFERENT: 'bool',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'int'
                },
                'float': {
                    Operators.PLUS: 'float',
                    Operators.MINUS: 'float',
                    Operators.MULTIPLY: 'float',
                    Operators.DIVIDE: 'float',
                    Operators.GREATHERTHAN: 'bool',
                    Operators.LESSTHAN: 'bool',
                    Operators.GREATHEREQUAL: 'bool',
                    Operators.LESSEQUAL: 'bool',
                    Operators.SAME: 'bool',
                    Operators.DIFFERENT: 'bool',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'int'
                },
                'char': {
                    Operators.PLUS: 'Error',
                    Operators.MINUS: 'Error',
                    Operators.MULTIPLY: 'Error',
                    Operators.DIVIDE: 'Error',
                    Operators.GREATHERTHAN: 'Error',
                    Operators.LESSTHAN: 'Error',
                    Operators.GREATHEREQUAL: 'Error',
                    Operators.LESSEQUAL: 'Error',
                    Operators.SAME: 'Error',
                    Operators.DIFFERENT: 'Error',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'Error'
                }
            },
            'float': {
                'int': {
                    Operators.PLUS: 'float',
                    Operators.MINUS: 'float',
                    Operators.MULTIPLY: 'float',
                    Operators.DIVIDE: 'float',
                    Operators.GREATHERTHAN: 'bool',
                    Operators.LESSTHAN: 'bool',
                    Operators.GREATHEREQUAL: 'bool',
                    Operators.LESSEQUAL: 'bool',
                    Operators.SAME: 'bool',
                    Operators.DIFFERENT: 'bool',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'float'
                },
                'float': {
                    Operators.PLUS: 'float',
                    Operators.MINUS: 'float',
                    Operators.MULTIPLY: 'float',
                    Operators.DIVIDE: 'float',
                    Operators.GREATHERTHAN: 'bool',
                    Operators.LESSTHAN: 'bool',
                    Operators.GREATHEREQUAL: 'bool',
                    Operators.LESSEQUAL: 'bool',
                    Operators.SAME: 'bool',
                    Operators.DIFFERENT: 'bool',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'float'
                },
                'char': {
                    Operators.PLUS: 'Error',
                    Operators.MINUS: 'Error',
                    Operators.MULTIPLY: 'Error',
                    Operators.DIVIDE: 'Error',
                    Operators.GREATHERTHAN: 'Error',
                    Operators.LESSTHAN: 'Error',
                    Operators.GREATHEREQUAL: 'Error',
                    Operators.LESSEQUAL: 'Error',
                    Operators.SAME: 'Error',
                    Operators.DIFFERENT: 'Error',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'Error'
                }
            },
            'char': {
                'int': {
                    Operators.PLUS: 'Error',
                    Operators.MINUS: 'Error',
                    Operators.MULTIPLY: 'Error',
                    Operators.DIVIDE: 'Error',
                    Operators.GREATHERTHAN: 'Error',
                    Operators.LESSTHAN: 'Error',
                    Operators.GREATHEREQUAL: 'Error',
                    Operators.LESSEQUAL: 'Error',
                    Operators.SAME: 'Error',
                    Operators.DIFFERENT: 'Error',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'Error'
                },
                'float': {
                    Operators.PLUS: 'Error',
                    Operators.MINUS: 'Error',
                    Operators.MULTIPLY: 'Error',
                    Operators.DIVIDE: 'Error',
                    Operators.GREATHERTHAN: 'Error',
                    Operators.LESSTHAN: 'Error',
                    Operators.GREATHEREQUAL: 'Error',
                    Operators.LESSEQUAL: 'Error',
                    Operators.SAME: 'Error',
                    Operators.DIFFERENT: 'Error',
                    Operators.AND: 'Error',
                    Operators.OR: 'Error',
                    Operators.EQUAL: 'Error'
                },
                'char': {
                    Operators.PLUS: 'char',
                    Operators.MINUS: 'Error',
                    Operators.MULTIPLY: 'Error',
                    Operators.DIVIDE: 'Error',
                    Operators.GREATHERTHAN: 'Error',
                    Operators.LESSTHAN: 'Error',
                    Operators.GREATHEREQUAL: 'Error',
                    Operators.LESSEQUAL: 'Error',
                    Operators.SAME: 'bool',
                    Operators.DIFFERENT: 'bool',
                    Operators.AND: 'bool',
                    Operators.OR: 'bool',
                    Operators.EQUAL: 'char'
                }
            }
        }