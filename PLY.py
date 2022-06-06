import sys
import ply.lex as lex
import ply.yacc as yacc
from DirectorioFunciones import DirectorioFunciones
from Cuadruplos import Cuadruplos
from SymbolTable import Constantes
from CuboSemantico import CuboSemantico
from MaquinaVirtual import MaquinaVirtual
from Error import Error

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
    'ID', 'CTFLOAT','CTEINT', 'PARENOPEN', 'PARENCLOSE', 'SEMICOLON', 'BRACEOPEN', 
    'BRACECLOSE', 'GREATHERTHAN', 'LESSTHAN', 'DIFFERENT', 'CTESTRING', 'EQUAL', 'DIVIDE', 'MULTIPLY', 'PLUS', 'MINUS',
    'BRACKETOPEN', 'BRACKETCLOSE', 'COLON', 'SAME', "GREATHEREQUAL", "LESSEQUAL", "AND", "OR", "CTECHAR"
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

def t_CTFLOAT(t):
    r'-?\d+?\.\d+'
    t.value = float(t.value)
    return t

def t_CTEINT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_CTESTRING(t):
    r'"(.*?)"'
    t.value = str(t.value)
    return t

def t_CTECHAR(t):
    r"'.'"
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
cubo = CuboSemantico()
directorioFunciones = DirectorioFunciones()
tablaConstantes = Constantes()
maquinaVirtual = MaquinaVirtual(lista_cuadruplos, directorioFunciones, tablaConstantes)
directorioFunciones.add("global")
tablaGlobal = directorioFunciones.get("global")
tablaGlobal.setFuncType("np")
contador_parametros = 0
contador_parametros_call = 0
tipos_param = []
validar_tipos_param = []

temporal_int = -1
temporal_bool = -1
temporal_float = -1
temporal_char = -1

espacio_temp_i = 15000
espacio_temp_f = 16000
espacio_temp_c = 17000
espacio_temp_b = 18000


def p_start_program(p):
    '''
    start_program : cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body end
    | cuadruploMain PROGRAM ID SEMICOLON vars main_body end
    | cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body end
    | cuadruploMain PROGRAM ID SEMICOLON main_body end
    '''
    p[0] = "COMPILED"

    print("Pila de tipos: ", tipos)
    print("Pila de operandos: ",operandos)
    print("Pila de operadores: ",operadores)
    print("Pila de saltos: ", saltos)
    print("//////////////////////////////////////////")
    print("Directorio Global: ", directorioFunciones.get("global").variables)
    print("Memoria global: ", directorioFunciones.get("global").memoria)
    print("Tipo de Global: ", directorioFunciones.get("global").type)
    print("//////////////////////////////////////////")
    print("Tabla de constantes: ", tablaConstantes.constantes)
    print("Memoria constantes: ", tablaConstantes.memoria)
    print("//////////////////////////////////////////")
    print("Tabla de promedio: ", directorioFunciones.get("promedio").variables)
    print("Memoria promedio: ", directorioFunciones.get("promedio").memoria)
    print("Tipo de promedio: ", directorioFunciones.get("promedio").type)
    print("NumParam de promedio: ", directorioFunciones.get("promedio").numParam)
    print("TiposParam de promedio: ", directorioFunciones.get("promedio").tipos_Param)
    print("Inicia en el cuadruplo: ", directorioFunciones.get("promedio").dirV)
    print("//////////////////////////////////////////")
    print("Tabla de hola: ", directorioFunciones.get("hola").variables)
    print("Memoria hola: ", directorioFunciones.get("hola").memoria)
    print("Tipo de hola: ", directorioFunciones.get("hola").type)
    print("NumParam de hola: ", directorioFunciones.get("hola").numParam)
    print("TiposParam de hola: ", directorioFunciones.get("hola").tipos_Param)
    print("Inicia en el cuadruplo: ", directorioFunciones.get("hola").dirV)
    print("//////////////////////////////////////////")
    print("Tabla de main: ", directorioFunciones.get("main").variables)
    print("Memoria main: ", directorioFunciones.get("main").memoria)
    print("Tipo de main: ", directorioFunciones.get("main").type)
    print("NumParam de main: ", directorioFunciones.get("main").numParam)
    print("//////////////////////////////////////////")
    
    #print(directorioFunciones.get("main").getType("A"))

    '''for index, i in enumerate(lista_cuadruplos):
        print(str(index+1)+".-", i.get())'''

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
    tablaMain = directorioFunciones.get("main")
    tablaMain.setFuncType("void")

def p_gotoMain(p):
    '''
    gotoMain : empty
    '''
    saltos.append(len(lista_cuadruplos)+1)
    #print(saltos)
    #Cambiar el GOTOF incompleto por el completo
    goto = saltos.pop()
    tablaMain = directorioFunciones.get("main")
    tablaMain.setDirV(goto)

    #Index del GOTOF incompleto
    index = saltos.pop()

    #Cambiar el GOTOF incompleto por el completo
    lista_cuadruplos.pop(index)
    lista_cuadruplos.insert(index, Cuadruplos("GOTO","" , "main", directorioFunciones.get("main").dirV))

def p_end(p):
    '''
    end : empty
    '''
    lista_cuadruplos.append(Cuadruplos("END","" , "", ""))

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
    mvar : ID guardarIDvar COLON mvar
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID guardarIDvar
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE 
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE 
    '''

def p_guardarIDvar(p):
    '''
    guardarIDvar : empty
    '''
     #print(p[:])
    operandos.append(p[-1])
    tipo = tipos[-1]
    tipos.append(tipo)
    variable = operandos.pop()
    if tablaGlobal.verify(variable):
        raise Error("NOMBRES DE VARIABLES REPETIDOS DENTRO DE LA MISMA FUNCION")
    else:
        tablaGlobal.addGlobal(variable, tipos.pop())
    #print("Llevo estos operandos (mvar): ", operandos)

def p_dec_func(p):
    '''
    dec_func : FUNCTION type ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc
    | FUNCTION VOID ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc
    '''
    #print(p[:])
    #tipos.append(p[2])
    #operandos.append(p[3])
    #print("Llevo estos operandos (dec_func): ", operandos)

def p_crearSymbolTable(p):
    '''
    crearSymbolTable : empty
    '''
    #print(p[-2])
    contexto.append(p[-1])
    #print(contexto)
    if directorioFunciones.verify(p[-1]):
        #print("HAY UN ERROR")
        raise Error("NOMBRE DE FUNCION REPETIDO")
    else:
        directorioFunciones.add(p[-1])
        tablaVariables = directorioFunciones.get(p[-1])
        tablaVariables.setFuncType(p[-2])

def p_exitFunc(p):
    '''
    exitFunc : empty
    '''
    lista_cuadruplos.append(Cuadruplos("ENDFUNC", "", "", ""))
    contexto.pop()
    global temporal_int
    temporal_int = -1
    
    global temporal_bool
    temporal_bool = -1
    
    global temporal_float
    temporal_float = -1
    
    global temporal_char
    temporal_char = -1
    
    global contador_parametros
    contador_parametros = 0

    global tipos_param
    tipos_param = []


def p_param(p):
    '''
    param : typeParam ID
    | typeParam ID COLON param
    | empty
    '''
    #print(p[:])
    if len(p) > 2:
        global contador_parametros
        contador_parametros = contador_parametros + 1
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
    
def p_numeroParam(p):
    '''
    numeroParam : empty
    '''
    global contador_parametros
    print("Llevo ", contador_parametros, "parametros")
    tablaVar = directorioFunciones.get(contexto[-1])
    tablaVar.setNumParam(contador_parametros)
    tablaVar.setTiposParam(tipos_param)
    print(tipos_param)

def p_typeParam(p):
    '''
    typeParam : INT
    | FLOAT
    | CHAR
    '''
    #print(p[:])
    if p[1]:
        tipos.append(p[1])
        tipos_param.append(p[1])

def p_type(p):
    '''
    type : INT
    | FLOAT
    | CHAR
    '''
    p[0] = p[1]

def p_startFunc(p):
    '''
    startFunc : empty
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    tablaVar.setDirV(len(lista_cuadruplos)+1)


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
    dec_mvar : ID guardarID COLON dec_mvar
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar
    | ID guardarID
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE 
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE 
    '''
    #print(p[:])
    ##print("Saliendo de dec_mvar", tipos)

def p_guardarID(p):
    '''
    guardarID : empty
    '''
    print(p[-1])
    operandos.append(p[-1])
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

def p_assignment(p):
    '''
    assignment : variableAssignment EQUAL exp SEMICOLON
    '''
    if p[2] and len(p) > 4:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoIzq = operandos.pop()
        operandoDer = operandos.pop()
        
        tablaVar = directorioFunciones.get(contexto[-1])
       
        #print(operandoIzq, operandoDer)
        #print(tipos)
       #Obtener el tipo del operandoIzq
        if tablaVar.verify(operandoIzq): #Ver si es local
            tipoIzq = tablaVar.getType(operandoIzq)
            memoriaI = tablaVar.getMemory(operandoIzq)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal", operandoIzq)
            tipoIzq = tipos.pop()
            if tipoIzq == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_int + espacio_temp_i
            elif tipoIzq == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_float + espacio_temp_f
            elif tipoIzq == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c
            elif tipoIzq == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c

        #Obtener el tipo del operandoDer
        if tablaVar.verify(operandoDer): #Ver si es local
            tipoDer = tablaVar.getType(operandoDer)
            memoriaD = tablaVar.getMemory(operandoDer)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal")
            tipoDer = tipos.pop()
            if tipoDer == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_int + espacio_temp_i
            elif tipoDer == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_float + espacio_temp_f
            elif tipoDer == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c
            elif tipoDer == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c

        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            #print("Saliendo de assignment", tipos)
            #lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, "", operandoDer))
            lista_cuadruplos.append(Cuadruplos(operador, memoriaI, "", memoriaD))
            tipos.pop()

def p_call_func(p):
    '''
    call_func : ID generarERA PARENOPEN call_funcc PARENCLOSE
    '''
    print(p[:])
    global contador_parametros_call
    global validar_tipos_param
    if contador_parametros_call != directorioFunciones.get(p[1]).numParam:
        raise Error("ERROR CON EL NUMERO DE PARAMETROS")
    elif directorioFunciones.get(p[1]).tipos_Param != validar_tipos_param:
        raise Error("ERROR EN LOS TIPOS DE LOS ARGUMENTOS")
    else:
        lista_cuadruplos.append(Cuadruplos("GOSUB", "", "", directorioFunciones.get(p[1]).dirV))
        contador_parametros_call = 0
        validar_tipos_param = []

def p_generarERA(p):
    '''
    generarERA : empty
    '''
    if directorioFunciones.verify(p[-1]):
        print("Si existe")
    else:
        raise Error("NO EXISTE FUNCION CON ESE NOMBRE")
    lista_cuadruplos.append(Cuadruplos("ERA", "", "", p[-1]))

def p_call_funcc(p):
    '''
    call_funcc : exp mandarParam
    | exp mandarParam COLON call_funcc
    | empty
    '''

def p_mandarParam(p):
    '''
    mandarParam : empty
    '''
    print(p[:])
    param = operandos.pop()
    
    #Obtener el tipo del parametro
    tablaVar = directorioFunciones.get(contexto[-1])
    if tablaVar.verify(param): #Ver si es local
        tipo_Validar = tablaVar.getType(param)
        memoria = tablaVar.getMemory(param)
        #print(p[1], "es local")
    elif tablaConstantes.verify(param): #Ver si es constante
        tipo_Validar = tablaConstantes.getType(param)
        memoria = tablaConstantes.getMemory(param)
    elif tablaGlobal.verify(param): #Ver si es global
        tipo_Validar = tablaGlobal.getType(param)
        memoria = tablaGlobal.getMemory(param)
        #print(p[1], "es global")
    else: #es temporal
        print("Estemporal")
        tipo_Validar = tipos.pop()
        if tipo_Validar == "int":
            if temporal_int + espacio_temp_i >= 16000:
                raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
            else:
                memoria = temporal_int + espacio_temp_i
        elif tipo_Validar == "float":
            if temporal_float + espacio_temp_f >= 17000:
                raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
            else:
                memoria = temporal_float + espacio_temp_f
        elif tipo_Validar == "char":
            if temporal_float + espacio_temp_c >= 18000:
                raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
            else:
                memoria = temporal_char + espacio_temp_c
        elif tipo_Validar == "bool":
            if temporal_bool + espacio_temp_b >= 1:
                raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
            else:
                memoria = temporal_char + espacio_temp_c


    global validar_tipos_param
    validar_tipos_param.append(tipo_Validar)
    
    global contador_parametros_call
    contador_parametros_call = contador_parametros_call + 1
    lista_cuadruplos.append(Cuadruplos("PARAM", memoria, "", "PARAM"+str(contador_parametros_call)))

def p_graph(p):
    '''
    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON
    
    '''
def p_exp(p):
    '''
    exp : expp
    | exp AND expp
    | exp OR expp
    
    '''
    global temporal_int
    global temporal_float
    global temporal_char
    global temporal_bool
    if len(p) >= 3 and p[2]:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        
        tablaVar = directorioFunciones.get(contexto[-1])
    
       #Obtener el tipo del operandoIzq
        if tablaVar.verify(operandoIzq): #Ver si es local
            tipoIzq = tablaVar.getType(operandoIzq)
            memoriaI = tablaVar.getMemory(operandoIzq)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal", operandoIzq)
            tipoIzq = tipos.pop()
            if tipoIzq == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_int + espacio_temp_i
            elif tipoIzq == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_float + espacio_temp_f
            elif tipoIzq == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c
            elif tipoIzq == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c

        #Obtener el tipo del operandoDer
        if tablaVar.verify(operandoDer): #Ver si es local
            tipoDer = tablaVar.getType(operandoDer)
            memoriaD = tablaVar.getMemory(operandoDer)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal")
            tipoDer = tipos.pop()
            if tipoDer == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_int + espacio_temp_i
            elif tipoDer == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_float + espacio_temp_f
            elif tipoDer == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c
            elif tipoDer == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c

        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_int+espacio_temp_i)))
                operandos.append(str(temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_float+espacio_temp_f)))
                operandos.append(str(temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, operandoDer, str(temporal_char+espacio_temp_c)))
                operandos.append(str(temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, str(temporal_bool+espacio_temp_b)))
                operandos.append(str(temporal_bool+espacio_temp_b))
                
            #print("Saliendo de exp", tipos)

def p_expp(p):
    '''
    expp : m_exp
    | expp GREATHERTHAN m_exp 
    | expp LESSTHAN m_exp 
    | expp GREATHEREQUAL m_exp 
    | expp LESSEQUAL m_exp 
    | expp DIFFERENT m_exp 
    | expp SAME m_exp
    '''
    global temporal_int
    global temporal_float
    global temporal_char
    global temporal_bool

    if len(p) >= 3 and p[2]:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        
        tablaVar = directorioFunciones.get(contexto[-1])
       
       #Obtener el tipo del operandoIzq
        if tablaVar.verify(operandoIzq): #Ver si es local
            tipoIzq = tablaVar.getType(operandoIzq)
            memoriaI = tablaVar.getMemory(operandoIzq)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal", operandoIzq)
            tipoIzq = tipos.pop()
            if tipoIzq == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_int + espacio_temp_i
            elif tipoIzq == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_float + espacio_temp_f
            elif tipoIzq == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c
            elif tipoIzq == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c

        #Obtener el tipo del operandoDer
        if tablaVar.verify(operandoDer): #Ver si es local
            tipoDer = tablaVar.getType(operandoDer)
            memoriaD = tablaVar.getMemory(operandoDer)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal")
            tipoDer = tipos.pop()
            if tipoDer == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_int + espacio_temp_i
            elif tipoDer == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_float + espacio_temp_f
            elif tipoDer == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c
            elif tipoDer == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c

        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_int+espacio_temp_i)))
                operandos.append(str(temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_float+espacio_temp_f)))
                operandos.append(str(temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, operandoDer, str(temporal_char+espacio_temp_c)))
                operandos.append(str(temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, str(temporal_bool+espacio_temp_b)))
                operandos.append(str(temporal_bool+espacio_temp_b))
            #print("Saliendo de expp", tipos)

def p_m_exp(p):
    '''
    m_exp : termino
    | m_exp PLUS termino
    | m_exp MINUS termino
    '''
    global temporal_int
    global temporal_float
    global temporal_char
    global temporal_bool

    if len(p) > 2:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        
        tablaVar = directorioFunciones.get(contexto[-1])
       
       #Obtener el tipo del operandoIzq
        if tablaVar.verify(operandoIzq): #Ver si es local
            tipoIzq = tablaVar.getType(operandoIzq)
            memoriaI = tablaVar.getMemory(operandoIzq)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal", operandoIzq)
            tipoIzq = tipos.pop()
            if tipoIzq == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_int + espacio_temp_i
            elif tipoIzq == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_float + espacio_temp_f
            elif tipoIzq == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c
            elif tipoIzq == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c

        #Obtener el tipo del operandoDer
        if tablaVar.verify(operandoDer): #Ver si es local
            tipoDer = tablaVar.getType(operandoDer)
            memoriaD = tablaVar.getMemory(operandoDer)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal")
            tipoDer = tipos.pop()
            if tipoDer == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_int + espacio_temp_i
            elif tipoDer == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_float + espacio_temp_f
            elif tipoDer == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c
            elif tipoDer == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c

        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_int+espacio_temp_i)))
                operandos.append(str(temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_float+espacio_temp_f)))
                operandos.append(str(temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, operandoDer, str(temporal_char+espacio_temp_c)))
                operandos.append(str(temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, str(temporal_bool+espacio_temp_b)))
                operandos.append(str(temporal_bool+espacio_temp_b))
            #print("Saliendo de m_exp", tipos)
           
def p_termino(p):
    '''
    termino : factor
    | termino MULTIPLY factor
    | termino DIVIDE factor 
    '''
    global temporal_int
    global temporal_float
    global temporal_char
    global temporal_bool

    if len(p) > 2:
        operadores.append(p[2])
        operador = operadores.pop()
        operandoDer = operandos.pop()
        operandoIzq = operandos.pop()
        
        tablaVar = directorioFunciones.get(contexto[-1])
       
       #Obtener el tipo del operandoIzq
        if tablaVar.verify(operandoIzq): #Ver si es local
            tipoIzq = tablaVar.getType(operandoIzq)
            memoriaI = tablaVar.getMemory(operandoIzq)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal", operandoIzq)
            tipoIzq = tipos.pop()
            if tipoIzq == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_int + espacio_temp_i
            elif tipoIzq == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_float + espacio_temp_f
            elif tipoIzq == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c
            elif tipoIzq == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaI = temporal_char + espacio_temp_c

        #Obtener el tipo del operandoDer
        if tablaVar.verify(operandoDer): #Ver si es local
            tipoDer = tablaVar.getType(operandoDer)
            memoriaD = tablaVar.getMemory(operandoDer)
            #print(p[1], "es local")
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
            #print(p[1], "es global")
        else: #es temporal
            print("Estemporal")
            tipoDer = tipos.pop()
            if tipoDer == "int":
                if temporal_int + espacio_temp_i >= 16000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_int + espacio_temp_i
            elif tipoDer == "float":
                if temporal_float + espacio_temp_f >= 17000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_float + espacio_temp_f
            elif tipoDer == "char":
                if temporal_float + espacio_temp_c >= 18000:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c
            elif tipoDer == "bool":
                if temporal_bool + espacio_temp_b >= 1:
                    raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                else:
                    memoriaD = temporal_char + espacio_temp_c

        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_int+espacio_temp_i)))
                operandos.append(str(temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_float+espacio_temp_f)))
                operandos.append(str(temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, operandoDer, str(temporal_char+espacio_temp_c)))
                operandos.append(str(temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, str(temporal_bool+espacio_temp_b)))
                operandos.append(str(temporal_bool+espacio_temp_b))
            #print("Saliendo de termino", tipos)

def p_factor(p):
    '''
    factor : ID 
    | CTEINT guardarConstanteInt
    | CTFLOAT guardarConstanteFloat
    | CTECHAR guardarConstanteChar
    | variable
    | call_func
    | PARENOPEN exp PARENCLOSE
    '''
    global temporal_int
    global temporal_float
    global temporal_char
    global temporal_bool
    
    if p[1] == "(":
        pass
    else:
        declarada = False
        tablaVar = directorioFunciones.get(contexto[-1])
        print(contexto)
        #variable = operandos.pop()
        if tablaVar.verify(p[1]) or tablaConstantes.verify(p[1]):
            declarada = True
            #print(p[1], "es local")
        else:
            if tablaGlobal.verify(p[1]):
                declarada = True
                #print(p[1], "es global")
            else:
                print(p[1], "No declarada")
                print(contexto[-1])
                raise Error("VARIABLE NO DECLARADA")
        
        if declarada:
            operandos.append(p[1])
            if(len(operadores) > 0 and (operadores[len(operadores)-1] == "*" or operadores[len(operadores)-1] == "/")):
                operador = operadores.pop()
                operandoDer = operandos.pop()
                operandoIzq = operandos.pop()

                tablaVar = directorioFunciones.get(contexto[-1])
       
                #Obtener el tipo del operandoIzq
                if tablaVar.verify(operandoIzq): #Ver si es local
                    tipoIzq = tablaVar.getType(operandoIzq)
                    memoriaI = tablaVar.getMemory(operandoIzq)
                    #print(p[1], "es local")
                elif tablaConstantes.verify(operandoIzq): #Ver si es constante
                    tipoIzq = tablaConstantes.getType(operandoIzq)
                    memoriaI = tablaConstantes.getMemory(operandoIzq)
                elif tablaGlobal.verify(operandoIzq): #Ver si es global
                    tipoIzq = tablaGlobal.getType(operandoIzq)
                    memoriaI = tablaGlobal.getMemory(operandoIzq)
                    #print(p[1], "es global")
                else: #es temporal
                    print("Estemporal", operandoIzq)
                    tipoIzq = tipos.pop()
                    if tipoIzq == "int":
                        if temporal_int + espacio_temp_i >= 16000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_int + espacio_temp_i
                    elif tipoIzq == "float":
                        if temporal_float + espacio_temp_f >= 17000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_float + espacio_temp_f
                    elif tipoIzq == "char":
                        if temporal_float + espacio_temp_c >= 18000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_char + espacio_temp_c
                    elif tipoIzq == "bool":
                        if temporal_bool + espacio_temp_b >= 1:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_char + espacio_temp_c

                #Obtener el tipo del operandoDer
                if tablaVar.verify(operandoDer): #Ver si es local
                    tipoDer = tablaVar.getType(operandoDer)
                    memoriaD = tablaVar.getMemory(operandoDer)
                    #print(p[1], "es local")
                elif tablaConstantes.verify(operandoDer): #Ver si es constante
                    tipoDer = tablaConstantes.getType(operandoDer)
                    memoriaD = tablaConstantes.getMemory(operandoDer)
                elif tablaGlobal.verify(operandoDer): #Ver si es global
                    tipoDer = tablaGlobal.getType(operandoDer)
                    memoriaD = tablaGlobal.getMemory(operandoDer)
                    #print(p[1], "es global")
                else: #es temporal
                    print("Estemporal")
                    tipoDer = tipos.pop()
                    if tipoDer == "int":
                        if temporal_int + espacio_temp_i >= 16000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_int + espacio_temp_i
                    elif tipoDer == "float":
                        if temporal_float + espacio_temp_f >= 17000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_float + espacio_temp_f
                    elif tipoDer == "char":
                        if temporal_float + espacio_temp_c >= 18000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_char + espacio_temp_c
                    elif tipoDer == "bool":
                        if temporal_bool + espacio_temp_b >= 1:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_char + espacio_temp_c

                if cubo.get(tipoIzq, tipoDer, operador) == "Error":
                    raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
                else:
                    tipos.append(cubo.get(tipoIzq, tipoDer, operador))
                    tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
                    if tipo_temporal == "int":
                        temporal_int = temporal_int + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_int+espacio_temp_i)))
                        operandos.append(str(temporal_int+espacio_temp_i))
                    elif tipo_temporal == "float":
                        temporal_float = temporal_float + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_float+espacio_temp_f)))
                        operandos.append(str(temporal_float+espacio_temp_f))
                    elif tipo_temporal == "char":
                        temporal_char = temporal_char + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, operandoDer, str(temporal_char+espacio_temp_c)))
                        operandos.append(str(temporal_char+espacio_temp_c))
                    else:
                        temporal_bool = temporal_bool + 1
                        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, str(temporal_bool+espacio_temp_b)))
                        operandos.append(str(temporal_bool+espacio_temp_b))
                    #print("Saliendo de factor", tipos)
                    

def p_guardarConstanteInt(p):
    '''
    guardarConstanteInt : empty
    '''
    #print(p[-1])
    if tablaConstantes.verify(p[-1]):
        pass
    else:
        tablaConstantes.add(p[-1], "int")

def p_guardarConstanteFloat(p):
    '''
    guardarConstanteFloat : empty
    '''
    #print(p[-1])
    if tablaConstantes.verify(p[-1]):
        pass
    else:
        tablaConstantes.add(p[-1], "float")

def p_guardarConstanteChar(p):
    '''
    guardarConstanteChar : empty
    '''
    #print(p[-1])
    if tablaConstantes.verify(p[-1]):
        pass
    else:
        tablaConstantes.add(p[-1], "char")

def p_variable(p):
    '''
    variable : ID 
    | ID BRACEOPEN exp BRACECLOSE 
    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE
    '''
    if len(p) >= 2 and p[1]:
        operandos.append(p[1])

def p_variableAssignment(p):
    '''
    variableAssignment : ID 
    | ID BRACEOPEN exp BRACECLOSE 
    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE
    '''

    if len(p) >= 2 and p[1]:
        declarada = False
        tablaVar = directorioFunciones.get(contexto[-1])
        #print(contexto)
        #variable = operandos.pop()
        if tablaVar.verify(p[1]):
            declarada = True
            #print(p[1], "es local")
        else:
            if tablaGlobal.verify(p[1]):
                declarada = True
               #print(p[1], "es global")
            else:
                print(p[1])
                raise Error("VARIABLE NO DECLARADA")
        
        if declarada:
            operandos.append(p[1])
            if(len(operadores) > 0 and (operadores[len(operadores)-1] == "*" or operadores[len(operadores)-1] == "/")):
                operador = operadores.pop()
                operandoDer = operandos.pop()
                operandoIzq = operandos.pop()
                tablaVar = directorioFunciones.get(contexto[-1])
       
                #Obtener el tipo del operandoIzq
                if tablaVar.verify(operandoIzq): #Ver si es local
                    tipoIzq = tablaVar.getType(operandoIzq)
                    memoriaI = tablaVar.getMemory(operandoIzq)
                    #print(p[1], "es local")
                elif tablaConstantes.verify(operandoIzq): #Ver si es constante
                    tipoIzq = tablaConstantes.getType(operandoIzq)
                    memoriaI = tablaConstantes.getMemory(operandoIzq)
                elif tablaGlobal.verify(operandoIzq): #Ver si es global
                    tipoIzq = tablaGlobal.getType(operandoIzq)
                    memoriaI = tablaGlobal.getMemory(operandoIzq)
                    #print(p[1], "es global")
                else: #es temporal
                    print("Estemporal", operandoIzq)
                    tipoIzq = tipos.pop()
                    if tipoIzq == "int":
                        if temporal_int + espacio_temp_i >= 16000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_int + espacio_temp_i
                    elif tipoIzq == "float":
                        if temporal_float + espacio_temp_f >= 17000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_float + espacio_temp_f
                    elif tipoIzq == "char":
                        if temporal_float + espacio_temp_c >= 18000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_char + espacio_temp_c
                    elif tipoIzq == "bool":
                        if temporal_bool + espacio_temp_b >= 1:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaI = temporal_char + espacio_temp_c

                #Obtener el tipo del operandoDer
                if tablaVar.verify(operandoDer): #Ver si es local
                    tipoDer = tablaVar.getType(operandoDer)
                    memoriaD = tablaVar.getMemory(operandoDer)
                    #print(p[1], "es local")
                elif tablaConstantes.verify(operandoDer): #Ver si es constante
                    tipoDer = tablaConstantes.getType(operandoDer)
                    memoriaD = tablaConstantes.getMemory(operandoDer)
                elif tablaGlobal.verify(operandoDer): #Ver si es global
                    tipoDer = tablaGlobal.getType(operandoDer)
                    memoriaD = tablaGlobal.getMemory(operandoDer)
                    #print(p[1], "es global")
                else: #es temporal
                    print("Estemporal")
                    tipoDer = tipos.pop()
                    if tipoDer == "int":
                        if temporal_int + espacio_temp_i >= 16000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_int + espacio_temp_i
                    elif tipoDer == "float":
                        if temporal_float + espacio_temp_f >= 17000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_float + espacio_temp_f
                    elif tipoDer == "char":
                        if temporal_float + espacio_temp_c >= 18000:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_char + espacio_temp_c
                    elif tipoDer == "bool":
                        if temporal_bool + espacio_temp_b >= 1:
                            raise Error("LIMITE DE ESPACIO DE MEMORIA ALCANZADO")
                        else:
                            memoriaD = temporal_char + espacio_temp_c

                if cubo.get(tipoIzq, tipoDer, operador) == "Error":
                    raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
                else:
                    tipos.append(cubo.get(tipoIzq, tipoDer, operador))
                    tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
                    if tipo_temporal == "int":
                        temporal_int = temporal_int + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_int+espacio_temp_i)))
                        operandos.append(str(temporal_int+espacio_temp_i))
                    elif tipo_temporal == "float":
                        temporal_float = temporal_float + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, str(temporal_float+espacio_temp_f)))
                        operandos.append(str(temporal_float+espacio_temp_f))
                    elif tipo_temporal == "char":
                        temporal_char = temporal_char + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, operandoDer, str(temporal_char+espacio_temp_c)))
                        operandos.append(str(temporal_char+espacio_temp_c))
                    else:
                        temporal_bool = temporal_bool + 1
                        lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, operandoDer, str(temporal_bool+espacio_temp_b)))
                        operandos.append(str(temporal_bool+espacio_temp_b))
                    #print("Saliendo de variableAssignment", tipos)

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

    tipo = tipos.pop()
    if tipo != "bool":
        raise Error("LA EXPRESION NO ES BOOLEANA")
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
    lista_cuadruplos.append(Cuadruplos(operador, "", "", operandoDer))
    #print(operandos)

def p_auxString(p):
    '''
    auxString : CTESTRING
       
    '''
    if(p[1]):
        operandos.append(p[1])
        if tablaConstantes.verify(p[1]):
            pass
        else:
            tablaConstantes.add(p[1], "print")

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
    tablaVar = directorioFunciones.get(contexto[-1])
    if tablaVar.verify(operandoDer) or tablaConstantes.verify(operandoDer):
        memory = tablaVar.getMemory(operandoDer)
    else:
        if tablaGlobal.verify(operandoDer):
            memory = tablaVar.getMemory(operandoDer)
        else:
            print(p[1], "No declarada")
            print(contexto[-1])
            raise Error("VARIABLE NO DECLARADA")

    lista_cuadruplos.append(Cuadruplos(operador, "", "", memory))

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
    tipo = tipos.pop()
    if tipo != "bool":
        raise Error("LA EXPRESION NO ES BOOLEANA")
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
    for_loop : FOR PARENOPEN ID EQUAL exp guardarValorFor TO exp PARENCLOSE body forEnd

    '''
    print(p[:])
    declarada = False
    tablaVar = directorioFunciones.get(contexto[-1])
    #print(contexto)
    #variable = operandos.pop()
    if tablaVar.verify(p[3]) or tablaConstantes.verify(p[3]):
        declarada = True
        #print(p[1], "es local")
    else:
        if tablaGlobal.verify(p[3]):
            declarada = True
            #print(p[1], "es global")
        else:
            print(p[3], "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada:
        operandos.append(p[3])

def p_guardarValorFor(p):
    '''
    guardarValorFor : empty

    '''
    exp = operandos.pop()
    print(operandos)
    print(exp)
   # print(vcontrol)

def p_forEnd(p):
    '''
    forEnd : empty

    '''

def p_return(p):
    '''
    return : RETURN exp SEMICOLON
       
    '''
    print(p[:])
    if directorioFunciones.get(contexto[-1]).type == "void" and contexto[-1] != "main":
        raise Error("LAS FUNCIONES VOID NO DEBEN RETORNAR")
    else:
        valor = operandos.pop()
        lista_cuadruplos.append(Cuadruplos("RET","" , "", valor))

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
        archivo = open('test8.txt','r')
        datos = archivo.read()
        archivo.close()
        if(yacc.parse(datos, tracking=True) == 'COMPILED'):
            maquinaVirtual.start()
            print("\nAPROPIADO: ANALISIS CONCLUIDO SIN ERRORES")
        else:
            print("SE PRODUJO UN ERROR DURANTE EL ANALISIS")
    except EOFError:
        print(EOFError)