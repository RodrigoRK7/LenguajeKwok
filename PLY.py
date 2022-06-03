import sys
from turtle import goto
import ply.lex as lex
import ply.yacc as yacc
from DirectorioFunciones import DirectorioFunciones
from SymbolTable import DirectorioGlobal
from Cuadruplos import Cuadruplos

class Error(Exception):
    def __init__(self, message):
        self.message = message

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
    'return' : 'RETURN',
    'to': 'TO'
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
    r'"(.*?)"'
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
saltos = []
operandos_verificar = []
contexto = ["global"]
directorioFunciones = DirectorioFunciones()
directorioFunciones.add("global")
tablaGlobal = directorioFunciones.get("global")
temporal = 1


def p_start_program(p):
    '''
    start_program : cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body
    | cuadruploMain PROGRAM ID SEMICOLON vars main_body
    | cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body
    | cuadruploMain PROGRAM ID SEMICOLON main_body
    '''
    p[0] = "COMPILED"

    print("Pila de tipos: ", tipos)
    print("Pila de operandos: ",operandos)
    print("Pila de operadores: ",operadores)
    print("Pila de saltos: ", saltos)
    print("Directorio Global: ", directorioFunciones.get("global").variables)
    print("Tabla de promedio: ", directorioFunciones.get("promedio").variables)
    print("Tabla de hola: ", directorioFunciones.get("hola").variables)
    print("Tabla de main: ", directorioFunciones.get("main").variables)
    
    for index, i in enumerate(lista_cuadruplos):
        print(str(index+1)+".-", i.get())

def p_cuadruploMain(p):
    '''
    cuadruploMain : empty
    '''
    #Goto para el main
    lista_cuadruplos.append(Cuadruplos("GOTO","" , "", ""))
    #Guardamos el index actual para luego reemplazar el cuadruplo GOTO por uno completo
    saltos.append(len(lista_cuadruplos)-1)

def p_multiple_funcs(p):
    '''
    multiple_funcs : dec_func 
    | dec_func multiple_funcs
    '''
def p_main_body(p):
    '''
    main_body : MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body 
    '''
def p_crearTablaMain(p):
    '''
    crearTablaMain : empty
    '''
    contexto.append("main")
    directorioFunciones.add("main")

def p_gotoMain(p):
    '''
    gotoMain : empty
    '''
    saltos.append(len(lista_cuadruplos)+1)
    print(saltos)
    #Cambiar el GOTOF incompleto por el completo
    goto = saltos.pop()
    
    #Index del GOTOF incompleto
    index = saltos.pop()

    #Cambiar el GOTOF incompleto por el completo
    lista_cuadruplos.pop(index)
    lista_cuadruplos.insert(index, Cuadruplos("GOTO","" , "", goto))

def p_vars(p):
    '''
    vars : VAR varss
    '''
   ## print(p[:])

def p_varss(p):
    '''
    varss : type guardarTipo mvar SEMICOLON varss
    | type guardarTipo mvar SEMICOLON
    '''
    #print(p[:])
    tipos.pop()

def p_guardarTipo(p):
    '''
    guardarTipo : empty
    '''
    #print(p[-1])
    tipos.append(p[-1])
    #tablaGlobal.add(operandos.pop(), tipos.pop())

def p_mvar(p):
    '''
    mvar : ID COLON mvar
    | ID BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID 
    | ID BRACEOPEN CTEINT BRACECLOSE 
    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE 
    '''
    #print(p[:])
    operandos.append(p[1])
    tipo = tipos[-1]
    tipos.append(tipo)
    variable = operandos.pop()
    if tablaGlobal.verify(variable):
        raise Error("NOMBRES DE VARIABLES REPETIDOS DENTRO DE LA MISMA FUNCION")
    else:
        tablaGlobal.add(variable, tipos.pop())
    print("Llevo estos operandos (mvar): ", operandos)

def p_dec_func(p):
    '''
    dec_func : FUNCTION type ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc
    | FUNCTION VOID ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc
    '''
    #print(p[:])
    #tipos.append(p[2])
    #operandos.append(p[3])
    print("Llevo estos operandos (dec_func): ", operandos)

def p_crearSymbolTable(p):
    '''
    crearSymbolTable : empty
    '''
    #print(p[-1])
    contexto.append(p[-1])
    #print(contexto)
    if directorioFunciones.verify(p[-1]) == 1:
        print("HAY UN ERROR")
        raise Error("NOMBRE DE FUNCION REPETIDO")
    else:
        directorioFunciones.add(p[-1])
    #tablaVariables = directorioFunciones.get(p[-1])

def p_exitFunc(p):
    '''
    exitFunc : empty
    '''
    contexto.pop()

def p_param(p):
    '''
    param : typeParam ID
    | typeParam ID COLON param
    | empty
    '''
    #print(p[:])
    if len(p) > 2:
        operandos.append(p[2])
        tablaVar = directorioFunciones.get(contexto[-1])
        variable = operandos.pop()
        if tablaVar.verify(variable):
            raise Error("NOMBRES DE VARIABLES REPETIDOS DENTRO DE LA MISMA FUNCION")
        else:
            if directorioFunciones.verify(variable):
                raise Error("NOMBRES DE VARIABLES-FUNCIONES REPETIDOS")
            else:
                tablaVar.add(variable, tipos.pop())
    

def p_typeParam(p):
    '''
    typeParam : INT
    | FLOAT
    | CHAR
    '''
    #print(p[:])
    if p[1]:
        tipos.append(p[1])

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
    dec_variabless : type guardarTipo dec_mvar SEMICOLON dec_variabless
    | type guardarTipo dec_mvar SEMICOLON
    '''
    #print(p[:])
    #print(p[:])
    tipos.pop()
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
    #print("AAAAAAAAAAAAA",p[:])
    operandos.append(p[1])
    tipo = tipos[-1]
    tipos.append(tipo)
    tablaVar = directorioFunciones.get(contexto[-1])
    variable = operandos.pop()
    if tablaVar.verify(variable):
        raise Error("NOMBRES DE VARIABLES REPETIDOS DENTRO DE LA MISMA FUNCION")
    else:
        if directorioFunciones.verify(variable):
            raise Error("NOMBRES DE VARIABLES-FUNCIONES REPETIDOS")
        else:
            tablaVar.add(variable, tipos.pop())

    #print("Llevo estos operandos (dec_mvar): ", operandos)
    #tablaGlobal.ad
    #lista_cuadruplos.append(Cuadruplos("dec_var","","", p[1]))

def p_assignment(p):
    '''
    assignment : variable EQUAL exp SEMICOLON
    '''
    #print("Entré en Assignment y la pila de operandos va: ",p[-1])
    #print("Entré en Assignment y la pila de operadores va ",operadores)
   # print(p[:])
    if p[2] and len(p) > 4:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoIzq = operandos.pop()
        operandoDer = operandos.pop()
        global temporal
        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, "", operandoDer))
    #print("Salí de Assignment y la pila de operandos va: ",operandos)
    #print("Salí de Assignment y la pila de operadores va ",operadores)

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
    exp : exp GREATHERTHAN exp 
    | exp LESSTHAN exp 
    | exp GREATHEREQUAL exp 
    | exp LESSEQUAL exp 
    | exp DIFFERENT exp 
    | exp SAME exp
    | exp AND exp
    | exp OR exp
    | m_exp
    '''
    #print(p[:])
    #print("Entré en exp y la pila de operandos va: ",operandos)
    #print("Entré en exp y la pila de operadores va ",operadores)
    if len(p) >= 3 and p[2]:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        global temporal
        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, "t"+str(temporal)))
        operandos.append("t"+str(temporal))
        temporal = temporal + 1
    #print("Salí de exp y la pila de operandos va: ",operandos)
    #print("Salí de exp y la pila de operadores va ",operadores)


def p_m_exp(p):
    '''
    m_exp : t m_expp 
    '''
    #print("Entré en m_exp y la pila de operandos va: ",operandos)
    #print("Entré en m_exp y la pila de operadores va ",operadores)
    #print(p[:])
    
    #print("Salí de m_exp y la pila de operandos va: ",operandos)
    #print("Salí de m_exp y la pila de operadores va ",operadores)

def p_m_expp(p):
    '''
    m_expp : PLUS appendPLUS m_exp
        | MINUS appendMINUS m_exp
        | empty
    '''
    #print(p[:])
    #print("Entré en m_expp y la pila de operandos va: ",operandos)
    #print("Entré en m_expp y la pila de operadores va ",operadores)
    #if p[1] and len(p) > 2:
    #print("Salí de m_expp y la pila de operandos va: ",operandos)
    #print("Salí de m_expp y la pila de operadores va ",operadores)

def p_appendPLUS(p):
    '''
    appendPLUS : empty
    '''
    operadores.append("+")

def p_appendMINUS(p):
    '''
    appendMINUS : empty
    '''
    operadores.append("-")

def p_appendMULTIPLY(p):
    '''
    appendMULTIPLY : empty
    '''
    operadores.append("*")

def p_appendDIVIDE(p):
    '''
    appendDIVIDE : empty
    '''
    operadores.append("/")

def p_t(p):
    '''
    t : f termino
    '''
    #print(p[:])
    #print(p[-1])
    #print("Entré en t y la pila de operandos va: ",operandos)
    #print("Entré en t y la pila de operadores va ",operadores)
    if(len(operadores) > 0 and (operadores[len(operadores)-1] == "+" or operadores[len(operadores)-1] == "-")):
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        global temporal
        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, "t"+str(temporal)))
        operandos.append("t"+str(temporal))
        temporal = temporal + 1
    #print("Salí de t y la pila de operandos va: ",operandos)
    #print("Salí de t y la pila de operadores va ",operadores)
    

def p_termino(p):
    '''
    termino : MULTIPLY appendMULTIPLY t 
        | DIVIDE appendDIVIDE t 
        | empty
    '''
    #print("termino", p[:])
    #print("Entré en termino y la pila de operandos va: ",operandos)
    #print("Entré en termino y la pila de operadores va ",operadores)
    #if p[1] and len(p) > 2:
    #print("Salí de termino y la pila de operandos va: ",operandos)
    #print("Salí de termino y la pila de operadores va ",operadores)

def p_f(p):
    '''
    f : PARENOPEN exp PARENCLOSE 
    | ID
    | CTEINT
    | CTFLOAT 
    | variable
    | call_func
    '''
    #print(p[:])
    #print(p[-1])
    #print("Entré de f y la pila de operandos va: ",operandos)
    #print("Entré de f y la pila de operadores va ",operadores)
    if len(p) == 2:
        declarada = False
        tablaVar = directorioFunciones.get(contexto[-1])
        #variable = operandos.pop()
        if tablaVar.verify(p[1]):
            declarada = True
        else:
            if directorioFunciones.get("global").verify(p[1]):
                declarada = True
            else:
                print("No declarada")
                raise Error("VARIABLE NO DECLARADA")
        
        if declarada:
            operandos.append(p[1])
            if(len(operadores) > 0 and (operadores[len(operadores)-1] == "*" or operadores[len(operadores)-1] == "/")):
                operador = operadores.pop()
                operandoDer = operandos.pop()
                operandoIzq = operandos.pop()
                global temporal
                lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, "t"+str(temporal)))
                operandos.append("t"+str(temporal))
                temporal = temporal + 1
    #print("Salí de f y la pila de operandos va: ",operandos)
    #print("Salí de f y la pila de operadores va ",operadores)

def p_variable(p):
    '''
    variable : ID 
    | ID BRACEOPEN exp BRACECLOSE 
    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE
    '''
    #print(p[:])
    #print("Entré de variable y la pila de operandos va: ",operandos)
    #print("Entré de variable y la pila de operadores va ",operadores)
    if len(p) >= 2 and p[1]:
        operandos.append(p[1])
    #print("Salí de variable y la pila de operandos va: ",operandos)
    #print("Salí de variable y la pila de operadores va ",operadores)

def p_condition(p):
    '''
    condition : IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd
        | IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse
    '''
def p_cuadruploIF(p):
    '''
    cuadruploIF : empty 
    '''
    #Obtener la expresion a evaluar
    resultado = operandos.pop()
    #Posicion para insertar el GotoF
    lista_cuadruplos.append(Cuadruplos("GOTOF",resultado , "", ""))
    
    #Guardamos el index actual para luego reemplazar el cuadruplo GOTOF por uno completo
    saltos.append(len(lista_cuadruplos)-1)

    #Guardamos la expresion a estar evaluando para cuando armemos el GOTOF completo
    operandos_verificar.append(resultado)
    
def p_ifEnd(p):
    '''
    ifEnd : empty 
    '''
    saltos.append(len(lista_cuadruplos)+1)
    #Obtener la expresion a evaluar
    resultado = operandos_verificar.pop()

    #Cambiar el GOTOF incompleto por el completo
    gotoF = saltos.pop()
    
    #Index del GOTOF incompleto
    index = saltos.pop()

    #Cambiar el GOTOF incompleto por el completo
    lista_cuadruplos.pop(index)
    lista_cuadruplos.insert(index, Cuadruplos("GOTOF",resultado , "", gotoF))

def p_cuadruploElse(p):
    '''
    cuadruploElse : empty 
    '''
    #Posicion para insertar el Goto
    lista_cuadruplos.append(Cuadruplos("GOTO", "", "", ""))
    
    #Posicion saliendo del else
    saltos.append(len(lista_cuadruplos)+1)

    #Obtener la expresion a evaluar
    resultado = operandos_verificar.pop()

    #Cambiar el GOTOF incompleto por el completo
    gotoF = saltos.pop()
    
    #Index del GOTOF incompleto
    index = saltos.pop()

    #Cambiar el GOTOF incompleto por el completo
    lista_cuadruplos.pop(index)
    lista_cuadruplos.insert(index, Cuadruplos("GOTOF",resultado , "", gotoF))
    
    #Posicion del GOTO
    saltos.append(len(lista_cuadruplos)-1)


def p_ifEndElse(p):
    '''
    ifEndElse : empty 
    '''
    #Agregar el index actual (+1 para salir del else)
    saltos.append(len(lista_cuadruplos)+1)

    #Cambiar el GOTO incompleto por el completo
    goto = saltos.pop()
    index = saltos.pop()
    lista_cuadruplos.pop(index)
    lista_cuadruplos.insert(index, Cuadruplos("GOTO","", "", goto))

def p_writing(p):
    '''
    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON
    '''
    #print(p[:])

def p_writingg(p):
    '''
    writingg : exp
    | exp COLON writingg
    | auxString
    | auxString COLON writingg
    '''
    #print(p[:])
    #print(operandos)
    operadores.append("print")
    #print(operandos)
    operador = operadores.pop()
    operandoDer = operandos.pop(0)
    global temporal
    lista_cuadruplos.append(Cuadruplos(operador, "", "", operandoDer))
    #print(operandos)

def p_auxString(p):
    '''
    auxString : CTESTRING
       
    '''
    if(p[1]):
        operandos.append(p[1])

def p_reading(p):
    '''
    reading : READ multivariables SEMICOLON
       
    '''
def p_multivariables(p):
    '''
    multivariables : variable
    | variable COLON multivariables
       
    '''
    #print(p[:])
    operadores.append("read")
    operador = operadores.pop()
    operandoDer = operandos.pop()
    global temporal
    lista_cuadruplos.append(Cuadruplos(operador, "", "", operandoDer))

def p_while_loop(p):
    '''
    while_loop : WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd
       
    '''
def p_whileMigaja(p):
    '''
    whileMigaja : empty
       
    '''
    #Se suma 1 porque las listas inician en 0
    saltos.append(len(lista_cuadruplos) + 1)

def p_whileEval(p):
    '''
    whileEval : empty
       
    '''
    #Obtenemos la expresion a estar evaluando
    resultado = operandos.pop()
    
    #Reservamos el espacio para el GOTOF
    lista_cuadruplos.append(Cuadruplos("GOTOF",resultado , "", ""))
    
    #Guardamos el index actual para luego reemplazar el cuadruplo GOTOF por uno completo
    saltos.append(len(lista_cuadruplos)-1)

    #Guardamos la expresion a estar evaluando para cuando armemos el GOTOF completo
    operandos_verificar.append(resultado)

def p_whileEnd(p):
    '''
    whileEnd : empty
       
    '''
    #Guardar el index en el que acaba el while (se suma 2 para direccionar a lo que sigue fuera del while)
    saltos.append(len(lista_cuadruplos)+2)
    
    #Cambiar el GOTOF incompleto por el completo
    gotoF = saltos.pop()

    #Index del GOTOF incompleto
    index = saltos.pop()
    lista_cuadruplos.pop(index)

    #Obtener la expresion a evaluar
    resultado = operandos_verificar.pop()

    lista_cuadruplos.insert(index, Cuadruplos("GOTOF",resultado , "", gotoF))

    #Obtener el index del cuadruplo que obtiene la expresion a evaluar para regresar a reevaluar la expresion
    goto = saltos.pop()
    
    #Generar el GOTO
    lista_cuadruplos.append(Cuadruplos("GOTO","", "", goto))    
    #saltos.append(len(lista_cuadruplos)+1)
    #gotof = saltos.pop(0)

def p_for_loop(p):
    '''
    for_loop : FOR PARENOPEN variable EQUAL exp guardarValorFor TO exp PARENCLOSE body forEnd

    '''

def p_guardarValorFor(p):
    '''
    guardarValorFor : empty

    '''
    exp = operandos.pop()
    #vcontrol = operandos.top()
    print(exp)
    #print(vcontrol)

def p_forEnd(p):
    '''
    forEnd : empty

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
   raise Error("HAY UN ERROR")


parser = yacc.yacc()

if __name__ == '__main__':
    try:
        archivo = open('test6.txt','r')
        datos = archivo.read()
        archivo.close()
        if(yacc.parse(datos, tracking=True) == 'COMPILED'):
            print("\nAPROPIADO: ANALISIS CONCLUIDO SIN ERRORES")
        else:
            print("SE PRODUJO UN ERROR DURANTE EL ANALISIS")
    except EOFError:
        print(EOFError)