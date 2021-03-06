'''
Rodrigo de Jesús Ruíz Kwok A00824488

PLY.py:

En este archivo se lleva acabo el lexer y parser de python que nos genera el código intermedio a procesar
en la máquina virtual.

'''
import sys
import ply.lex as lex
import ply.yacc as yacc
from DirectorioFunciones import DirectorioFunciones
from Cuadruplos import Cuadruplos
from Constantes import Constantes
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
    
#Definicion de lo que es un ID
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserverdWords.get(t.value, 'ID')
    return t

#Definicion de lo que es un CTFLOAT
def t_CTFLOAT(t):
    r'-?\d+?\.\d+'
    t.value = float(t.value)
    return t

#Definicion de lo que es un CTEINT
def t_CTEINT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

#Definicion de lo que es un CTESTRING
def t_CTESTRING(t):
    r'"(.*?)"'
    t.value = str(t.value)
    return t

#Definicion de lo que es un CTECHAR
def t_CTECHAR(t):
    r"'.'"
    t.value = str(t.value)
    return t

#Definicion de lo que es un error y el mensaje que imprime
def t_error(t):
    raise Error("HAY UN ERROR")
    t.lexer.skip(1)

#Se genera el lexer
lexer = lex.lex()

#Inicialización de las pilas 
operadores = []
operandos = []
tipos = []
lista_cuadruplos = [] #Aqui se irán guardando los cuadruplos
saltos = []
operandos_verificar = []

#Instanciación del cubo semantico, constantes y directorio de funciones
cubo = CuboSemantico()
directorioFunciones = DirectorioFunciones()
tablaConstantes = Constantes()

#Definimos que recien se corre el compilador se entra en el contexto global
contexto = ["global"]
directorioFunciones.add("global")
tablaGlobal = directorioFunciones.get("global")
tablaGlobal.setFuncType("np")

#Inicialización de los auxiliares para el manejo de parametros
contador_parametros = 0
contador_parametros_call = 0
tipos_param = []
validar_tipos_param = []

#Inicialización del contador de temporales (se empieza en -1 porque se incrementa antes de cada append a la lista de cuadruplos)
temporal_int = -1
temporal_bool = -1
temporal_float = -1
temporal_char = -1

#Inicialización de las direcciones virtuales de los temporales
espacio_temp_i = 15000
espacio_temp_f = 16000
espacio_temp_c = 17000
espacio_temp_b = 18000

#Inicio del programa
def p_start_program(p):
    '''
    start_program : cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body end
    | cuadruploMain PROGRAM ID SEMICOLON vars main_body end
    | cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body end
    | cuadruploMain PROGRAM ID SEMICOLON main_body end
    '''
    p[0] = "COMPILED"
    '''imprimirFunciones = []
    for index, i in enumerate(directorioFunciones.funciones):
        imprimirFunciones.append(i)
    for index, i in enumerate(imprimirFunciones):
        print("Tabla de ", i)
        print("Tabla de variables: ", directorioFunciones.get(i).variables)
        print("Tabla de memoria: ", directorioFunciones.get(i).memoria)
        print("Tipo: ", directorioFunciones.get(i).type)
        print("DirV: ", directorioFunciones.get(i).dirV)
    print("Tabla de constantes: ", tablaConstantes.constantes)
    print("Memoria constantes: ", tablaConstantes.memoria)'''
    #print(directorioFunciones.get("main").getType("A"))

    #for index, i in enumerate(lista_cuadruplos):
     #   print(str(index+1)+".-", i.get())

#Se genera el primer cuadruplo para posteriormente insertar la dirección de inicio del main
def p_cuadruploMain(p):
    '''
    cuadruploMain : empty
    '''
    #Goto para el main
    lista_cuadruplos.append(Cuadruplos("GOTO","" , "", ""))
    
    #Guardamos el index actual para luego reemplazar el cuadruplo GOTO por uno completo
    saltos.append(len(lista_cuadruplos)-1)

#Se define la estructura a seguir en el main
def p_main_body(p):
    '''
    main_body : MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body 
    '''
#Se indica el incio del Main, indicamos que contexto en el que estamos y creamos el SymbolTable para Main
def p_crearTablaMain(p):
    '''
    crearTablaMain : empty
    '''
    contexto.append("main")
    directorioFunciones.add("main")
    tablaMain = directorioFunciones.get("main")
    tablaMain.setFuncType("void")

#Se guarda la direccion en la que inicia el main
def p_gotoMain(p):
    '''
    gotoMain : empty
    '''
    saltos.append(len(lista_cuadruplos)+1)

    #Cambiar el GOTOF incompleto por el completo
    goto = saltos.pop()
    tablaMain = directorioFunciones.get("main")
    tablaMain.setDirV(goto)

    #Index del GOTOF incompleto
    index = saltos.pop()

    #Cambiar el GOTOF incompleto por el completo
    lista_cuadruplos.pop(index)
    lista_cuadruplos.insert(index, Cuadruplos("GOTO","" , "main", directorioFunciones.get("main").dirV))

#Se indica el fin del main (fin del programa)
def p_end(p):
    '''
    end : empty
    '''
    lista_cuadruplos.append(Cuadruplos("END","" , "", ""))

#Se declaran variables globales
def p_vars(p):
    '''
    vars : VAR varss
    '''

#Declaración de variables globales de distinto tipo
def p_varss(p):
    '''
    varss : type guardarTipo mvar SEMICOLON varss
    | type guardarTipo mvar SEMICOLON
    '''
    tipos.pop()

#Se guarda el tipo de la variable
def p_guardarTipo(p):
    '''
    guardarTipo : empty
    '''
    tipos.append(p[-1])

#Declaración de variables globales del mismo tipo
def p_mvar(p):
    '''
    mvar : ID guardarIDvar COLON mvar
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar
    | ID guardarIDvar
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE 
    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE 
    '''

#Guardar el ID de la variable con su tipo
def p_guardarIDvar(p):
    '''
    guardarIDvar : empty
    '''
    operandos.append(p[-1])
    tipo = tipos[-1]
    tipos.append(tipo)

    #Verificar que la variable no se haya declarado previamente antes de guardarla en la tabla
    variable = operandos.pop()
    if tablaGlobal.verify(variable):
        raise Error("NOMBRES DE VARIABLES REPETIDOS DENTRO DE LA MISMA FUNCION")
    else:
        tablaGlobal.addGlobal(variable, tipos.pop())

#Se pueden definir varias funciones
def p_multiple_funcs(p):
    '''
    multiple_funcs : dec_func 
    | dec_func multiple_funcs
    '''
#Declaración de una función
def p_dec_func(p):
    '''
    dec_func : FUNCTION type ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc
    | FUNCTION VOID ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc
    '''
#Crear la tabla de la funcion
def p_crearSymbolTable(p):
    '''
    crearSymbolTable : empty
    '''
    #Añadir el nombre de la funcion a la pila de contexto
    contexto.append(p[-1])
    
    #Validar si ya se había declarado la función previamente antes de agregarla al directorio
    if directorioFunciones.verify(p[-1]):
        raise Error("NOMBRE DE FUNCION REPETIDO")
    else:
        #Se añade la funcion al directorio con su tipo
        directorioFunciones.add(p[-1])
        tablaVariables = directorioFunciones.get(p[-1])
        tablaVariables.setFuncType(p[-2])

#Se va leyendo parametro por parametro
def p_param(p):
    '''
    param : typeParam ID
    | typeParam ID COLON param
    | empty
    '''
    #print(p[:])
    if len(p) > 2:
        #Se va incrementando el contador de parámetros
        global contador_parametros
        contador_parametros = contador_parametros + 1
        operandos.append(p[2])

        #Validar que el ID del parametro no sea repetido en la tabla de la funcion o sea el nombre de la funcion
        tablaVar = directorioFunciones.get(contexto[-1])
        variable = operandos.pop()
        if tablaVar.verify(variable):
            raise Error("NOMBRES DE VARIABLES REPETIDOS DENTRO DE LA MISMA FUNCION")
        else:
            if directorioFunciones.verify(variable):
                raise Error("NOMBRES DE VARIABLES-FUNCIONES REPETIDOS")
            else:
                #Si no hay error se guarda el parametro en la tabla de la funcion con su tipo
                tablaVar.add(variable, tipos.pop())

#Se van guardando el orden y tipos de parametros
def p_typeParam(p):
    '''
    typeParam : INT
    | FLOAT
    | CHAR
    '''
    if p[1]:
        tipos.append(p[1])
        tipos_param.append(p[1])

#Se define el numero de parametros que espera recibir la funcion
def p_numeroParam(p):
    '''
    numeroParam : empty
    '''
    #Se añaden la cantidad y orden de tipos de los parametros a la tabla de la funcion
    global contador_parametros
    tablaVar = directorioFunciones.get(contexto[-1])
    tablaVar.setNumParam(contador_parametros)
    tablaVar.setTiposParam(tipos_param)

#Se define la direccion en la que inician los cuadruplos de la funcion
def p_startFunc(p):
    '''
    startFunc : empty
    '''
    #Se guarda la direccion en la tabla de la funcion
    tablaVar = directorioFunciones.get(contexto[-1])
    tablaVar.setDirV(len(lista_cuadruplos)+1)

#Se define el fin de la declaración de la función
def p_exitFunc(p):
    '''
    exitFunc : empty
    '''
    #Se agrega el cuadruplo ENDFUNC, se reinician los temporales y se cambia de contexto
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

#Se definen los tipos a usar en el lenguaje
def p_type(p):
    '''
    type : INT
    | FLOAT
    | CHAR
    '''
    p[0] = p[1]

#Estructura del cuerpo
def p_body(p):
    '''
    body : BRACKETOPEN bodyy BRACKETCLOSE
    '''

#El cuerpo puede estar vacío o con uno/varios estatutos
def p_bodyy(p):
    '''
    bodyy : statement 
    | statement bodyy
    | empty
    '''

#Se define lo que puede haber dentro de los estatutos
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
    | max
    | min
    | sum
    | normal
    | uniforme
    | poisson
    | binomial
    '''
#Estatuto para la declaración de variables en contextos locales
def p_dec_variables(p):
    '''
    dec_variables : dec_variabless
    '''
#Se pueden declarar varias variables de diferente tipo separados por ";"
def p_dec_variabless(p):
    '''
    dec_variabless : type guardarTipo dec_mvar SEMICOLON dec_variabless
    | type guardarTipo dec_mvar SEMICOLON
    '''
    tipos.pop()

#Se pueden declarar varias variables del mismo tipo separados por ","
def p_dec_mvar(p):
    '''
    dec_mvar : ID guardarID COLON dec_mvar
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar
    | ID guardarID
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE 
    | ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE 
    '''
#Se va guardando el ID de cada variable
def p_guardarID(p):
    '''
    guardarID : empty
    '''
    operandos.append(p[-1])
    tipo = tipos[-1]
    tipos.append(tipo)
    tablaVar = directorioFunciones.get(contexto[-1])

    #Verificar que no se haya declarado previamente la variable o que sea el nombre de alguna funcion
    variable = operandos.pop()
    if tablaVar.verify(variable):
        raise Error("NOMBRES DE VARIABLES REPETIDOS DENTRO DE LA MISMA FUNCION")
    else:
        if directorioFunciones.verify(variable):
            raise Error("NOMBRES DE VARIABLES-FUNCIONES REPETIDOS")
        else:
            #Si no hay error se guarda la variable y su tipo en la tabla
            tablaVar.add(variable, tipos.pop())

#Estatuto de asignación
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
        else: #es temporal
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
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
        else: #es temporal
            tipoDer = tipos.pop()
            
            #Dependiendo de su tipo asignarle una dirección de memoria
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
        
        #Validar con el cubo que los tipos permitan hacer la operación
        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            #Generar cuadruplos con los nombres
            #lista_cuadruplos.append(Cuadruplos(operador, operandoIzq, "", operandoDer))
            
            #Generar cuadruplo con las direcciones
            lista_cuadruplos.append(Cuadruplos(operador, memoriaI, "", memoriaD))
            tipos.pop()

#Estatuto de llamada a una función
def p_call_func(p):
    '''
    call_func : ID generarERA PARENOPEN call_funcc PARENCLOSE
    '''
    global contador_parametros_call
    global validar_tipos_param
    
    #Si el numero de parametros que se mandan no es el mismo al que la función requiere marcar error
    if contador_parametros_call != directorioFunciones.get(p[1]).numParam:
        raise Error("ERROR CON EL NUMERO DE PARAMETROS")
    #Si los tipos de los parametros no coinciden con el orden o tipo al de los que la función requiere marcar error
    elif directorioFunciones.get(p[1]).tipos_Param != validar_tipos_param:
        raise Error("ERROR EN LOS TIPOS DE LOS ARGUMENTOS")
    else:
        lista_cuadruplos.append(Cuadruplos("GOSUB", "", "", directorioFunciones.get(p[1]).dirV))
        contador_parametros_call = 0
        validar_tipos_param = []

#Generación de ERA
def p_generarERA(p):
    '''
    generarERA : empty
    '''
    #Validar que la funcion a la que se quiere acceder exista
    if directorioFunciones.verify(p[-1]):
        pass
    else:
        raise Error("NO EXISTE FUNCION CON ESE NOMBRE")
    #Generar ERA hacia la dirección donde empieza la funcion
    lista_cuadruplos.append(Cuadruplos("ERA", "", "", p[-1]))

#Se pueden mandar a llamar varios parámetros
def p_call_funcc(p):
    '''
    call_funcc : exp mandarParam
    | exp mandarParam COLON call_funcc
    | empty
    '''
#Generación de parámetros
def p_mandarParam(p):
    '''
    mandarParam : empty
    '''
    param = operandos.pop()
    
    #Obtener el tipo del parametro
    tablaVar = directorioFunciones.get(contexto[-1])
    if tablaVar.verify(param): #Ver si es local
        tipo_Validar = tablaVar.getType(param)
        memoria = tablaVar.getMemory(param)
    elif tablaConstantes.verify(param): #Ver si es constante
        tipo_Validar = tablaConstantes.getType(param)
        memoria = tablaConstantes.getMemory(param)
    elif tablaGlobal.verify(param): #Ver si es global
        tipo_Validar = tablaGlobal.getType(param)
        memoria = tablaGlobal.getMemory(param)
    else: #es temporal
        tipo_Validar = tipos.pop()

        #Dependiendo de su tipo asignarle una dirección de memoria
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
    
    #Ir guardando el orden de los tipos de los parametros
    global validar_tipos_param
    validar_tipos_param.append(tipo_Validar)
    
    #Ir incrementando el contador de parámetros
    global contador_parametros_call
    contador_parametros_call = contador_parametros_call + 1

    #Generar cuadruplo
    lista_cuadruplos.append(Cuadruplos("PARAM", memoria, "", "PARAM"+str(contador_parametros_call)))

#Estatuto para el trabajo con expresiones && || (más baja prioridad)
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
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
        else: #es temporal
            tipoIzq = tipos.pop()

            #Dependiendo de su tipo asignarle una dirección de memoria
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
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
        else: #es temporal
            tipoDer = tipos.pop()

            #Dependiendo de su tipo asignarle una dirección de memoria
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

        #Validar con el cubo que se pueda hacer la operación
        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            #Incrementar temporal dependiendo el tipo y generar cuadruplos
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_int+espacio_temp_i)))
                operandos.append((temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_float+espacio_temp_f)))
                operandos.append((temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_char+espacio_temp_c)))
                operandos.append((temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_bool+espacio_temp_b)))
                operandos.append((temporal_bool+espacio_temp_b))

#Trabajo de expresiones > < >= <= != ==
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
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
        else: #es temporal
            tipoIzq = tipos.pop()

            #Dependiendo de su tipo asignarle una dirección de memoria
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
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
        else: #es temporal
            tipoDer = tipos.pop()

            #Dependiendo de su tipo asignarle una dirección de memoria
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
        
        #Verificar con el cubo que si se pueda hacer la operación
        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)

            #Dependiendo del tipo se incrementa el contador y se genera el cuadruplo
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_int+espacio_temp_i)))
                operandos.append((temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_float+espacio_temp_f)))
                operandos.append((temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_char+espacio_temp_c)))
                operandos.append((temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_bool+espacio_temp_b)))
                operandos.append((temporal_bool+espacio_temp_b))

#Manejo de sumas y restas
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
        elif tablaConstantes.verify(operandoIzq): #Ver si es constante
            tipoIzq = tablaConstantes.getType(operandoIzq)
            memoriaI = tablaConstantes.getMemory(operandoIzq)
        elif tablaGlobal.verify(operandoIzq): #Ver si es global
            tipoIzq = tablaGlobal.getType(operandoIzq)
            memoriaI = tablaGlobal.getMemory(operandoIzq)
        else: #es temporal
            tipoIzq = tipos.pop()

            #Dependiendo de su tipo asignarle una dirección de memoria
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
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
        else: #es temporal
            tipoDer = tipos.pop()

            #Dependiendo de su tipo asignarle una dirección de memoria
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

        #Verificar con el cubo si se puede hacer la operacion
        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
            #Dependiendo del tipo incremental el temporal y generar cuadruplo
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_int+espacio_temp_i)))
                operandos.append((temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_float+espacio_temp_f)))
                operandos.append((temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_char+espacio_temp_c)))
                operandos.append((temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_bool+espacio_temp_b)))
                operandos.append((temporal_bool+espacio_temp_b))

#Manejo de multiplicaciones y divisiones          
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
        else: #es temporal
            tipoIzq = tipos.pop()
            #Dependiendo de su tipo asignarle una dirección de memoria
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
        elif tablaConstantes.verify(operandoDer): #Ver si es constante
            tipoDer = tablaConstantes.getType(operandoDer)
            memoriaD = tablaConstantes.getMemory(operandoDer)
        elif tablaGlobal.verify(operandoDer): #Ver si es global
            tipoDer = tablaGlobal.getType(operandoDer)
            memoriaD = tablaGlobal.getMemory(operandoDer)
        else: #es temporal
            tipoDer = tipos.pop()
            #Dependiendo de su tipo asignarle una dirección de memoria
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
        #Verificar con el cubo si se puede hacer la operacion
        if cubo.get(tipoIzq, tipoDer, operador) == "Error":
            raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
        else:
            tipos.append(cubo.get(tipoIzq, tipoDer, operador))
            tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
            #Dependiendo del tipo incremental el temporal y generar cuadruplo
            if tipo_temporal == "int":
                temporal_int = temporal_int + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_int+espacio_temp_i)))
                operandos.append((temporal_int+espacio_temp_i))
            elif tipo_temporal == "float":
                temporal_float = temporal_float + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_float+espacio_temp_f)))
                operandos.append((temporal_float+espacio_temp_f))
            elif tipo_temporal == "char":
                temporal_char = temporal_char + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_char+espacio_temp_c)))
                operandos.append((temporal_char+espacio_temp_c))
            else:
                temporal_bool = temporal_bool + 1
                lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_bool+espacio_temp_b)))
                operandos.append((temporal_bool+espacio_temp_b))

#Manejo de factores
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
        
        #Verificar si la variable ya ha sido declarada previamente
        if tablaVar.verify(p[1]) or tablaConstantes.verify(p[1]):
            declarada = True
        else:
            if tablaGlobal.verify(p[1]):
                declarada = True
            else:
                raise Error("VARIABLE NO DECLARADA")
        
        #Si ya fue declarada verificar la prioridad de operaciones
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
                elif tablaConstantes.verify(operandoIzq): #Ver si es constante
                    tipoIzq = tablaConstantes.getType(operandoIzq)
                    memoriaI = tablaConstantes.getMemory(operandoIzq)
                elif tablaGlobal.verify(operandoIzq): #Ver si es global
                    tipoIzq = tablaGlobal.getType(operandoIzq)
                    memoriaI = tablaGlobal.getMemory(operandoIzq)
                else: #es temporal
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
                    tipoDer = tipos.pop()

                    #Dependiendo de su tipo asignarle una dirección de memoria
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
                #Verificar con el cubo si se puede hacer la operacion
                if cubo.get(tipoIzq, tipoDer, operador) == "Error":
                    raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
                else:
                    tipos.append(cubo.get(tipoIzq, tipoDer, operador))
                    #Dependiendo del tipo incremental el temporal y generar cuadruplo
                    tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
                    if tipo_temporal == "int":
                        temporal_int = temporal_int + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_int+espacio_temp_i)))
                        operandos.append((temporal_int+espacio_temp_i))
                    elif tipo_temporal == "float":
                        temporal_float = temporal_float + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_float+espacio_temp_f)))
                        operandos.append((temporal_float+espacio_temp_f))
                    elif tipo_temporal == "char":
                        temporal_char = temporal_char + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_char+espacio_temp_c)))
                        operandos.append((temporal_char+espacio_temp_c))
                    else:
                        temporal_bool = temporal_bool + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_bool+espacio_temp_b)))
                        operandos.append((temporal_bool+espacio_temp_b))
                    
#Guardar la constante entera en la tabla de constantes (si no ha sido guardada antes)
def p_guardarConstanteInt(p):
    '''
    guardarConstanteInt : empty
    '''
    if tablaConstantes.verify(p[-1]):
        pass
    else:
        tablaConstantes.add(p[-1], "int")

#Guardar la constante flotante en la tabla de constantes (si no ha sido guardada antes)
def p_guardarConstanteFloat(p):
    '''
    guardarConstanteFloat : empty
    '''
    if tablaConstantes.verify(p[-1]):
        pass
    else:
        tablaConstantes.add(p[-1], "float")

#Guardar la constante char en la tabla de constantes (si no ha sido guardada antes)
def p_guardarConstanteChar(p):
    '''
    guardarConstanteChar : empty
    '''
    if tablaConstantes.verify(p[-1]):
        pass
    else:
        tablaConstantes.add(p[-1], "char")

#Guardar el ID de la variable en la pila de operandos
def p_variable(p):
    '''
    variable : ID 
    | ID BRACEOPEN exp BRACECLOSE 
    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE
    '''
    if len(p) >= 2 and p[1]:
        operandos.append(p[1])

#Estatuto para las variables que se les asignará un valor
def p_variableAssignment(p):
    '''
    variableAssignment : ID 
    | ID BRACEOPEN exp BRACECLOSE 
    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE
    '''

    if len(p) >= 2 and p[1]:
        declarada = False
        tablaVar = directorioFunciones.get(contexto[-1])

        #Verificar si ya fue declarada
        if tablaVar.verify(p[1]):
            declarada = True
        else:
            if tablaGlobal.verify(p[1]):
                declarada = True
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
                elif tablaConstantes.verify(operandoIzq): #Ver si es constante
                    tipoIzq = tablaConstantes.getType(operandoIzq)
                    memoriaI = tablaConstantes.getMemory(operandoIzq)
                elif tablaGlobal.verify(operandoIzq): #Ver si es global
                    tipoIzq = tablaGlobal.getType(operandoIzq)
                    memoriaI = tablaGlobal.getMemory(operandoIzq)
                else: #es temporal
                    tipoIzq = tipos.pop()

                    #Dependiendo de su tipo asignarle una dirección de memoria
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
                elif tablaConstantes.verify(operandoDer): #Ver si es constante
                    tipoDer = tablaConstantes.getType(operandoDer)
                    memoriaD = tablaConstantes.getMemory(operandoDer)
                elif tablaGlobal.verify(operandoDer): #Ver si es global
                    tipoDer = tablaGlobal.getType(operandoDer)
                    memoriaD = tablaGlobal.getMemory(operandoDer)
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
                #Verificar con el cubo si
                if cubo.get(tipoIzq, tipoDer, operador) == "Error":
                    raise Error("LOS TIPOS DE LAS VARIABLES NO SON COMPATIBLES")
                else:
                    tipos.append(cubo.get(tipoIzq, tipoDer, operador))
                    tipo_temporal = cubo.get(tipoIzq, tipoDer, operador)
                    if tipo_temporal == "int":
                        temporal_int = temporal_int + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_int+espacio_temp_i)))
                        operandos.append((temporal_int+espacio_temp_i))
                    elif tipo_temporal == "float":
                        temporal_float = temporal_float + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_float+espacio_temp_f)))
                        operandos.append((temporal_float+espacio_temp_f))
                    elif tipo_temporal == "char":
                        temporal_char = temporal_char + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_char+espacio_temp_c)))
                        operandos.append((temporal_char+espacio_temp_c))
                    else:
                        temporal_bool = temporal_bool + 1
                        lista_cuadruplos.append(Cuadruplos(operador, memoriaI, memoriaD, (temporal_bool+espacio_temp_b)))
                        operandos.append((temporal_bool+espacio_temp_b))

#Estatuto condicional
def p_condition(p):
    '''
    condition : IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd
        | IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse
    '''
#Validacion y generación del GOTOF
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

#Señalar el final del if
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

#Señalar el GOTO en else
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

#Señalar el final del IFELSE
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

#Estatuto para imprimir valores
def p_writing(p):
    '''
    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON
    '''

#Imprimir múltiples valores
def p_writingg(p):
    '''
    writingg : exp
    | exp COLON writingg
    | auxString
    | auxString COLON writingg
    '''
    operadores.append("print")
    operador = operadores.pop()
    operandoDer = operandos.pop(0)
    lista_cuadruplos.append(Cuadruplos(operador, "", "", operandoDer))

#Manejo de strings
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

#Leer variable 
def p_reading(p):
    '''
    reading : READ multivariables SEMICOLON
       
    '''
#Leer varias variables
def p_multivariables(p):
    '''
    multivariables : variable
    | variable COLON multivariables
       
    '''
    operadores.append("read")
    operador = operadores.pop()
    operandoDer = operandos.pop()

    #Verificar que ya se haya declarado la variables para guardarla
    tablaVar = directorioFunciones.get(contexto[-1])
    if tablaVar.verify(operandoDer) or tablaConstantes.verify(operandoDer):
        memory = tablaVar.getMemory(operandoDer)
    else:
        if tablaGlobal.verify(operandoDer):
            memory = tablaVar.getMemory(operandoDer)
        else:
            raise Error("VARIABLE NO DECLARADA")

    lista_cuadruplos.append(Cuadruplos(operador, "", "", memory))

#Estatuto ciclico
def p_while_loop(p):
    '''
    while_loop : WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd
       
    '''
#Saber a donde regresar a evaluar la expresion
def p_whileMigaja(p):
    '''
    whileMigaja : empty
       
    '''
    #Se suma 1 porque las listas inician en 0
    saltos.append(len(lista_cuadruplos) + 1)

#Evaluar la expresion del while
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

#Marcar el final del While
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

#Regresar una expresion
def p_return(p):
    '''
    return : RETURN exp SEMICOLON
       
    '''
    #Si no estamos en un void aceptar el return
    if directorioFunciones.get(contexto[-1]).type == "void" and contexto[-1] != "main":
        raise Error("LAS FUNCIONES VOID NO DEBEN RETORNAR")
    else:
        valor = operandos.pop()
        lista_cuadruplos.append(Cuadruplos("RET","" , "", valor))

#Funcion que grafica una expresion
def p_graph(p):
    '''
    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON
    
    '''
    if p[1]:
        valor = operandos.pop()
        lista_cuadruplos.append(Cuadruplos("PLOT","" , "", valor))

#Funcion que regresa el maximo de un arreglo
def p_max(p):
    '''
    max : MAX PARENOPEN ID PARENCLOSE SEMICOLON
       
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    if tablaVar.verify(p[3]) or tablaConstantes.verify(p[3]):
        declarada = True
    else:
        if tablaGlobal.verify(p[3]):
            declarada = True
        else:
            print(p[3], "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada:
        lista_cuadruplos.append(Cuadruplos("MAX","" , "", p[3]))

#Funcion que regresa el minimo de un arreglo
def p_min(p):
    '''
    min : MIN PARENOPEN ID PARENCLOSE SEMICOLON
       
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    if tablaVar.verify(p[3]) or tablaConstantes.verify(p[3]):
        declarada = True
    else:
        if tablaGlobal.verify(p[3]):
            declarada = True
        else:
            print(p[3], "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada:
        lista_cuadruplos.append(Cuadruplos("MIN","" , "", p[3]))

#Funcion que regresa la suma de un arreglo
def p_sum(p):
    '''
    sum : SUM PARENOPEN ID PARENCLOSE SEMICOLON
       
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    if tablaVar.verify(p[3]) or tablaConstantes.verify(p[3]):
        declarada = True
    else:
        if tablaGlobal.verify(p[3]):
            declarada = True
        else:
            print(p[3], "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada:
        lista_cuadruplos.append(Cuadruplos("SUM","" , "", p[3]))

def p_binomial(p):
    '''
    binomial : BINOMIAL PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON
       
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    operando3 = operandos.pop()
    operando2 = operandos.pop()
    operando1 = operandos.pop()

    if tablaVar.verify(operando1) or tablaConstantes.verify(operando1):
        declarada1 = True
    else:
        if tablaGlobal.verify(operando1):
            declarada1 = True
        else:
            print(operando1, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if tablaVar.verify(operando2) or tablaConstantes.verify(operando2):
        declarada2 = True
    else:
        if tablaGlobal.verify(operando2):
            declarada2 = True
        else:
            print(operando2, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if tablaVar.verify(operando3) or tablaConstantes.verify(operando3):
        declarada3 = True
    else:
        if tablaGlobal.verify(operando1):
            declarada3 = True
        else:
            print(operando1, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada1 and declarada2 and declarada3:
        lista_cuadruplos.append(Cuadruplos("BINOMIAL",operando1, operando2, operando3))

def p_poisson(p):
    '''
    poisson : POISSON PARENOPEN exp COLON exp PARENCLOSE SEMICOLON
       
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    operando2 = operandos.pop()
    operando1 = operandos.pop()

    if tablaVar.verify(operando1) or tablaConstantes.verify(operando1):
        declarada1 = True
    else:
        if tablaGlobal.verify(operando1):
            declarada1 = True
        else:
            print(operando1, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if tablaVar.verify(operando2) or tablaConstantes.verify(operando2):
        declarada2 = True
    else:
        if tablaGlobal.verify(operando2):
            declarada2 = True
        else:
            print(operando2, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada1 and declarada2:
        lista_cuadruplos.append(Cuadruplos("POISSON",operando1, operando2, ""))

def p_uniforme(p):
    '''
    uniforme : UNIFORME PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON
       
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    operando3 = operandos.pop()
    operando2 = operandos.pop()
    operando1 = operandos.pop()

    if tablaVar.verify(operando1) or tablaConstantes.verify(operando1):
        declarada1 = True
    else:
        if tablaGlobal.verify(operando1):
            declarada1 = True
        else:
            print(operando1, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if tablaVar.verify(operando2) or tablaConstantes.verify(operando2):
        declarada2 = True
    else:
        if tablaGlobal.verify(operando2):
            declarada2 = True
        else:
            print(operando2, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if tablaVar.verify(operando3) or tablaConstantes.verify(operando3):
        declarada3 = True
    else:
        if tablaGlobal.verify(operando1):
            declarada3 = True
        else:
            print(operando1, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada1 and declarada2 and declarada3:
        lista_cuadruplos.append(Cuadruplos("UNIFORME",operando1, operando2, operando3))

def p_normal(p):
    '''
    normal : NORMAL PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON
       
    '''
    tablaVar = directorioFunciones.get(contexto[-1])
    operando3 = operandos.pop()
    operando2 = operandos.pop()
    operando1 = operandos.pop()

    if tablaVar.verify(operando1) or tablaConstantes.verify(operando1):
        declarada1 = True
    else:
        if tablaGlobal.verify(operando1):
            declarada1 = True
        else:
            print(operando1, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if tablaVar.verify(operando2) or tablaConstantes.verify(operando2):
        declarada2 = True
    else:
        if tablaGlobal.verify(operando2):
            declarada2 = True
        else:
            print(operando2, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if tablaVar.verify(operando3) or tablaConstantes.verify(operando3):
        declarada3 = True
    else:
        if tablaGlobal.verify(operando1):
            declarada3 = True
        else:
            print(operando1, "No declarada")
            raise Error("VARIABLE NO DECLARADA")
    
    if declarada1 and declarada2 and declarada3:
        lista_cuadruplos.append(Cuadruplos("NORMAL",operando1, operando2, operando3))

#Estatuto vacío
def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

#Marcar Error
def p_error(p):
   raise Error("HAY UN ERROR")

#Creación de la instancia de la maquina virtual
maquinaVirtual = MaquinaVirtual(lista_cuadruplos, directorioFunciones, tablaConstantes)

#Creación del parser yacc
parser = yacc.yacc()

if __name__ == '__main__':
    try:
        archivo = open('main.kwok','r')
        datos = archivo.read()
        archivo.close()
        if(yacc.parse(datos, tracking=True) == 'COMPILED'):
            
            #Iniciar la máquina
            maquinaVirtual.start()
        else:
            print("SE PRODUJO UN ERROR DURANTE EL ANALISIS")
    except EOFError:
        print(EOFError)