import sys
from tkinter.dialog import DIALOG_ICON
import ply.lex as lex
import ply.yacc as yacc
from DirectorioFunciones import DirectorioFunciones
from SymbolTable import DirectorioGlobal
from Cuadruplos import Cuadruplos

reserverdWords = {
    'program' : 'PROGRAM',
    'int' : 'INT',
    'var' : 'VAR',
    'float' : 'FLOAT',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'read' : 'READ',
    'plot' : 'PLOT',
    'function' : 'FUNCTION',
    'void' : 'VOID',
    'char' : 'CHAR',
    'main' : 'MAIN',
    'while' : 'WHILE',
    'for' : 'FOR',
    'normal' : 'NORMAL',
    'binomial' : 'BINOMIAL',
    'min' : 'MIN',
    'max' : 'MAX',
    'sum' : 'SUM',
    'uniforme' : 'UNIFORME',
    'poisson' : 'POISSON',
    'return' : 'RETURN'
}

tokens = [
    'ID', 'CTEINT', 'CTFLOAT', 'PARENOPEN', 'PARENCLOSE', 'SEMICOLON', 'BRACEOPEN', 
    'BRACECLOSE', 'GREATHERTHAN', 'LESSTHAN', 'DIFFERENT', 'CTESTRING', 'EQUAL', 'DIVIDE', 'MULTIPLY', 'PLUS', 'MINUS',
    'BRACKETOPEN', 'BRACKETCLOSE', 'COLON', 'SAME', "GREATHEREQUAL", "LESSEQUAL", "AND", "OR"
] + list(reserverdWords.values())

t_SEMICOLON = r'\;'
t_COLON = r'\,'
t_BRACKETOPEN = r'\{'
t_BRACKETCLOSE = r'\}'
t_BRACEOPEN = r'\['
t_BRACECLOSE = r'\]'
t_EQUAL = r'\='
t_SAME = r'\=='
t_PARENOPEN = r'\('
t_PARENCLOSE = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_GREATHERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_GREATHEREQUAL = r'\>='
t_LESSEQUAL = r'\<='
t_DIFFERENT = r'\!='
t_AND = r'\&&'
t_ignore = r' '

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserverdWords.get(t.value, 'ID')
    return t

def t_CTEINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTESTRING(t):
    r'(\")([A-Za-z0-9]|[ \t\n] | (\() | (\))) + (\")'
    t.value = str(t.value)
    return t

def t_error(t):
    print("HAY UN ERROR")
    t.lexer.skip(1)

lexer = lex.lex()

operadores = []
operandos = []
tipos = []
lista_cuadruplos = []
directorioFunciones = DirectorioFunciones()
directorioFunciones.add("global")
tablaGlobal = directorioFunciones.get("global")
temporal = 1

def p_start_program(p):
    '''
    start_program : PROGRAM ID SEMICOLON vars multiple_funcs main_body
    | PROGRAM ID SEMICOLON vars main_body
    | PROGRAM ID SEMICOLON multiple_funcs main_body
    | PROGRAM ID SEMICOLON main_body
    '''
    p[0] = "COMPILED"

    print("Pila de tipos: ", tipos)
    print("Pila de operandos: ",operandos)
    print("Pila de operadores: ",operadores)
    print("Directorio Global: ", directorioFunciones.get("global").variables)
    #print("Tabla de variables: ", directorioFunciones.get("media").variables)
    for index, i in enumerate(lista_cuadruplos):
        print(str(index+1)+".-", i.get())


def p_multiple_funcs(p):
    '''
    multiple_funcs : dec_func 
    | dec_func multiple_funcs
    '''
def p_main_body(p):
    '''
    main_body : MAIN body
    '''

def p_vars(p):
    '''
    vars : VAR varss
    '''
   ## print(p[:])

def p_varss(p):
    '''
    varss : type mvar SEMICOLON varss
    | type mvar SEMICOLON
    '''
    ##print(p[:])
    tipos.append(p[1])
    tablaGlobal.add(operandos.pop(), tipos.pop())


def p_mvar(p):
    '''
    mvar : ID COLON mvar
    | ID BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID 
    | ID BRACEOPEN CTEINT BRACECLOSE 
    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE 
    '''
   ## print(p[:])
    operandos.append(p[1])
    print("Llevo estos operandos (mvar): ", operandos)

def p_dec_func(p):
    '''
    dec_func : FUNCTION type ID PARENOPEN param PARENCLOSE body
    | FUNCTION VOID ID PARENOPEN param PARENCLOSE body

    '''
    ##print(p[:])
    tipos.append(p[2])
    operandos.append(p[3])
    print("Llevo estos operandos (dec_func): ", operandos)
    directorioFunciones.add(p[3])


def p_param(p):
    '''
    param : type variable
    | type variable COLON param
    | empty

    '''
    ##print(p[:])
    #operandos.append(p[1])
    
def p_type(p):
    '''
    type : INT
    | FLOAT
    | CHAR
    '''
    p[0] = p[1]

def p_body(p):
    '''
    body : BRACKETOPEN bodyy BRACKETCLOSE
    '''

def p_bodyy(p):
    '''
    bodyy : statement 
    | statement bodyy
    | empty

    '''

def p_statement(p):
    '''
    statement : dec_variables 
    | assignment
    | condition
    | writing
    | reading
    | call_func
    | graph
    | return
    | while_loop
    | for_loop
    | max
    | min
    | sum
    | normal
    | uniforme
    | poisson
    | binomial
    '''
def p_dec_variables(p):
    '''
    dec_variables : dec_variabless
    '''
    #print(p[:])

def p_dec_variabless(p):
    '''
    dec_variabless : type dec_mvar SEMICOLON dec_variabless
    | type dec_mvar SEMICOLON
    '''
    ##print(p[:])
    tipos.append(p[1])
    ##tabla_Variables.add(operandos.pop(), tipos.pop())

def p_dec_mvar(p):
    '''
    dec_mvar : ID COLON dec_mvar
    | ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar
    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar
    | ID 
    | ID BRACEOPEN CTEINT BRACECLOSE 
    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE 
    '''
   ## print(p[:])
    operandos.append(p[1])
    print("Llevo estos operandos (dec_mvar): ", operandos)
    lista_cuadruplos.append(Cuadruplos("dec_var","","", p[1]))

def p_assignment(p):
    '''
    assignment : variable EQUAL exp SEMICOLON
    '''
    print(p[:])
    if p[2] and len(p) > 4:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        global temporal
        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, "t"+str(temporal)))
        operandos.append("t"+str(temporal))
        temporal = temporal + 1
    

def p_call_func(p):
    '''
    call_func : ID PARENOPEN call_funcc PARENCLOSE

    '''
def p_call_funcc(p):
    '''
    call_funcc : exp 
    | exp COLON call_funcc
    | empty
    '''
def p_graph(p):
    '''
    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON
    
    '''
def p_exp(p):
    '''
    exp : m_exp GREATHERTHAN m_exp 
    | m_exp LESSTHAN m_exp 
    | m_exp GREATHEREQUAL m_exp 
    | m_exp LESSEQUAL m_exp 
    | m_exp DIFFERENT m_exp 
    | m_exp SAME m_exp
    | m_exp AND m_exp
    | m_exp OR m_exp
    | m_exp

    '''
    print(p[:])
    if len(p) >= 3 and p[2]:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        global temporal
        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, "t"+str(temporal)))
        operandos.append("t"+str(temporal))
        temporal = temporal + 1

def p_m_exp(p):
    '''
    m_exp : t m_expp
    '''

def p_m_expp(p):
    '''
    m_expp : PLUS m_exp 
        | MINUS m_exp 
        | empty
    '''
    ##print(p[:])
    if p[1] and len(p) > 2:
        operadores.append(p[1])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        global temporal
        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, "t"+str(temporal)))
        operandos.append("t"+str(temporal))
        temporal = temporal + 1

def p_t(p):
    '''
    t : f termino
    '''
    

def p_termino(p):
    '''
    termino : MULTIPLY t 
        | DIVIDE t 
        | empty
    '''
    #print(p[:]) 
    if p[1] and len(p) > 2:
        operadores.append(p[1])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        global temporal
        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, "t"+str(temporal)))
        operandos.append("t"+str(temporal))
        temporal = temporal + 1

def p_f(p):
    '''
    f : PARENOPEN exp PARENCLOSE 
    | PLUS ID
    | MINUS ID
    | ID
    | PLUS CTEINT
    | MINUS CTEINT
    | CTEINT
    | PLUS CTFLOAT
    | MINUS CTFLOAT
    | CTFLOAT 
    | variable
    | call_func
    '''
    #print(p[:])
    #print(p[:])
    if len(p) == 2:
        operandos.append(p[1])

def p_variable(p):
    '''
    variable : ID 
    | ID BRACEOPEN exp BRACECLOSE 
    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE
    '''
    #print(p[:])
    if len(p) >= 2 and p[1]:
        operandos.insert(0,p[1])

def p_condition(p):
    '''
    condition : IF PARENOPEN exp PARENCLOSE body  
        | IF PARENOPEN exp PARENCLOSE body ELSE body 
    '''
def p_writing(p):
    '''
    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON
    '''

def p_writingg(p):
    '''
    writingg : exp
    | exp COLON writingg
    | CTESTRING 
    | CTESTRING COLON writingg
    '''
def p_reading(p):
    '''
    reading : READ multivariables SEMICOLON
       
    '''
def p_multivariables(p):
    '''
    multivariables : variable
    | variable COLON multivariables
       
    '''
def p_while_loop(p):
    '''
    while_loop : WHILE PARENOPEN exp PARENCLOSE body
       
    '''
def p_for_loop(p):
    '''
    for_loop : FOR PARENOPEN for_assignment SEMICOLON exp SEMICOLON for_assignment PARENCLOSE body
       
    '''
def p_for_assignment(p):
    '''
    for_assignment : variable EQUAL exp
       
    '''
def p_return(p):
    '''
    return : RETURN exp SEMICOLON
       
    '''
def p_max(p):
    '''
    max : MAX PARENOPEN exp PARENCLOSE SEMICOLON
       
    '''
def p_min(p):
    '''
    min : MIN PARENOPEN exp PARENCLOSE SEMICOLON
       
    '''
def p_sum(p):
    '''
    sum : SUM PARENOPEN exp PARENCLOSE SEMICOLON
       
    '''
def p_param_dist(p):
    '''
    param_dist : variable
    | variable COLON param_dist
       
    '''
def p_binomial(p):
    '''
    binomial : BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON
       
    '''
def p_poisson(p):
    '''
    poisson : POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON
       
    '''
def p_uniforme(p):
    '''
    uniforme : UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON
       
    '''
def p_normal(p):
    '''
    normal : NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON
       
    '''
def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
   print("HAY UN ERROR")


parser = yacc.yacc()

if __name__ == '__main__':
    try:
        archivo = open('test1.txt','r')
        datos = archivo.read()
        archivo.close()
        if(yacc.parse(datos, tracking=True) == 'COMPILED'):
            print("\nAPROPIADO: ANALISIS CONCLUIDO SIN ERRORES")
        else:
            print("SE PRODUJO UN ERROR DURANTE EL ANALISIS")
    except EOFError:
        print(EOFError)