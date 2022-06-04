
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BINOMIAL BRACECLOSE BRACEOPEN BRACKETCLOSE BRACKETOPEN CHAR COLON CTEINT CTESTRING CTFLOAT DIFFERENT DIVIDE ELSE EQUAL FLOAT FOR FUNCTION GREATHEREQUAL GREATHERTHAN ID IF INT LESSEQUAL LESSTHAN MAIN MAX MIN MINUS MULTIPLY NORMAL OR PARENCLOSE PARENOPEN PLOT PLUS POISSON PRINT PROGRAM READ RETURN SAME SEMICOLON SUM TO UNIFORME VAR VOID WHILE\n    start_program : cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body\n    | cuadruploMain PROGRAM ID SEMICOLON vars main_body\n    | cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body\n    | cuadruploMain PROGRAM ID SEMICOLON main_body\n    \n    cuadruploMain : empty\n    \n    multiple_funcs : dec_func \n    | dec_func multiple_funcs\n    \n    main_body : MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body \n    \n    crearTablaMain : empty\n    \n    gotoMain : empty\n    \n    vars : VAR varss\n    \n    varss : type guardarTipo mvar SEMICOLON varss\n    | type guardarTipo mvar SEMICOLON\n    \n    guardarTipo : empty\n    \n    mvar : ID COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    dec_func : FUNCTION type ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc\n    | FUNCTION VOID ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc\n    \n    crearSymbolTable : empty\n    \n    exitFunc : empty\n    \n    param : typeParam ID\n    | typeParam ID COLON param\n    | empty\n    \n    typeParam : INT\n    | FLOAT\n    | CHAR\n    \n    type : INT\n    | FLOAT\n    | CHAR\n    \n    body : BRACKETOPEN bodyy BRACKETCLOSE\n    \n    bodyy : statement \n    | statement bodyy\n    | empty\n    \n    statement : dec_variables \n    | assignment\n    | condition\n    | writing\n    | reading\n    | call_func\n    | graph\n    | return\n    | while_loop\n    | for_loop\n    | max\n    | min\n    | sum\n    | normal\n    | uniforme\n    | poisson\n    | binomial\n    \n    dec_variables : dec_variabless\n    \n    dec_variabless : type guardarTipo dec_mvar SEMICOLON dec_variabless\n    | type guardarTipo dec_mvar SEMICOLON\n    \n    dec_mvar : ID COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    assignment : variableAssignment EQUAL exp SEMICOLON\n    \n    call_func : ID PARENOPEN call_funcc PARENCLOSE\n    \n    call_funcc : exp \n    | exp COLON call_funcc\n    | empty\n    \n    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON\n    \n    \n    exp : exp GREATHERTHAN exp \n    | exp LESSTHAN exp \n    | exp GREATHEREQUAL exp \n    | exp LESSEQUAL exp \n    | exp DIFFERENT exp \n    | exp SAME exp\n    | exp AND exp\n    | exp OR exp\n    | m_exp\n    \n    m_exp : t m_expp \n    \n    m_expp : PLUS appendPLUS m_exp\n        | MINUS appendMINUS m_exp\n        | empty\n    \n    appendPLUS : empty\n    \n    appendMINUS : empty\n    \n    appendMULTIPLY : empty\n    \n    appendDIVIDE : empty\n    \n    t : f termino\n    \n    termino : MULTIPLY appendMULTIPLY t \n        | DIVIDE appendDIVIDE t \n        | empty\n    \n    f : PARENOPEN exp PARENCLOSE \n    | ID\n    | CTEINT guardarConstante\n    | CTFLOAT guardarConstante\n    | variable\n    | call_func\n    \n    guardarConstante : empty\n    \n    variable : ID \n    | ID BRACEOPEN exp BRACECLOSE \n    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE\n    \n    variableAssignment : ID \n    | ID BRACEOPEN exp BRACECLOSE \n    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE\n    \n    condition : IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd\n        | IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse\n    \n    cuadruploIF : empty \n    \n    ifEnd : empty \n    \n    cuadruploElse : empty \n    \n    ifEndElse : empty \n    \n    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON\n    \n    writingg : exp\n    | exp COLON writingg\n    | auxString\n    | auxString COLON writingg\n    \n    auxString : CTESTRING\n       \n    \n    reading : READ multivariables SEMICOLON\n       \n    \n    multivariables : variable\n    | variable COLON multivariables\n       \n    \n    while_loop : WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd\n       \n    \n    whileMigaja : empty\n       \n    \n    whileEval : empty\n       \n    \n    whileEnd : empty\n       \n    \n    for_loop : FOR PARENOPEN variable EQUAL exp guardarValorFor TO exp PARENCLOSE body forEnd\n\n    \n    guardarValorFor : empty\n\n    \n    forEnd : empty\n\n    \n    return : RETURN exp SEMICOLON\n       \n    \n    max : MAX PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    min : MIN PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    sum : SUM PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    param_dist : variable\n    | variable COLON param_dist\n       \n    \n    binomial : BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    poisson : POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    uniforme : UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    normal : NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,2,3,],[-136,4,-5,]),'$end':([1,9,15,16,27,49,102,],[0,-4,-2,-3,-1,-8,-34,]),'ID':([4,18,19,20,21,25,26,28,29,40,50,52,54,55,56,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,86,96,101,102,104,105,106,110,111,112,117,125,126,127,128,129,130,131,132,133,145,146,147,153,154,155,156,157,158,159,160,161,163,164,167,168,174,191,194,195,198,199,210,211,212,213,214,215,216,217,220,225,229,230,232,235,240,241,248,249,250,251,253,254,255,256,260,261,268,270,273,274,276,279,280,284,287,288,289,290,291,292,],[5,-136,-31,-32,-33,31,32,34,-14,34,84,98,-28,-29,-30,84,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,109,118,-136,34,-34,118,118,118,118,118,118,118,109,118,118,118,109,109,109,109,185,-116,109,118,-126,118,118,118,118,118,118,118,118,-136,-136,-136,-136,118,-64,118,118,-65,118,118,-83,118,-84,118,-85,118,-86,118,109,-57,185,34,-110,118,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,118,-104,-107,-136,118,185,-119,-122,-136,-105,-109,-136,185,-123,-125,]),'SEMICOLON':([5,33,34,47,58,107,108,109,113,114,115,116,118,119,120,121,122,138,139,162,165,166,169,171,172,173,184,185,190,193,196,198,201,202,203,204,205,206,207,208,209,218,221,222,223,224,226,227,228,238,242,243,244,245,257,259,267,278,283,286,293,],[6,39,-18,-15,-19,145,-117,-98,153,-78,-136,-136,-92,-136,-136,-95,-96,-16,191,-79,-82,-87,-90,-93,-97,-94,229,-61,-20,235,-118,-65,241,-70,-71,-72,-73,-74,-75,-76,-77,-91,248,249,250,251,253,254,255,-99,-80,-81,-88,-89,-58,-17,-62,-100,-59,-63,-60,]),'VAR':([6,],[10,]),'MAIN':([6,7,8,11,14,17,22,39,46,102,134,136,186,187,189,],[12,12,12,-6,12,-11,-7,-13,-12,-34,-136,-136,-21,-24,-22,]),'FUNCTION':([6,7,11,17,39,46,102,134,136,186,187,189,],[13,13,13,-11,-13,-12,-34,-136,-136,-21,-24,-22,]),'INT':([10,13,39,44,45,50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,135,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[19,19,19,54,54,19,19,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,54,-116,-126,-64,-65,19,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'FLOAT':([10,13,39,44,45,50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,135,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[20,20,20,55,55,20,20,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,55,-116,-126,-64,-65,20,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'CHAR':([10,13,39,44,45,50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,135,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[21,21,21,56,56,21,21,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,56,-116,-126,-64,-65,21,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'PARENOPEN':([12,23,24,31,32,36,37,38,81,82,84,85,86,87,88,89,90,91,92,93,94,95,104,105,106,110,111,112,117,118,123,124,126,127,128,147,154,155,156,157,158,159,160,161,163,164,167,168,174,194,195,199,210,211,212,213,214,215,216,217,220,240,261,274,],[-136,30,-9,-136,-136,44,-23,45,105,106,110,112,117,-136,125,126,127,128,129,130,131,132,117,117,117,117,117,117,117,110,174,-120,117,117,117,117,117,117,117,117,117,117,117,117,-136,-136,-136,-136,117,117,117,117,117,-83,117,-84,117,-85,117,-86,117,117,117,117,]),'VOID':([13,],[26,]),'PARENCLOSE':([30,44,45,51,53,57,98,109,110,114,115,116,118,119,120,121,122,135,140,141,142,143,144,148,149,150,152,162,165,166,169,170,171,172,173,176,177,178,179,180,181,182,183,188,198,199,202,203,204,205,206,207,208,209,218,219,236,237,238,239,242,243,244,245,252,278,281,],[35,-136,-136,97,-27,99,-25,-98,-136,-78,-136,-136,-92,-136,-136,-95,-96,-136,192,193,-111,-113,-115,198,-66,-68,201,-79,-82,-87,-90,218,-93,-97,-94,221,222,223,224,-130,226,227,228,-26,-65,-136,-70,-71,-72,-73,-74,-75,-76,-77,-91,246,-112,-114,-99,-67,-80,-81,-88,-89,-131,-100,285,]),'COLON':([34,58,98,108,109,114,115,116,118,119,120,121,122,142,143,144,149,162,165,166,169,171,172,173,180,185,190,198,202,203,204,205,206,207,208,209,218,238,242,243,244,245,267,278,286,],[40,101,135,146,-98,-78,-136,-136,-92,-136,-136,-95,-96,194,195,-115,199,-79,-82,-87,-90,-93,-97,-94,225,230,232,-65,-70,-71,-72,-73,-74,-75,-76,-77,-91,-99,-80,-81,-88,-89,276,-100,290,]),'BRACEOPEN':([34,58,84,109,118,185,200,238,267,],[41,100,111,147,147,231,240,261,275,]),'BRACKETOPEN':([35,42,43,97,99,192,233,234,246,263,264,277,285,],[-136,50,-10,50,50,-136,50,-106,-136,50,-121,50,50,]),'CTEINT':([41,86,100,104,105,106,110,111,112,117,126,127,128,147,154,155,156,157,158,159,160,161,163,164,167,168,174,194,195,199,210,211,212,213,214,215,216,217,220,231,240,261,274,275,],[48,119,137,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,-136,-136,-136,-136,119,119,119,119,119,-83,119,-84,119,-85,119,-86,119,258,119,119,119,282,]),'BRACECLOSE':([48,114,115,116,118,119,120,121,122,137,151,162,165,166,169,171,172,173,197,198,202,203,204,205,206,207,208,209,218,238,242,243,244,245,258,262,271,278,282,],[58,-78,-136,-136,-92,-136,-136,-95,-96,190,200,-79,-82,-87,-90,-93,-97,-94,238,-65,-70,-71,-72,-73,-74,-75,-76,-77,-91,-99,-80,-81,-88,-89,267,272,278,-100,286,]),'BRACKETCLOSE':([50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,103,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[-136,102,-35,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-36,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'IF':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[81,81,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'PRINT':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[82,82,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'READ':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[83,83,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'PLOT':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[85,85,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'RETURN':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[86,86,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'WHILE':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[87,87,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'FOR':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[88,88,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'MAX':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[89,89,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'MIN':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[90,90,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'SUM':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[91,91,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'NORMAL':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[92,92,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'UNIFORME':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[93,93,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'POISSON':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[94,94,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'BINOMIAL':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,153,191,198,229,235,241,248,249,250,251,253,254,255,256,260,268,270,273,279,280,284,287,288,289,291,292,],[95,95,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-116,-126,-64,-65,-57,-110,-69,-127,-128,-129,-135,-134,-133,-132,-56,-136,-104,-107,-136,-119,-122,-136,-105,-109,-136,-123,-125,]),'EQUAL':([80,84,109,175,200,238,272,278,],[104,-101,-98,220,-102,-99,-103,-100,]),'CTFLOAT':([86,104,105,106,110,111,112,117,126,127,128,147,154,155,156,157,158,159,160,161,163,164,167,168,174,194,195,199,210,211,212,213,214,215,216,217,220,240,261,274,],[120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,-136,-136,-136,-136,120,120,120,120,120,-83,120,-84,120,-85,120,-86,120,120,120,120,]),'ELSE':([102,260,269,270,],[-34,-136,277,-108,]),'CTESTRING':([106,194,195,],[144,144,144,]),'GREATHERTHAN':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[154,-78,-136,-136,-92,-136,-136,-95,-96,154,154,154,154,154,154,-79,-82,-87,-90,154,-93,-97,-94,154,154,154,154,-65,154,154,154,154,154,154,154,154,-91,154,-99,-80,-81,-88,-89,154,154,154,-100,154,]),'LESSTHAN':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[155,-78,-136,-136,-92,-136,-136,-95,-96,155,155,155,155,155,155,-79,-82,-87,-90,155,-93,-97,-94,155,155,155,155,-65,155,155,155,155,155,155,155,155,-91,155,-99,-80,-81,-88,-89,155,155,155,-100,155,]),'GREATHEREQUAL':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[156,-78,-136,-136,-92,-136,-136,-95,-96,156,156,156,156,156,156,-79,-82,-87,-90,156,-93,-97,-94,156,156,156,156,-65,156,156,156,156,156,156,156,156,-91,156,-99,-80,-81,-88,-89,156,156,156,-100,156,]),'LESSEQUAL':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[157,-78,-136,-136,-92,-136,-136,-95,-96,157,157,157,157,157,157,-79,-82,-87,-90,157,-93,-97,-94,157,157,157,157,-65,157,157,157,157,157,157,157,157,-91,157,-99,-80,-81,-88,-89,157,157,157,-100,157,]),'DIFFERENT':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[158,-78,-136,-136,-92,-136,-136,-95,-96,158,158,158,158,158,158,-79,-82,-87,-90,158,-93,-97,-94,158,158,158,158,-65,158,158,158,158,158,158,158,158,-91,158,-99,-80,-81,-88,-89,158,158,158,-100,158,]),'SAME':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[159,-78,-136,-136,-92,-136,-136,-95,-96,159,159,159,159,159,159,-79,-82,-87,-90,159,-93,-97,-94,159,159,159,159,-65,159,159,159,159,159,159,159,159,-91,159,-99,-80,-81,-88,-89,159,159,159,-100,159,]),'AND':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[160,-78,-136,-136,-92,-136,-136,-95,-96,160,160,160,160,160,160,-79,-82,-87,-90,160,-93,-97,-94,160,160,160,160,-65,160,160,160,160,160,160,160,160,-91,160,-99,-80,-81,-88,-89,160,160,160,-100,160,]),'OR':([113,114,115,116,118,119,120,121,122,139,140,142,149,151,152,162,165,166,169,170,171,172,173,176,177,178,197,198,202,203,204,205,206,207,208,209,218,219,238,242,243,244,245,247,262,271,278,281,],[161,-78,-136,-136,-92,-136,-136,-95,-96,161,161,161,161,161,161,-79,-82,-87,-90,161,-93,-97,-94,161,161,161,161,-65,161,161,161,161,161,161,161,161,-91,161,-99,-80,-81,-88,-89,161,161,161,-100,161,]),'TO':([114,115,116,118,119,120,121,122,162,165,166,169,171,172,173,198,202,203,204,205,206,207,208,209,218,238,242,243,244,245,247,265,266,278,],[-78,-136,-136,-92,-136,-136,-95,-96,-79,-82,-87,-90,-93,-97,-94,-65,-70,-71,-72,-73,-74,-75,-76,-77,-91,-99,-80,-81,-88,-89,-136,274,-124,-100,]),'PLUS':([115,116,118,119,120,121,122,166,169,171,172,173,198,218,238,244,245,278,],[163,-136,-92,-136,-136,-95,-96,-87,-90,-93,-97,-94,-65,-91,-99,-88,-89,-100,]),'MINUS':([115,116,118,119,120,121,122,166,169,171,172,173,198,218,238,244,245,278,],[164,-136,-92,-136,-136,-95,-96,-87,-90,-93,-97,-94,-65,-91,-99,-88,-89,-100,]),'MULTIPLY':([116,118,119,120,121,122,171,172,173,198,218,238,278,],[167,-92,-136,-136,-95,-96,-93,-97,-94,-65,-91,-99,-100,]),'DIVIDE':([116,118,119,120,121,122,171,172,173,198,218,238,278,],[168,-92,-136,-136,-95,-96,-93,-97,-94,-65,-91,-99,-100,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start_program':([0,],[1,]),'cuadruploMain':([0,],[2,]),'empty':([0,12,18,31,32,35,44,45,50,60,87,96,110,115,116,119,120,134,135,136,163,164,167,168,192,199,246,247,260,273,284,289,],[3,24,29,37,37,43,53,53,61,61,124,29,150,165,169,172,172,187,53,187,211,213,215,217,234,150,264,266,270,280,288,292,]),'vars':([6,],[7,]),'multiple_funcs':([6,7,11,],[8,14,22,]),'main_body':([6,7,8,14,],[9,15,16,27,]),'dec_func':([6,7,11,],[11,11,11,]),'varss':([10,39,],[17,46,]),'type':([10,13,39,50,60,229,],[18,25,18,96,96,96,]),'crearTablaMain':([12,],[23,]),'guardarTipo':([18,96,],[28,133,]),'mvar':([28,40,101,232,],[33,47,138,259,]),'crearSymbolTable':([31,32,],[36,38,]),'gotoMain':([35,],[42,]),'body':([42,97,99,233,263,277,285,],[49,134,136,260,273,284,289,]),'param':([44,45,135,],[51,57,188,]),'typeParam':([44,45,135,],[52,52,52,]),'bodyy':([50,60,],[59,103,]),'statement':([50,60,],[60,60,]),'dec_variables':([50,60,],[62,62,]),'assignment':([50,60,],[63,63,]),'condition':([50,60,],[64,64,]),'writing':([50,60,],[65,65,]),'reading':([50,60,],[66,66,]),'call_func':([50,60,86,104,105,106,110,111,112,117,126,127,128,147,154,155,156,157,158,159,160,161,174,194,195,199,210,212,214,216,220,240,261,274,],[67,67,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,]),'graph':([50,60,],[68,68,]),'return':([50,60,],[69,69,]),'while_loop':([50,60,],[70,70,]),'for_loop':([50,60,],[71,71,]),'max':([50,60,],[72,72,]),'min':([50,60,],[73,73,]),'sum':([50,60,],[74,74,]),'normal':([50,60,],[75,75,]),'uniforme':([50,60,],[76,76,]),'poisson':([50,60,],[77,77,]),'binomial':([50,60,],[78,78,]),'dec_variabless':([50,60,229,],[79,79,256,]),'variableAssignment':([50,60,],[80,80,]),'multivariables':([83,146,],[107,196,]),'variable':([83,86,104,105,106,110,111,112,117,125,126,127,128,129,130,131,132,146,147,154,155,156,157,158,159,160,161,174,194,195,199,210,212,214,216,220,225,240,261,274,],[108,121,121,121,121,121,121,121,121,175,121,121,121,180,180,180,180,108,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,180,121,121,121,]),'exp':([86,104,105,106,110,111,112,117,126,127,128,147,154,155,156,157,158,159,160,161,174,194,195,199,220,240,261,274,],[113,139,140,142,149,151,152,170,176,177,178,197,202,203,204,205,206,207,208,209,219,142,142,149,247,262,271,281,]),'m_exp':([86,104,105,106,110,111,112,117,126,127,128,147,154,155,156,157,158,159,160,161,174,194,195,199,210,212,220,240,261,274,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,242,243,114,114,114,114,]),'t':([86,104,105,106,110,111,112,117,126,127,128,147,154,155,156,157,158,159,160,161,174,194,195,199,210,212,214,216,220,240,261,274,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,244,245,115,115,115,115,]),'f':([86,104,105,106,110,111,112,117,126,127,128,147,154,155,156,157,158,159,160,161,174,194,195,199,210,212,214,216,220,240,261,274,],[116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'whileMigaja':([87,],[123,]),'writingg':([106,194,195,],[141,236,237,]),'auxString':([106,194,195,],[143,143,143,]),'call_funcc':([110,199,],[148,239,]),'m_expp':([115,],[162,]),'termino':([116,],[166,]),'guardarConstante':([119,120,],[171,173,]),'param_dist':([129,130,131,132,225,],[179,181,182,183,252,]),'dec_mvar':([133,230,276,290,],[184,257,283,293,]),'exitFunc':([134,136,],[186,189,]),'appendPLUS':([163,],[210,]),'appendMINUS':([164,],[212,]),'appendMULTIPLY':([167,],[214,]),'appendDIVIDE':([168,],[216,]),'cuadruploIF':([192,],[233,]),'whileEval':([246,],[263,]),'guardarValorFor':([247,],[265,]),'ifEnd':([260,],[268,]),'cuadruploElse':([260,],[269,]),'whileEnd':([273,],[279,]),'ifEndElse':([284,],[287,]),'forEnd':([289,],[291,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start_program","S'",1,None,None,None),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body','start_program',7,'p_start_program','PLY.py',113),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON vars main_body','start_program',6,'p_start_program','PLY.py',114),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body','start_program',6,'p_start_program','PLY.py',115),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON main_body','start_program',5,'p_start_program','PLY.py',116),
  ('cuadruploMain -> empty','cuadruploMain',1,'p_cuadruploMain','PLY.py',135),
  ('multiple_funcs -> dec_func','multiple_funcs',1,'p_multiple_funcs','PLY.py',144),
  ('multiple_funcs -> dec_func multiple_funcs','multiple_funcs',2,'p_multiple_funcs','PLY.py',145),
  ('main_body -> MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body','main_body',6,'p_main_body','PLY.py',149),
  ('crearTablaMain -> empty','crearTablaMain',1,'p_crearTablaMain','PLY.py',153),
  ('gotoMain -> empty','gotoMain',1,'p_gotoMain','PLY.py',160),
  ('vars -> VAR varss','vars',2,'p_vars','PLY.py',176),
  ('varss -> type guardarTipo mvar SEMICOLON varss','varss',5,'p_varss','PLY.py',182),
  ('varss -> type guardarTipo mvar SEMICOLON','varss',4,'p_varss','PLY.py',183),
  ('guardarTipo -> empty','guardarTipo',1,'p_guardarTipo','PLY.py',190),
  ('mvar -> ID COLON mvar','mvar',3,'p_mvar','PLY.py',198),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',6,'p_mvar','PLY.py',199),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',9,'p_mvar','PLY.py',200),
  ('mvar -> ID','mvar',1,'p_mvar','PLY.py',201),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE','mvar',4,'p_mvar','PLY.py',202),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','mvar',7,'p_mvar','PLY.py',203),
  ('dec_func -> FUNCTION type ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc','dec_func',9,'p_dec_func','PLY.py',218),
  ('dec_func -> FUNCTION VOID ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc','dec_func',9,'p_dec_func','PLY.py',219),
  ('crearSymbolTable -> empty','crearSymbolTable',1,'p_crearSymbolTable','PLY.py',228),
  ('exitFunc -> empty','exitFunc',1,'p_exitFunc','PLY.py',242),
  ('param -> typeParam ID','param',2,'p_param','PLY.py',248),
  ('param -> typeParam ID COLON param','param',4,'p_param','PLY.py',249),
  ('param -> empty','param',1,'p_param','PLY.py',250),
  ('typeParam -> INT','typeParam',1,'p_typeParam','PLY.py',268),
  ('typeParam -> FLOAT','typeParam',1,'p_typeParam','PLY.py',269),
  ('typeParam -> CHAR','typeParam',1,'p_typeParam','PLY.py',270),
  ('type -> INT','type',1,'p_type','PLY.py',278),
  ('type -> FLOAT','type',1,'p_type','PLY.py',279),
  ('type -> CHAR','type',1,'p_type','PLY.py',280),
  ('body -> BRACKETOPEN bodyy BRACKETCLOSE','body',3,'p_body','PLY.py',286),
  ('bodyy -> statement','bodyy',1,'p_bodyy','PLY.py',291),
  ('bodyy -> statement bodyy','bodyy',2,'p_bodyy','PLY.py',292),
  ('bodyy -> empty','bodyy',1,'p_bodyy','PLY.py',293),
  ('statement -> dec_variables','statement',1,'p_statement','PLY.py',298),
  ('statement -> assignment','statement',1,'p_statement','PLY.py',299),
  ('statement -> condition','statement',1,'p_statement','PLY.py',300),
  ('statement -> writing','statement',1,'p_statement','PLY.py',301),
  ('statement -> reading','statement',1,'p_statement','PLY.py',302),
  ('statement -> call_func','statement',1,'p_statement','PLY.py',303),
  ('statement -> graph','statement',1,'p_statement','PLY.py',304),
  ('statement -> return','statement',1,'p_statement','PLY.py',305),
  ('statement -> while_loop','statement',1,'p_statement','PLY.py',306),
  ('statement -> for_loop','statement',1,'p_statement','PLY.py',307),
  ('statement -> max','statement',1,'p_statement','PLY.py',308),
  ('statement -> min','statement',1,'p_statement','PLY.py',309),
  ('statement -> sum','statement',1,'p_statement','PLY.py',310),
  ('statement -> normal','statement',1,'p_statement','PLY.py',311),
  ('statement -> uniforme','statement',1,'p_statement','PLY.py',312),
  ('statement -> poisson','statement',1,'p_statement','PLY.py',313),
  ('statement -> binomial','statement',1,'p_statement','PLY.py',314),
  ('dec_variables -> dec_variabless','dec_variables',1,'p_dec_variables','PLY.py',318),
  ('dec_variabless -> type guardarTipo dec_mvar SEMICOLON dec_variabless','dec_variabless',5,'p_dec_variabless','PLY.py',324),
  ('dec_variabless -> type guardarTipo dec_mvar SEMICOLON','dec_variabless',4,'p_dec_variabless','PLY.py',325),
  ('dec_mvar -> ID COLON dec_mvar','dec_mvar',3,'p_dec_mvar','PLY.py',334),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',6,'p_dec_mvar','PLY.py',335),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',9,'p_dec_mvar','PLY.py',336),
  ('dec_mvar -> ID','dec_mvar',1,'p_dec_mvar','PLY.py',337),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE','dec_mvar',4,'p_dec_mvar','PLY.py',338),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','dec_mvar',7,'p_dec_mvar','PLY.py',339),
  ('assignment -> variableAssignment EQUAL exp SEMICOLON','assignment',4,'p_assignment','PLY.py',361),
  ('call_func -> ID PARENOPEN call_funcc PARENCLOSE','call_func',4,'p_call_func','PLY.py',378),
  ('call_funcc -> exp','call_funcc',1,'p_call_funcc','PLY.py',382),
  ('call_funcc -> exp COLON call_funcc','call_funcc',3,'p_call_funcc','PLY.py',383),
  ('call_funcc -> empty','call_funcc',1,'p_call_funcc','PLY.py',384),
  ('graph -> PLOT PARENOPEN exp PARENCLOSE SEMICOLON','graph',5,'p_graph','PLY.py',388),
  ('exp -> exp GREATHERTHAN exp','exp',3,'p_exp','PLY.py',393),
  ('exp -> exp LESSTHAN exp','exp',3,'p_exp','PLY.py',394),
  ('exp -> exp GREATHEREQUAL exp','exp',3,'p_exp','PLY.py',395),
  ('exp -> exp LESSEQUAL exp','exp',3,'p_exp','PLY.py',396),
  ('exp -> exp DIFFERENT exp','exp',3,'p_exp','PLY.py',397),
  ('exp -> exp SAME exp','exp',3,'p_exp','PLY.py',398),
  ('exp -> exp AND exp','exp',3,'p_exp','PLY.py',399),
  ('exp -> exp OR exp','exp',3,'p_exp','PLY.py',400),
  ('exp -> m_exp','exp',1,'p_exp','PLY.py',401),
  ('m_exp -> t m_expp','m_exp',2,'p_m_exp','PLY.py',421),
  ('m_expp -> PLUS appendPLUS m_exp','m_expp',3,'p_m_expp','PLY.py',432),
  ('m_expp -> MINUS appendMINUS m_exp','m_expp',3,'p_m_expp','PLY.py',433),
  ('m_expp -> empty','m_expp',1,'p_m_expp','PLY.py',434),
  ('appendPLUS -> empty','appendPLUS',1,'p_appendPLUS','PLY.py',445),
  ('appendMINUS -> empty','appendMINUS',1,'p_appendMINUS','PLY.py',451),
  ('appendMULTIPLY -> empty','appendMULTIPLY',1,'p_appendMULTIPLY','PLY.py',457),
  ('appendDIVIDE -> empty','appendDIVIDE',1,'p_appendDIVIDE','PLY.py',463),
  ('t -> f termino','t',2,'p_t','PLY.py',469),
  ('termino -> MULTIPLY appendMULTIPLY t','termino',3,'p_termino','PLY.py',489),
  ('termino -> DIVIDE appendDIVIDE t','termino',3,'p_termino','PLY.py',490),
  ('termino -> empty','termino',1,'p_termino','PLY.py',491),
  ('f -> PARENOPEN exp PARENCLOSE','f',3,'p_f','PLY.py',502),
  ('f -> ID','f',1,'p_f','PLY.py',503),
  ('f -> CTEINT guardarConstante','f',2,'p_f','PLY.py',504),
  ('f -> CTFLOAT guardarConstante','f',2,'p_f','PLY.py',505),
  ('f -> variable','f',1,'p_f','PLY.py',506),
  ('f -> call_func','f',1,'p_f','PLY.py',507),
  ('guardarConstante -> empty','guardarConstante',1,'p_guardarConstante','PLY.py',544),
  ('variable -> ID','variable',1,'p_variable','PLY.py',553),
  ('variable -> ID BRACEOPEN exp BRACECLOSE','variable',4,'p_variable','PLY.py',554),
  ('variable -> ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE','variable',7,'p_variable','PLY.py',555),
  ('variableAssignment -> ID','variableAssignment',1,'p_variableAssignment','PLY.py',567),
  ('variableAssignment -> ID BRACEOPEN exp BRACECLOSE','variableAssignment',4,'p_variableAssignment','PLY.py',568),
  ('variableAssignment -> ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE','variableAssignment',7,'p_variableAssignment','PLY.py',569),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd','condition',7,'p_condition','PLY.py',605),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse','condition',10,'p_condition','PLY.py',606),
  ('cuadruploIF -> empty','cuadruploIF',1,'p_cuadruploIF','PLY.py',610),
  ('ifEnd -> empty','ifEnd',1,'p_ifEnd','PLY.py',625),
  ('cuadruploElse -> empty','cuadruploElse',1,'p_cuadruploElse','PLY.py',643),
  ('ifEndElse -> empty','ifEndElse',1,'p_ifEndElse','PLY.py',670),
  ('writing -> PRINT PARENOPEN writingg PARENCLOSE SEMICOLON','writing',5,'p_writing','PLY.py',683),
  ('writingg -> exp','writingg',1,'p_writingg','PLY.py',689),
  ('writingg -> exp COLON writingg','writingg',3,'p_writingg','PLY.py',690),
  ('writingg -> auxString','writingg',1,'p_writingg','PLY.py',691),
  ('writingg -> auxString COLON writingg','writingg',3,'p_writingg','PLY.py',692),
  ('auxString -> CTESTRING','auxString',1,'p_auxString','PLY.py',706),
  ('reading -> READ multivariables SEMICOLON','reading',3,'p_reading','PLY.py',714),
  ('multivariables -> variable','multivariables',1,'p_multivariables','PLY.py',719),
  ('multivariables -> variable COLON multivariables','multivariables',3,'p_multivariables','PLY.py',720),
  ('while_loop -> WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd','while_loop',8,'p_while_loop','PLY.py',732),
  ('whileMigaja -> empty','whileMigaja',1,'p_whileMigaja','PLY.py',737),
  ('whileEval -> empty','whileEval',1,'p_whileEval','PLY.py',745),
  ('whileEnd -> empty','whileEnd',1,'p_whileEnd','PLY.py',762),
  ('for_loop -> FOR PARENOPEN variable EQUAL exp guardarValorFor TO exp PARENCLOSE body forEnd','for_loop',11,'p_for_loop','PLY.py',790),
  ('guardarValorFor -> empty','guardarValorFor',1,'p_guardarValorFor','PLY.py',796),
  ('forEnd -> empty','forEnd',1,'p_forEnd','PLY.py',806),
  ('return -> RETURN exp SEMICOLON','return',3,'p_return','PLY.py',812),
  ('max -> MAX PARENOPEN exp PARENCLOSE SEMICOLON','max',5,'p_max','PLY.py',817),
  ('min -> MIN PARENOPEN exp PARENCLOSE SEMICOLON','min',5,'p_min','PLY.py',822),
  ('sum -> SUM PARENOPEN exp PARENCLOSE SEMICOLON','sum',5,'p_sum','PLY.py',827),
  ('param_dist -> variable','param_dist',1,'p_param_dist','PLY.py',832),
  ('param_dist -> variable COLON param_dist','param_dist',3,'p_param_dist','PLY.py',833),
  ('binomial -> BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON','binomial',5,'p_binomial','PLY.py',838),
  ('poisson -> POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON','poisson',5,'p_poisson','PLY.py',843),
  ('uniforme -> UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON','uniforme',5,'p_uniforme','PLY.py',848),
  ('normal -> NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON','normal',5,'p_normal','PLY.py',853),
  ('empty -> <empty>','empty',0,'p_empty','PLY.py',858),
]
