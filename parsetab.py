
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BINOMIAL BRACECLOSE BRACEOPEN BRACKETCLOSE BRACKETOPEN CHAR COLON CTEINT CTESTRING CTFLOAT DIFFERENT DIVIDE ELSE EQUAL FLOAT FOR FUNCTION GREATHEREQUAL GREATHERTHAN ID IF INT LESSEQUAL LESSTHAN MAIN MAX MIN MINUS MULTIPLY NORMAL OR PARENCLOSE PARENOPEN PLOT PLUS POISSON PRINT PROGRAM READ RETURN SAME SEMICOLON SUM TO UNIFORME VAR VOID WHILE\n    start_program : cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body\n    | cuadruploMain PROGRAM ID SEMICOLON vars main_body\n    | cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body\n    | cuadruploMain PROGRAM ID SEMICOLON main_body\n    \n    cuadruploMain : empty\n    \n    multiple_funcs : dec_func \n    | dec_func multiple_funcs\n    \n    main_body : MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body \n    \n    crearTablaMain : empty\n    \n    gotoMain : empty\n    \n    vars : VAR varss\n    \n    varss : type guardarTipo mvar SEMICOLON varss\n    | type guardarTipo mvar SEMICOLON\n    \n    guardarTipo : empty\n    \n    mvar : ID COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    dec_func : FUNCTION type ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc\n    | FUNCTION VOID ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc\n    \n    crearSymbolTable : empty\n    \n    exitFunc : empty\n    \n    param : typeParam ID\n    | typeParam ID COLON param\n    | empty\n    \n    typeParam : INT\n    | FLOAT\n    | CHAR\n    \n    type : INT\n    | FLOAT\n    | CHAR\n    \n    body : BRACKETOPEN bodyy BRACKETCLOSE\n    \n    bodyy : statement \n    | statement bodyy\n    | empty\n    \n    statement : dec_variables \n    | assignment\n    | condition\n    | writing\n    | reading\n    | call_func\n    | graph\n    | return\n    | while_loop\n    | for_loop\n    | max\n    | min\n    | sum\n    | normal\n    | uniforme\n    | poisson\n    | binomial\n    \n    dec_variables : dec_variabless\n    \n    dec_variabless : type guardarTipo dec_mvar SEMICOLON dec_variabless\n    | type guardarTipo dec_mvar SEMICOLON\n    \n    dec_mvar : ID COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    assignment : variable EQUAL exp SEMICOLON\n    \n    call_func : ID PARENOPEN call_funcc PARENCLOSE\n    \n    call_funcc : exp \n    | exp COLON call_funcc\n    | empty\n    \n    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON\n    \n    \n    exp : exp GREATHERTHAN exp \n    | exp LESSTHAN exp \n    | exp GREATHEREQUAL exp \n    | exp LESSEQUAL exp \n    | exp DIFFERENT exp \n    | exp SAME exp\n    | exp AND exp\n    | exp OR exp\n    | m_exp\n    \n    m_exp : t m_expp \n    \n    m_expp : PLUS appendPLUS m_exp\n        | MINUS appendMINUS m_exp\n        | empty\n    \n    appendPLUS : empty\n    \n    appendMINUS : empty\n    \n    appendMULTIPLY : empty\n    \n    appendDIVIDE : empty\n    \n    t : f termino\n    \n    termino : MULTIPLY appendMULTIPLY t \n        | DIVIDE appendDIVIDE t \n        | empty\n    \n    f : PARENOPEN exp PARENCLOSE \n    | ID\n    | CTEINT\n    | CTFLOAT \n    | variable\n    | call_func\n    \n    variable : ID \n    | ID BRACEOPEN exp BRACECLOSE \n    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE\n    \n    condition : IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd\n        | IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse\n    \n    cuadruploIF : empty \n    \n    ifEnd : empty \n    \n    cuadruploElse : empty \n    \n    ifEndElse : empty \n    \n    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON\n    \n    writingg : exp\n    | exp COLON writingg\n    | auxString\n    | auxString COLON writingg\n    \n    auxString : CTESTRING\n       \n    \n    reading : READ multivariables SEMICOLON\n       \n    \n    multivariables : variable\n    | variable COLON multivariables\n       \n    \n    while_loop : WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd\n       \n    \n    whileMigaja : empty\n       \n    \n    whileEval : empty\n       \n    \n    whileEnd : empty\n       \n    \n    for_loop : FOR PARENOPEN variable EQUAL exp guardarValorFor TO exp PARENCLOSE body forEnd\n\n    \n    guardarValorFor : empty\n\n    \n    forEnd : empty\n\n    \n    return : RETURN exp SEMICOLON\n       \n    \n    max : MAX PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    min : MIN PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    sum : SUM PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    param_dist : variable\n    | variable COLON param_dist\n       \n    \n    binomial : BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    poisson : POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    uniforme : UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    normal : NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,2,3,],[-132,4,-5,]),'$end':([1,9,15,16,27,49,102,],[0,-4,-2,-3,-1,-8,-34,]),'ID':([4,18,19,20,21,25,26,28,29,40,50,52,54,55,56,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,83,86,96,101,102,104,105,106,110,111,112,117,125,126,127,128,129,130,131,132,133,145,146,152,153,154,155,156,157,158,159,160,162,163,166,167,170,187,190,191,193,194,205,206,207,208,209,210,211,212,215,220,224,225,227,230,234,235,242,243,244,245,247,248,249,250,254,261,263,265,266,268,270,271,275,278,279,280,281,282,283,],[5,-132,-31,-32,-33,31,32,34,-14,34,84,98,-28,-29,-30,84,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,109,118,-132,34,-34,118,118,118,118,118,118,118,109,118,118,118,109,109,109,109,181,-112,109,-122,118,118,118,118,118,118,118,118,-132,-132,-132,-132,118,-64,118,118,-65,118,118,-83,118,-84,118,-85,118,-86,118,109,-57,181,34,-106,118,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,118,181,-115,-118,-132,-101,-105,-132,181,-119,-121,]),'SEMICOLON':([5,33,34,47,58,107,108,109,113,114,115,116,118,119,120,121,122,138,139,161,164,165,168,180,181,186,189,192,193,195,196,197,198,199,200,201,202,203,204,213,216,217,218,219,221,222,223,236,237,238,239,251,253,260,264,274,277,284,],[6,39,-18,-15,-19,145,-113,-97,152,-78,-132,-132,-92,-93,-94,-95,-96,-16,187,-79,-82,-87,-90,224,-61,-20,230,-114,-65,-98,235,-70,-71,-72,-73,-74,-75,-76,-77,-91,242,243,244,245,247,248,249,-80,-81,-88,-89,-58,-17,-62,-99,-59,-63,-60,]),'VAR':([6,],[10,]),'MAIN':([6,7,8,11,14,17,22,39,46,102,134,136,182,183,185,],[12,12,12,-6,12,-11,-7,-13,-12,-34,-132,-132,-21,-24,-22,]),'FUNCTION':([6,7,11,17,39,46,102,134,136,182,183,185,],[13,13,13,-11,-13,-12,-34,-132,-132,-21,-24,-22,]),'INT':([10,13,39,44,45,50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,135,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[19,19,19,54,54,19,19,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,54,-112,-122,-64,-65,19,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'FLOAT':([10,13,39,44,45,50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,135,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[20,20,20,55,55,20,20,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,55,-112,-122,-64,-65,20,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'CHAR':([10,13,39,44,45,50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,135,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[21,21,21,56,56,21,21,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,56,-112,-122,-64,-65,21,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'PARENOPEN':([12,23,24,31,32,36,37,38,81,82,84,85,86,87,88,89,90,91,92,93,94,95,104,105,106,110,111,112,117,118,123,124,126,127,128,153,154,155,156,157,158,159,160,162,163,166,167,170,190,191,194,205,206,207,208,209,210,211,212,215,234,266,],[-132,30,-9,-132,-132,44,-23,45,105,106,110,112,117,-132,125,126,127,128,129,130,131,132,117,117,117,117,117,117,117,110,170,-116,117,117,117,117,117,117,117,117,117,117,117,-132,-132,-132,-132,117,117,117,117,117,-83,117,-84,117,-85,117,-86,117,117,117,]),'VOID':([13,],[26,]),'PARENCLOSE':([30,44,45,51,53,57,98,109,110,114,115,116,118,119,120,121,122,135,140,141,142,143,144,147,148,149,151,161,164,165,168,169,172,173,174,175,176,177,178,179,184,193,194,195,197,198,199,200,201,202,203,204,213,214,231,232,233,236,237,238,239,246,264,272,],[35,-132,-132,97,-27,99,-25,-97,-132,-78,-132,-132,-92,-93,-94,-95,-96,-132,188,189,-107,-109,-111,193,-66,-68,196,-79,-82,-87,-90,213,216,217,218,219,-126,221,222,223,-26,-65,-132,-98,-70,-71,-72,-73,-74,-75,-76,-77,-91,240,-108,-110,-67,-80,-81,-88,-89,-127,-99,276,]),'COLON':([34,58,98,108,109,114,115,116,118,119,120,121,122,142,143,144,148,161,164,165,168,176,181,186,193,195,197,198,199,200,201,202,203,204,213,236,237,238,239,260,264,277,],[40,101,135,146,-97,-78,-132,-132,-92,-93,-94,-95,-96,190,191,-111,194,-79,-82,-87,-90,220,225,227,-65,-98,-70,-71,-72,-73,-74,-75,-76,-77,-91,-80,-81,-88,-89,268,-99,281,]),'BRACEOPEN':([34,58,84,109,118,181,195,260,],[41,100,111,111,111,226,234,267,]),'BRACKETOPEN':([35,42,43,97,99,188,228,229,240,256,257,269,276,],[-132,50,-10,50,50,-132,50,-102,-132,50,-117,50,50,]),'CTEINT':([41,86,100,104,105,106,110,111,112,117,126,127,128,153,154,155,156,157,158,159,160,162,163,166,167,170,190,191,194,205,206,207,208,209,210,211,212,215,226,234,266,267,],[48,119,137,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,-132,-132,-132,-132,119,119,119,119,119,-83,119,-84,119,-85,119,-86,119,252,119,119,273,]),'BRACECLOSE':([48,114,115,116,118,119,120,121,122,137,150,161,164,165,168,193,195,197,198,199,200,201,202,203,204,213,236,237,238,239,252,255,264,273,],[58,-78,-132,-132,-92,-93,-94,-95,-96,186,195,-79,-82,-87,-90,-65,-98,-70,-71,-72,-73,-74,-75,-76,-77,-91,-80,-81,-88,-89,260,264,-99,277,]),'BRACKETCLOSE':([50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,103,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[-132,102,-35,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-36,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'IF':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[81,81,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'PRINT':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[82,82,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'READ':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[83,83,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'PLOT':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[85,85,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'RETURN':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[86,86,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'WHILE':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[87,87,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'FOR':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[88,88,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'MAX':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[89,89,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'MIN':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[90,90,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'SUM':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[91,91,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'NORMAL':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[92,92,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'UNIFORME':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[93,93,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'POISSON':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[94,94,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'BINOMIAL':([50,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,102,145,152,187,193,224,230,235,242,243,244,245,247,248,249,250,254,261,263,265,270,271,275,278,279,280,282,283,],[95,95,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-34,-112,-122,-64,-65,-57,-106,-69,-123,-124,-125,-131,-130,-129,-128,-56,-132,-100,-103,-132,-115,-118,-132,-101,-105,-132,-119,-121,]),'EQUAL':([80,84,109,171,195,264,],[104,-97,-97,215,-98,-99,]),'CTFLOAT':([86,104,105,106,110,111,112,117,126,127,128,153,154,155,156,157,158,159,160,162,163,166,167,170,190,191,194,205,206,207,208,209,210,211,212,215,234,266,],[120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,-132,-132,-132,-132,120,120,120,120,120,-83,120,-84,120,-85,120,-86,120,120,120,]),'ELSE':([102,254,262,263,],[-34,-132,269,-104,]),'CTESTRING':([106,190,191,],[144,144,144,]),'GREATHERTHAN':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[153,-78,-132,-132,-92,-93,-94,-95,-96,153,153,153,153,153,153,-79,-82,-87,-90,153,153,153,153,-65,-98,153,153,153,153,153,153,153,153,-91,153,-80,-81,-88,-89,153,153,-99,153,]),'LESSTHAN':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[154,-78,-132,-132,-92,-93,-94,-95,-96,154,154,154,154,154,154,-79,-82,-87,-90,154,154,154,154,-65,-98,154,154,154,154,154,154,154,154,-91,154,-80,-81,-88,-89,154,154,-99,154,]),'GREATHEREQUAL':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[155,-78,-132,-132,-92,-93,-94,-95,-96,155,155,155,155,155,155,-79,-82,-87,-90,155,155,155,155,-65,-98,155,155,155,155,155,155,155,155,-91,155,-80,-81,-88,-89,155,155,-99,155,]),'LESSEQUAL':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[156,-78,-132,-132,-92,-93,-94,-95,-96,156,156,156,156,156,156,-79,-82,-87,-90,156,156,156,156,-65,-98,156,156,156,156,156,156,156,156,-91,156,-80,-81,-88,-89,156,156,-99,156,]),'DIFFERENT':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[157,-78,-132,-132,-92,-93,-94,-95,-96,157,157,157,157,157,157,-79,-82,-87,-90,157,157,157,157,-65,-98,157,157,157,157,157,157,157,157,-91,157,-80,-81,-88,-89,157,157,-99,157,]),'SAME':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[158,-78,-132,-132,-92,-93,-94,-95,-96,158,158,158,158,158,158,-79,-82,-87,-90,158,158,158,158,-65,-98,158,158,158,158,158,158,158,158,-91,158,-80,-81,-88,-89,158,158,-99,158,]),'AND':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[159,-78,-132,-132,-92,-93,-94,-95,-96,159,159,159,159,159,159,-79,-82,-87,-90,159,159,159,159,-65,-98,159,159,159,159,159,159,159,159,-91,159,-80,-81,-88,-89,159,159,-99,159,]),'OR':([113,114,115,116,118,119,120,121,122,139,140,142,148,150,151,161,164,165,168,169,172,173,174,193,195,197,198,199,200,201,202,203,204,213,214,236,237,238,239,241,255,264,272,],[160,-78,-132,-132,-92,-93,-94,-95,-96,160,160,160,160,160,160,-79,-82,-87,-90,160,160,160,160,-65,-98,160,160,160,160,160,160,160,160,-91,160,-80,-81,-88,-89,160,160,-99,160,]),'TO':([114,115,116,118,119,120,121,122,161,164,165,168,193,195,197,198,199,200,201,202,203,204,213,236,237,238,239,241,258,259,264,],[-78,-132,-132,-92,-93,-94,-95,-96,-79,-82,-87,-90,-65,-98,-70,-71,-72,-73,-74,-75,-76,-77,-91,-80,-81,-88,-89,-132,266,-120,-99,]),'PLUS':([115,116,118,119,120,121,122,165,168,193,195,213,238,239,264,],[162,-132,-92,-93,-94,-95,-96,-87,-90,-65,-98,-91,-88,-89,-99,]),'MINUS':([115,116,118,119,120,121,122,165,168,193,195,213,238,239,264,],[163,-132,-92,-93,-94,-95,-96,-87,-90,-65,-98,-91,-88,-89,-99,]),'MULTIPLY':([116,118,119,120,121,122,193,195,213,264,],[166,-92,-93,-94,-95,-96,-65,-98,-91,-99,]),'DIVIDE':([116,118,119,120,121,122,193,195,213,264,],[167,-92,-93,-94,-95,-96,-65,-98,-91,-99,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start_program':([0,],[1,]),'cuadruploMain':([0,],[2,]),'empty':([0,12,18,31,32,35,44,45,50,60,87,96,110,115,116,134,135,136,162,163,166,167,188,194,240,241,254,265,275,280,],[3,24,29,37,37,43,53,53,61,61,124,29,149,164,168,183,53,183,206,208,210,212,229,149,257,259,263,271,279,283,]),'vars':([6,],[7,]),'multiple_funcs':([6,7,11,],[8,14,22,]),'main_body':([6,7,8,14,],[9,15,16,27,]),'dec_func':([6,7,11,],[11,11,11,]),'varss':([10,39,],[17,46,]),'type':([10,13,39,50,60,224,],[18,25,18,96,96,96,]),'crearTablaMain':([12,],[23,]),'guardarTipo':([18,96,],[28,133,]),'mvar':([28,40,101,227,],[33,47,138,253,]),'crearSymbolTable':([31,32,],[36,38,]),'gotoMain':([35,],[42,]),'body':([42,97,99,228,256,269,276,],[49,134,136,254,265,275,280,]),'param':([44,45,135,],[51,57,184,]),'typeParam':([44,45,135,],[52,52,52,]),'bodyy':([50,60,],[59,103,]),'statement':([50,60,],[60,60,]),'dec_variables':([50,60,],[62,62,]),'assignment':([50,60,],[63,63,]),'condition':([50,60,],[64,64,]),'writing':([50,60,],[65,65,]),'reading':([50,60,],[66,66,]),'call_func':([50,60,86,104,105,106,110,111,112,117,126,127,128,153,154,155,156,157,158,159,160,170,190,191,194,205,207,209,211,215,234,266,],[67,67,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,]),'graph':([50,60,],[68,68,]),'return':([50,60,],[69,69,]),'while_loop':([50,60,],[70,70,]),'for_loop':([50,60,],[71,71,]),'max':([50,60,],[72,72,]),'min':([50,60,],[73,73,]),'sum':([50,60,],[74,74,]),'normal':([50,60,],[75,75,]),'uniforme':([50,60,],[76,76,]),'poisson':([50,60,],[77,77,]),'binomial':([50,60,],[78,78,]),'dec_variabless':([50,60,224,],[79,79,250,]),'variable':([50,60,83,86,104,105,106,110,111,112,117,125,126,127,128,129,130,131,132,146,153,154,155,156,157,158,159,160,170,190,191,194,205,207,209,211,215,220,234,266,],[80,80,108,121,121,121,121,121,121,121,121,171,121,121,121,176,176,176,176,108,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,176,121,121,]),'multivariables':([83,146,],[107,192,]),'exp':([86,104,105,106,110,111,112,117,126,127,128,153,154,155,156,157,158,159,160,170,190,191,194,215,234,266,],[113,139,140,142,148,150,151,169,172,173,174,197,198,199,200,201,202,203,204,214,142,142,148,241,255,272,]),'m_exp':([86,104,105,106,110,111,112,117,126,127,128,153,154,155,156,157,158,159,160,170,190,191,194,205,207,215,234,266,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,236,237,114,114,114,]),'t':([86,104,105,106,110,111,112,117,126,127,128,153,154,155,156,157,158,159,160,170,190,191,194,205,207,209,211,215,234,266,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,238,239,115,115,115,]),'f':([86,104,105,106,110,111,112,117,126,127,128,153,154,155,156,157,158,159,160,170,190,191,194,205,207,209,211,215,234,266,],[116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'whileMigaja':([87,],[123,]),'writingg':([106,190,191,],[141,231,232,]),'auxString':([106,190,191,],[143,143,143,]),'call_funcc':([110,194,],[147,233,]),'m_expp':([115,],[161,]),'termino':([116,],[165,]),'param_dist':([129,130,131,132,220,],[175,177,178,179,246,]),'dec_mvar':([133,225,268,281,],[180,251,274,284,]),'exitFunc':([134,136,],[182,185,]),'appendPLUS':([162,],[205,]),'appendMINUS':([163,],[207,]),'appendMULTIPLY':([166,],[209,]),'appendDIVIDE':([167,],[211,]),'cuadruploIF':([188,],[228,]),'whileEval':([240,],[256,]),'guardarValorFor':([241,],[258,]),'ifEnd':([254,],[261,]),'cuadruploElse':([254,],[262,]),'whileEnd':([265,],[270,]),'ifEndElse':([275,],[278,]),'forEnd':([280,],[282,]),}

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
  ('cuadruploMain -> empty','cuadruploMain',1,'p_cuadruploMain','PLY.py',134),
  ('multiple_funcs -> dec_func','multiple_funcs',1,'p_multiple_funcs','PLY.py',143),
  ('multiple_funcs -> dec_func multiple_funcs','multiple_funcs',2,'p_multiple_funcs','PLY.py',144),
  ('main_body -> MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body','main_body',6,'p_main_body','PLY.py',148),
  ('crearTablaMain -> empty','crearTablaMain',1,'p_crearTablaMain','PLY.py',152),
  ('gotoMain -> empty','gotoMain',1,'p_gotoMain','PLY.py',159),
  ('vars -> VAR varss','vars',2,'p_vars','PLY.py',175),
  ('varss -> type guardarTipo mvar SEMICOLON varss','varss',5,'p_varss','PLY.py',181),
  ('varss -> type guardarTipo mvar SEMICOLON','varss',4,'p_varss','PLY.py',182),
  ('guardarTipo -> empty','guardarTipo',1,'p_guardarTipo','PLY.py',189),
  ('mvar -> ID COLON mvar','mvar',3,'p_mvar','PLY.py',197),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',6,'p_mvar','PLY.py',198),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',9,'p_mvar','PLY.py',199),
  ('mvar -> ID','mvar',1,'p_mvar','PLY.py',200),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE','mvar',4,'p_mvar','PLY.py',201),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','mvar',7,'p_mvar','PLY.py',202),
  ('dec_func -> FUNCTION type ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc','dec_func',9,'p_dec_func','PLY.py',217),
  ('dec_func -> FUNCTION VOID ID crearSymbolTable PARENOPEN param PARENCLOSE body exitFunc','dec_func',9,'p_dec_func','PLY.py',218),
  ('crearSymbolTable -> empty','crearSymbolTable',1,'p_crearSymbolTable','PLY.py',227),
  ('exitFunc -> empty','exitFunc',1,'p_exitFunc','PLY.py',241),
  ('param -> typeParam ID','param',2,'p_param','PLY.py',247),
  ('param -> typeParam ID COLON param','param',4,'p_param','PLY.py',248),
  ('param -> empty','param',1,'p_param','PLY.py',249),
  ('typeParam -> INT','typeParam',1,'p_typeParam','PLY.py',267),
  ('typeParam -> FLOAT','typeParam',1,'p_typeParam','PLY.py',268),
  ('typeParam -> CHAR','typeParam',1,'p_typeParam','PLY.py',269),
  ('type -> INT','type',1,'p_type','PLY.py',277),
  ('type -> FLOAT','type',1,'p_type','PLY.py',278),
  ('type -> CHAR','type',1,'p_type','PLY.py',279),
  ('body -> BRACKETOPEN bodyy BRACKETCLOSE','body',3,'p_body','PLY.py',285),
  ('bodyy -> statement','bodyy',1,'p_bodyy','PLY.py',290),
  ('bodyy -> statement bodyy','bodyy',2,'p_bodyy','PLY.py',291),
  ('bodyy -> empty','bodyy',1,'p_bodyy','PLY.py',292),
  ('statement -> dec_variables','statement',1,'p_statement','PLY.py',297),
  ('statement -> assignment','statement',1,'p_statement','PLY.py',298),
  ('statement -> condition','statement',1,'p_statement','PLY.py',299),
  ('statement -> writing','statement',1,'p_statement','PLY.py',300),
  ('statement -> reading','statement',1,'p_statement','PLY.py',301),
  ('statement -> call_func','statement',1,'p_statement','PLY.py',302),
  ('statement -> graph','statement',1,'p_statement','PLY.py',303),
  ('statement -> return','statement',1,'p_statement','PLY.py',304),
  ('statement -> while_loop','statement',1,'p_statement','PLY.py',305),
  ('statement -> for_loop','statement',1,'p_statement','PLY.py',306),
  ('statement -> max','statement',1,'p_statement','PLY.py',307),
  ('statement -> min','statement',1,'p_statement','PLY.py',308),
  ('statement -> sum','statement',1,'p_statement','PLY.py',309),
  ('statement -> normal','statement',1,'p_statement','PLY.py',310),
  ('statement -> uniforme','statement',1,'p_statement','PLY.py',311),
  ('statement -> poisson','statement',1,'p_statement','PLY.py',312),
  ('statement -> binomial','statement',1,'p_statement','PLY.py',313),
  ('dec_variables -> dec_variabless','dec_variables',1,'p_dec_variables','PLY.py',317),
  ('dec_variabless -> type guardarTipo dec_mvar SEMICOLON dec_variabless','dec_variabless',5,'p_dec_variabless','PLY.py',323),
  ('dec_variabless -> type guardarTipo dec_mvar SEMICOLON','dec_variabless',4,'p_dec_variabless','PLY.py',324),
  ('dec_mvar -> ID COLON dec_mvar','dec_mvar',3,'p_dec_mvar','PLY.py',333),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',6,'p_dec_mvar','PLY.py',334),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',9,'p_dec_mvar','PLY.py',335),
  ('dec_mvar -> ID','dec_mvar',1,'p_dec_mvar','PLY.py',336),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE','dec_mvar',4,'p_dec_mvar','PLY.py',337),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','dec_mvar',7,'p_dec_mvar','PLY.py',338),
  ('assignment -> variable EQUAL exp SEMICOLON','assignment',4,'p_assignment','PLY.py',360),
  ('call_func -> ID PARENOPEN call_funcc PARENCLOSE','call_func',4,'p_call_func','PLY.py',377),
  ('call_funcc -> exp','call_funcc',1,'p_call_funcc','PLY.py',381),
  ('call_funcc -> exp COLON call_funcc','call_funcc',3,'p_call_funcc','PLY.py',382),
  ('call_funcc -> empty','call_funcc',1,'p_call_funcc','PLY.py',383),
  ('graph -> PLOT PARENOPEN exp PARENCLOSE SEMICOLON','graph',5,'p_graph','PLY.py',387),
  ('exp -> exp GREATHERTHAN exp','exp',3,'p_exp','PLY.py',392),
  ('exp -> exp LESSTHAN exp','exp',3,'p_exp','PLY.py',393),
  ('exp -> exp GREATHEREQUAL exp','exp',3,'p_exp','PLY.py',394),
  ('exp -> exp LESSEQUAL exp','exp',3,'p_exp','PLY.py',395),
  ('exp -> exp DIFFERENT exp','exp',3,'p_exp','PLY.py',396),
  ('exp -> exp SAME exp','exp',3,'p_exp','PLY.py',397),
  ('exp -> exp AND exp','exp',3,'p_exp','PLY.py',398),
  ('exp -> exp OR exp','exp',3,'p_exp','PLY.py',399),
  ('exp -> m_exp','exp',1,'p_exp','PLY.py',400),
  ('m_exp -> t m_expp','m_exp',2,'p_m_exp','PLY.py',420),
  ('m_expp -> PLUS appendPLUS m_exp','m_expp',3,'p_m_expp','PLY.py',431),
  ('m_expp -> MINUS appendMINUS m_exp','m_expp',3,'p_m_expp','PLY.py',432),
  ('m_expp -> empty','m_expp',1,'p_m_expp','PLY.py',433),
  ('appendPLUS -> empty','appendPLUS',1,'p_appendPLUS','PLY.py',444),
  ('appendMINUS -> empty','appendMINUS',1,'p_appendMINUS','PLY.py',450),
  ('appendMULTIPLY -> empty','appendMULTIPLY',1,'p_appendMULTIPLY','PLY.py',456),
  ('appendDIVIDE -> empty','appendDIVIDE',1,'p_appendDIVIDE','PLY.py',462),
  ('t -> f termino','t',2,'p_t','PLY.py',468),
  ('termino -> MULTIPLY appendMULTIPLY t','termino',3,'p_termino','PLY.py',488),
  ('termino -> DIVIDE appendDIVIDE t','termino',3,'p_termino','PLY.py',489),
  ('termino -> empty','termino',1,'p_termino','PLY.py',490),
  ('f -> PARENOPEN exp PARENCLOSE','f',3,'p_f','PLY.py',501),
  ('f -> ID','f',1,'p_f','PLY.py',502),
  ('f -> CTEINT','f',1,'p_f','PLY.py',503),
  ('f -> CTFLOAT','f',1,'p_f','PLY.py',504),
  ('f -> variable','f',1,'p_f','PLY.py',505),
  ('f -> call_func','f',1,'p_f','PLY.py',506),
  ('variable -> ID','variable',1,'p_variable','PLY.py',540),
  ('variable -> ID BRACEOPEN exp BRACECLOSE','variable',4,'p_variable','PLY.py',541),
  ('variable -> ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE','variable',7,'p_variable','PLY.py',542),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd','condition',7,'p_condition','PLY.py',554),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse','condition',10,'p_condition','PLY.py',555),
  ('cuadruploIF -> empty','cuadruploIF',1,'p_cuadruploIF','PLY.py',559),
  ('ifEnd -> empty','ifEnd',1,'p_ifEnd','PLY.py',574),
  ('cuadruploElse -> empty','cuadruploElse',1,'p_cuadruploElse','PLY.py',592),
  ('ifEndElse -> empty','ifEndElse',1,'p_ifEndElse','PLY.py',619),
  ('writing -> PRINT PARENOPEN writingg PARENCLOSE SEMICOLON','writing',5,'p_writing','PLY.py',632),
  ('writingg -> exp','writingg',1,'p_writingg','PLY.py',638),
  ('writingg -> exp COLON writingg','writingg',3,'p_writingg','PLY.py',639),
  ('writingg -> auxString','writingg',1,'p_writingg','PLY.py',640),
  ('writingg -> auxString COLON writingg','writingg',3,'p_writingg','PLY.py',641),
  ('auxString -> CTESTRING','auxString',1,'p_auxString','PLY.py',655),
  ('reading -> READ multivariables SEMICOLON','reading',3,'p_reading','PLY.py',663),
  ('multivariables -> variable','multivariables',1,'p_multivariables','PLY.py',668),
  ('multivariables -> variable COLON multivariables','multivariables',3,'p_multivariables','PLY.py',669),
  ('while_loop -> WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd','while_loop',8,'p_while_loop','PLY.py',681),
  ('whileMigaja -> empty','whileMigaja',1,'p_whileMigaja','PLY.py',686),
  ('whileEval -> empty','whileEval',1,'p_whileEval','PLY.py',694),
  ('whileEnd -> empty','whileEnd',1,'p_whileEnd','PLY.py',711),
  ('for_loop -> FOR PARENOPEN variable EQUAL exp guardarValorFor TO exp PARENCLOSE body forEnd','for_loop',11,'p_for_loop','PLY.py',739),
  ('guardarValorFor -> empty','guardarValorFor',1,'p_guardarValorFor','PLY.py',745),
  ('forEnd -> empty','forEnd',1,'p_forEnd','PLY.py',755),
  ('return -> RETURN exp SEMICOLON','return',3,'p_return','PLY.py',761),
  ('max -> MAX PARENOPEN exp PARENCLOSE SEMICOLON','max',5,'p_max','PLY.py',766),
  ('min -> MIN PARENOPEN exp PARENCLOSE SEMICOLON','min',5,'p_min','PLY.py',771),
  ('sum -> SUM PARENOPEN exp PARENCLOSE SEMICOLON','sum',5,'p_sum','PLY.py',776),
  ('param_dist -> variable','param_dist',1,'p_param_dist','PLY.py',781),
  ('param_dist -> variable COLON param_dist','param_dist',3,'p_param_dist','PLY.py',782),
  ('binomial -> BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON','binomial',5,'p_binomial','PLY.py',787),
  ('poisson -> POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON','poisson',5,'p_poisson','PLY.py',792),
  ('uniforme -> UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON','uniforme',5,'p_uniforme','PLY.py',797),
  ('normal -> NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON','normal',5,'p_normal','PLY.py',802),
  ('empty -> <empty>','empty',0,'p_empty','PLY.py',807),
]
