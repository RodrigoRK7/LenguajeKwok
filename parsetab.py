
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BINOMIAL BRACECLOSE BRACEOPEN BRACKETCLOSE BRACKETOPEN CHAR COLON CTECHAR CTEINT CTESTRING CTFLOAT DIFFERENT DIVIDE ELSE EQUAL FLOAT FOR FUNCTION GREATHEREQUAL GREATHERTHAN ID IF INT LESSEQUAL LESSTHAN MAIN MAX MIN MINUS MULTIPLY NORMAL OR PARENCLOSE PARENOPEN PLOT PLUS POISSON PRINT PROGRAM READ RETURN SAME SEMICOLON SUM TO UNIFORME VAR VOID WHILE\n    start_program : cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body end\n    | cuadruploMain PROGRAM ID SEMICOLON vars main_body end\n    | cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body end\n    | cuadruploMain PROGRAM ID SEMICOLON main_body end\n    \n    cuadruploMain : empty\n    \n    main_body : MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body \n    \n    crearTablaMain : empty\n    \n    gotoMain : empty\n    \n    end : empty\n    \n    vars : VAR varss\n    \n    varss : type guardarTipo mvar SEMICOLON varss\n    | type guardarTipo mvar SEMICOLON\n    \n    guardarTipo : empty\n    \n    mvar : ID guardarIDvar COLON mvar\n    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID guardarIDvar\n    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE \n    | ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    guardarIDvar : empty\n    \n    multiple_funcs : dec_func \n    | dec_func multiple_funcs\n    \n    dec_func : FUNCTION type ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc\n    | FUNCTION VOID ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc\n    \n    crearSymbolTable : empty\n    \n    param : typeParam ID\n    | typeParam ID COLON param\n    | empty\n    \n    typeParam : INT\n    | FLOAT\n    | CHAR\n    \n    numeroParam : empty\n    \n    startFunc : empty\n    \n    exitFunc : empty\n    \n    type : INT\n    | FLOAT\n    | CHAR\n    \n    body : BRACKETOPEN bodyy BRACKETCLOSE\n    \n    bodyy : statement \n    | statement bodyy\n    | empty\n    \n    statement : dec_variables \n    | assignment\n    | condition\n    | writing\n    | reading\n    | call_func\n    | graph\n    | return\n    | while_loop\n    | max\n    | min\n    | sum\n    | normal\n    | uniforme\n    | poisson\n    | binomial\n    \n    dec_variables : dec_variabless\n    \n    dec_variabless : type guardarTipo dec_mvar SEMICOLON dec_variabless\n    | type guardarTipo dec_mvar SEMICOLON\n    \n    dec_mvar : ID guardarID COLON dec_mvar\n    | ID guardarID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID guardarID\n    | ID guardarID BRACEOPEN CTEINT BRACECLOSE \n    | ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    guardarID : empty\n    \n    assignment : variableAssignment EQUAL exp SEMICOLON\n    \n    call_func : ID generarERA PARENOPEN call_funcc PARENCLOSE\n    \n    generarERA : empty\n    \n    call_funcc : exp mandarParam\n    | exp mandarParam COLON call_funcc\n    | empty\n    \n    mandarParam : empty\n    \n    exp : expp\n    | exp AND expp\n    | exp OR expp\n    \n    expp : m_exp\n    | expp GREATHERTHAN m_exp \n    | expp LESSTHAN m_exp \n    | expp GREATHEREQUAL m_exp \n    | expp LESSEQUAL m_exp \n    | expp DIFFERENT m_exp \n    | expp SAME m_exp\n    \n    m_exp : termino\n    | m_exp PLUS termino\n    | m_exp MINUS termino\n    \n    termino : factor\n    | termino MULTIPLY factor\n    | termino DIVIDE factor \n    \n    factor : ID \n    | CTEINT guardarConstanteInt\n    | CTFLOAT guardarConstanteFloat\n    | CTECHAR guardarConstanteChar\n    | variable\n    | call_func\n    | PARENOPEN exp PARENCLOSE\n    \n    guardarConstanteInt : empty\n    \n    guardarConstanteFloat : empty\n    \n    guardarConstanteChar : empty\n    \n    variable : ID \n    | ID BRACEOPEN exp BRACECLOSE \n    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE\n    \n    variableAssignment : ID \n    | ID BRACEOPEN exp BRACECLOSE \n    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE\n    \n    condition : IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd\n        | IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse\n    \n    cuadruploIF : empty \n    \n    ifEnd : empty \n    \n    cuadruploElse : empty \n    \n    ifEndElse : empty \n    \n    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON\n    \n    writingg : exp\n    | exp COLON writingg\n    | auxString\n    | auxString COLON writingg\n    \n    auxString : CTESTRING\n       \n    \n    reading : READ multivariables SEMICOLON\n       \n    \n    multivariables : variable\n    | variable COLON multivariables\n       \n    \n    while_loop : WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd\n       \n    \n    whileMigaja : empty\n       \n    \n    whileEval : empty\n       \n    \n    whileEnd : empty\n       \n    \n    return : RETURN exp SEMICOLON\n       \n    \n    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON\n    \n    \n    max : MAX PARENOPEN ID PARENCLOSE SEMICOLON\n       \n    \n    min : MIN PARENOPEN ID PARENCLOSE SEMICOLON\n       \n    \n    sum : SUM PARENOPEN ID PARENCLOSE SEMICOLON\n       \n    \n    binomial : BINOMIAL PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON\n       \n    \n    poisson : POISSON PARENOPEN exp COLON exp PARENCLOSE SEMICOLON\n       \n    \n    uniforme : UNIFORME PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON\n       \n    \n    normal : NORMAL PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON\n       \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,2,3,],[-135,4,-5,]),'$end':([1,9,15,16,17,18,29,30,31,37,54,106,],[0,-135,-135,-135,-4,-9,-135,-2,-3,-1,-6,-38,]),'ID':([4,20,21,22,23,27,28,32,33,52,55,57,59,60,61,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,88,91,100,106,108,109,110,115,117,129,132,133,134,135,136,137,138,139,144,151,152,153,154,157,158,159,160,161,162,163,164,165,166,167,168,169,177,193,196,197,222,223,224,225,226,234,238,241,242,244,245,246,251,252,257,258,259,260,264,265,267,271,273,277,280,285,286,291,292,293,294,295,298,299,301,],[5,-135,-35,-36,-37,35,36,39,-13,39,89,103,-29,-30,-31,89,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,113,123,-135,-38,123,123,123,123,123,123,178,179,180,123,123,123,123,186,39,-119,113,123,123,-126,123,123,123,123,123,123,123,123,123,123,123,123,123,-68,123,123,123,123,123,123,-60,-113,-69,123,-127,-128,-129,-130,-59,186,39,-135,123,123,123,123,123,-107,-110,-135,-132,-122,-125,186,-135,-134,-133,-131,-108,-112,186,]),'SEMICOLON':([5,38,39,45,46,63,105,111,112,113,118,119,120,121,122,123,124,125,126,127,128,145,170,171,172,173,174,175,185,186,192,195,198,204,205,206,207,208,209,210,211,212,213,214,215,216,217,219,220,221,227,228,231,237,238,266,268,270,282,284,287,288,289,297,300,302,],[6,44,-135,-17,-20,-14,-18,151,-120,-101,157,-75,-78,-85,-88,-91,-135,-135,-135,-95,-96,193,-92,-98,-93,-99,-94,-100,226,-135,-15,234,-121,242,-76,-77,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,244,245,246,-64,-67,-19,-102,-69,280,-61,-16,-65,-103,293,294,295,-62,-66,-63,]),'VAR':([6,],[10,]),'MAIN':([6,7,8,11,14,19,24,44,51,106,229,230,254,255,256,],[12,12,12,-21,12,-10,-22,-12,-11,-38,-135,-135,-23,-34,-24,]),'FUNCTION':([6,7,11,19,44,51,106,229,230,254,255,256,],[13,13,13,-10,-12,-11,-38,-135,-135,-23,-34,-24,]),'INT':([10,13,44,49,50,55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,141,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[21,21,21,59,59,21,21,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,59,-119,-126,-68,21,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'FLOAT':([10,13,44,49,50,55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,141,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[22,22,22,60,60,22,22,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,60,-119,-126,-68,22,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'CHAR':([10,13,44,49,50,55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,141,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[23,23,23,61,61,23,23,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,61,-119,-126,-68,23,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'PARENOPEN':([12,25,26,35,36,41,42,43,86,87,89,90,91,92,93,94,95,96,97,98,99,108,109,110,114,115,116,117,123,129,130,131,135,136,137,138,153,154,158,159,160,161,162,163,164,165,166,167,168,169,177,196,197,222,223,224,225,241,259,260,264,265,267,],[-135,34,-7,-135,-135,49,-25,50,109,110,-135,117,129,-135,132,133,134,135,136,137,138,129,129,129,154,129,-70,129,-135,129,177,-123,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,]),'VOID':([13,],[28,]),'PARENCLOSE':([34,49,50,56,58,62,101,102,103,104,119,120,121,122,123,124,125,126,127,128,141,146,147,148,149,150,154,156,170,171,172,173,174,175,176,178,179,180,189,200,201,202,205,206,207,208,209,210,211,212,213,214,215,216,217,218,235,236,237,238,239,240,249,260,275,278,279,281,284,],[40,-135,-135,-135,-28,-135,140,-32,-26,142,-75,-78,-85,-88,-91,-135,-135,-135,-95,-96,-135,194,195,-114,-116,-118,-135,204,-92,-98,-93,-99,-94,-100,217,219,220,221,-27,238,-135,-73,-76,-77,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,243,-115,-117,-102,-69,-71,-74,266,-135,-72,287,288,289,-103,]),'COLON':([39,45,46,103,105,112,113,119,120,121,122,123,124,125,126,127,128,148,149,150,170,171,172,173,174,175,181,182,183,184,186,201,205,206,207,208,209,210,211,212,213,214,215,216,217,227,228,231,237,238,239,240,247,248,250,282,284,300,],[-135,52,-20,141,144,152,-101,-75,-78,-85,-88,-91,-135,-135,-135,-95,-96,196,197,-118,-92,-98,-93,-99,-94,-100,222,223,224,225,-135,-135,-76,-77,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,252,-67,257,-102,-69,260,-74,264,265,267,291,-103,301,]),'BRACEOPEN':([39,45,46,89,105,113,123,186,203,227,228,237,282,],[-135,53,-20,115,143,153,153,-135,241,253,-67,259,290,]),'BRACKETOPEN':([40,47,48,140,142,187,188,190,194,232,233,243,262,263,283,],[-135,55,-8,-135,-135,55,-33,55,-135,55,-109,-135,55,-124,55,]),'CTEINT':([53,91,108,109,110,115,117,129,135,136,137,138,143,153,154,158,159,160,161,162,163,164,165,166,167,168,169,177,196,197,222,223,224,225,241,253,259,260,264,265,267,290,],[64,124,124,124,124,124,124,124,124,124,124,124,191,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,269,124,124,124,124,124,296,]),'BRACKETCLOSE':([55,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,107,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[-135,106,-39,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-40,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'IF':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[86,86,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'PRINT':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[87,87,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'READ':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[88,88,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'PLOT':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[90,90,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'RETURN':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[91,91,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'WHILE':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[92,92,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'MAX':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[93,93,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'MIN':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[94,94,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'SUM':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[95,95,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'NORMAL':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[96,96,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'UNIFORME':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[97,97,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'POISSON':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[98,98,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'BINOMIAL':([55,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,106,151,157,193,226,234,238,242,244,245,246,251,258,271,273,277,280,285,286,292,293,294,295,298,299,],[99,99,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-38,-119,-126,-68,-60,-113,-69,-127,-128,-129,-130,-59,-135,-107,-110,-135,-132,-122,-125,-135,-134,-133,-131,-108,-112,]),'BRACECLOSE':([64,119,120,121,122,123,124,125,126,127,128,155,170,171,172,173,174,175,191,199,205,206,207,208,209,210,211,212,213,214,215,216,217,237,238,261,269,274,284,296,],[105,-75,-78,-85,-88,-91,-135,-135,-135,-95,-96,203,-92,-98,-93,-99,-94,-100,231,237,-76,-77,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,-102,-69,276,282,284,-103,300,]),'EQUAL':([85,89,203,276,],[108,-104,-105,-106,]),'CTFLOAT':([91,108,109,110,115,117,129,135,136,137,138,153,154,158,159,160,161,162,163,164,165,166,167,168,169,177,196,197,222,223,224,225,241,259,260,264,265,267,],[125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,]),'CTECHAR':([91,108,109,110,115,117,129,135,136,137,138,153,154,158,159,160,161,162,163,164,165,166,167,168,169,177,196,197,222,223,224,225,241,259,260,264,265,267,],[126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,]),'ELSE':([106,258,272,273,],[-38,-135,283,-111,]),'CTESTRING':([110,196,197,],[150,150,150,]),'AND':([118,119,120,121,122,123,124,125,126,127,128,145,146,148,155,156,170,171,172,173,174,175,176,181,182,183,184,199,201,205,206,207,208,209,210,211,212,213,214,215,216,217,218,237,238,247,248,249,250,261,274,278,279,281,284,],[158,-75,-78,-85,-88,-91,-135,-135,-135,-95,-96,158,158,158,158,158,-92,-98,-93,-99,-94,-100,158,158,158,158,158,158,158,-76,-77,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,158,-102,-69,158,158,158,158,158,158,158,158,158,-103,]),'OR':([118,119,120,121,122,123,124,125,126,127,128,145,146,148,155,156,170,171,172,173,174,175,176,181,182,183,184,199,201,205,206,207,208,209,210,211,212,213,214,215,216,217,218,237,238,247,248,249,250,261,274,278,279,281,284,],[159,-75,-78,-85,-88,-91,-135,-135,-135,-95,-96,159,159,159,159,159,-92,-98,-93,-99,-94,-100,159,159,159,159,159,159,159,-76,-77,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,159,-102,-69,159,159,159,159,159,159,159,159,159,-103,]),'GREATHERTHAN':([119,120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,205,206,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[160,-78,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,160,160,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,-102,-69,-103,]),'LESSTHAN':([119,120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,205,206,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[161,-78,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,161,161,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,-102,-69,-103,]),'GREATHEREQUAL':([119,120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,205,206,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[162,-78,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,162,162,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,-102,-69,-103,]),'LESSEQUAL':([119,120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,205,206,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[163,-78,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,163,163,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,-102,-69,-103,]),'DIFFERENT':([119,120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,205,206,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[164,-78,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,164,164,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,-102,-69,-103,]),'SAME':([119,120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,205,206,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[165,-78,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,165,165,-79,-80,-81,-82,-83,-84,-86,-87,-89,-90,-97,-102,-69,-103,]),'PLUS':([120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[166,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,166,166,166,166,166,166,-86,-87,-89,-90,-97,-102,-69,-103,]),'MINUS':([120,121,122,123,124,125,126,127,128,170,171,172,173,174,175,207,208,209,210,211,212,213,214,215,216,217,237,238,284,],[167,-85,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,167,167,167,167,167,167,-86,-87,-89,-90,-97,-102,-69,-103,]),'MULTIPLY':([121,122,123,124,125,126,127,128,170,171,172,173,174,175,213,214,215,216,217,237,238,284,],[168,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,168,168,-89,-90,-97,-102,-69,-103,]),'DIVIDE':([121,122,123,124,125,126,127,128,170,171,172,173,174,175,213,214,215,216,217,237,238,284,],[169,-88,-91,-135,-135,-135,-95,-96,-92,-98,-93,-99,-94,-100,169,169,-89,-90,-97,-102,-69,-103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start_program':([0,],[1,]),'cuadruploMain':([0,],[2,]),'empty':([0,9,12,15,16,20,29,35,36,39,40,49,50,55,56,62,66,89,92,100,123,124,125,126,140,141,142,154,186,194,201,229,230,243,258,260,277,292,],[3,18,26,18,18,33,18,42,42,46,48,58,58,67,102,102,67,116,131,33,116,171,173,175,188,58,188,202,228,233,240,255,255,263,273,202,286,299,]),'vars':([6,],[7,]),'multiple_funcs':([6,7,11,],[8,14,24,]),'main_body':([6,7,8,14,],[9,15,16,29,]),'dec_func':([6,7,11,],[11,11,11,]),'end':([9,15,16,29,],[17,30,31,37,]),'varss':([10,44,],[19,51,]),'type':([10,13,44,55,66,226,],[20,27,20,100,100,100,]),'crearTablaMain':([12,],[25,]),'guardarTipo':([20,100,],[32,139,]),'mvar':([32,52,144,257,],[38,63,192,270,]),'crearSymbolTable':([35,36,],[41,43,]),'guardarIDvar':([39,],[45,]),'gotoMain':([40,],[47,]),'body':([47,187,190,232,262,283,],[54,229,230,258,277,292,]),'param':([49,50,141,],[56,62,189,]),'typeParam':([49,50,141,],[57,57,57,]),'bodyy':([55,66,],[65,107,]),'statement':([55,66,],[66,66,]),'dec_variables':([55,66,],[68,68,]),'assignment':([55,66,],[69,69,]),'condition':([55,66,],[70,70,]),'writing':([55,66,],[71,71,]),'reading':([55,66,],[72,72,]),'call_func':([55,66,91,108,109,110,115,117,129,135,136,137,138,153,154,158,159,160,161,162,163,164,165,166,167,168,169,177,196,197,222,223,224,225,241,259,260,264,265,267,],[73,73,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,]),'graph':([55,66,],[74,74,]),'return':([55,66,],[75,75,]),'while_loop':([55,66,],[76,76,]),'max':([55,66,],[77,77,]),'min':([55,66,],[78,78,]),'sum':([55,66,],[79,79,]),'normal':([55,66,],[80,80,]),'uniforme':([55,66,],[81,81,]),'poisson':([55,66,],[82,82,]),'binomial':([55,66,],[83,83,]),'dec_variabless':([55,66,226,],[84,84,251,]),'variableAssignment':([55,66,],[85,85,]),'numeroParam':([56,62,],[101,104,]),'multivariables':([88,152,],[111,198,]),'variable':([88,91,108,109,110,115,117,129,135,136,137,138,152,153,154,158,159,160,161,162,163,164,165,166,167,168,169,177,196,197,222,223,224,225,241,259,260,264,265,267,],[112,127,127,127,127,127,127,127,127,127,127,127,112,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,]),'generarERA':([89,123,],[114,114,]),'exp':([91,108,109,110,115,117,129,135,136,137,138,153,154,177,196,197,222,223,224,225,241,259,260,264,265,267,],[118,145,146,148,155,156,176,181,182,183,184,199,201,218,148,148,247,248,249,250,261,274,201,278,279,281,]),'expp':([91,108,109,110,115,117,129,135,136,137,138,153,154,158,159,177,196,197,222,223,224,225,241,259,260,264,265,267,],[119,119,119,119,119,119,119,119,119,119,119,119,119,205,206,119,119,119,119,119,119,119,119,119,119,119,119,119,]),'m_exp':([91,108,109,110,115,117,129,135,136,137,138,153,154,158,159,160,161,162,163,164,165,177,196,197,222,223,224,225,241,259,260,264,265,267,],[120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,207,208,209,210,211,212,120,120,120,120,120,120,120,120,120,120,120,120,120,]),'termino':([91,108,109,110,115,117,129,135,136,137,138,153,154,158,159,160,161,162,163,164,165,166,167,177,196,197,222,223,224,225,241,259,260,264,265,267,],[121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,213,214,121,121,121,121,121,121,121,121,121,121,121,121,121,]),'factor':([91,108,109,110,115,117,129,135,136,137,138,153,154,158,159,160,161,162,163,164,165,166,167,168,169,177,196,197,222,223,224,225,241,259,260,264,265,267,],[122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,215,216,122,122,122,122,122,122,122,122,122,122,122,122,122,]),'whileMigaja':([92,],[130,]),'writingg':([110,196,197,],[147,235,236,]),'auxString':([110,196,197,],[149,149,149,]),'guardarConstanteInt':([124,],[170,]),'guardarConstanteFloat':([125,],[172,]),'guardarConstanteChar':([126,],[174,]),'dec_mvar':([139,252,291,301,],[185,268,297,302,]),'startFunc':([140,142,],[187,190,]),'call_funcc':([154,260,],[200,275,]),'guardarID':([186,],[227,]),'cuadruploIF':([194,],[232,]),'mandarParam':([201,],[239,]),'exitFunc':([229,230,],[254,256,]),'whileEval':([243,],[262,]),'ifEnd':([258,],[271,]),'cuadruploElse':([258,],[272,]),'whileEnd':([277,],[285,]),'ifEndElse':([292,],[298,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start_program","S'",1,None,None,None),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON vars multiple_funcs main_body end','start_program',8,'p_start_program','PLY.py',158),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON vars main_body end','start_program',7,'p_start_program','PLY.py',159),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON multiple_funcs main_body end','start_program',7,'p_start_program','PLY.py',160),
  ('start_program -> cuadruploMain PROGRAM ID SEMICOLON main_body end','start_program',6,'p_start_program','PLY.py',161),
  ('cuadruploMain -> empty','cuadruploMain',1,'p_cuadruploMain','PLY.py',183),
  ('main_body -> MAIN crearTablaMain PARENOPEN PARENCLOSE gotoMain body','main_body',6,'p_main_body','PLY.py',194),
  ('crearTablaMain -> empty','crearTablaMain',1,'p_crearTablaMain','PLY.py',199),
  ('gotoMain -> empty','gotoMain',1,'p_gotoMain','PLY.py',209),
  ('end -> empty','end',1,'p_end','PLY.py',228),
  ('vars -> VAR varss','vars',2,'p_vars','PLY.py',235),
  ('varss -> type guardarTipo mvar SEMICOLON varss','varss',5,'p_varss','PLY.py',241),
  ('varss -> type guardarTipo mvar SEMICOLON','varss',4,'p_varss','PLY.py',242),
  ('guardarTipo -> empty','guardarTipo',1,'p_guardarTipo','PLY.py',249),
  ('mvar -> ID guardarIDvar COLON mvar','mvar',4,'p_mvar','PLY.py',256),
  ('mvar -> ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',7,'p_mvar','PLY.py',257),
  ('mvar -> ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',10,'p_mvar','PLY.py',258),
  ('mvar -> ID guardarIDvar','mvar',2,'p_mvar','PLY.py',259),
  ('mvar -> ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE','mvar',5,'p_mvar','PLY.py',260),
  ('mvar -> ID guardarIDvar BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','mvar',8,'p_mvar','PLY.py',261),
  ('guardarIDvar -> empty','guardarIDvar',1,'p_guardarIDvar','PLY.py',267),
  ('multiple_funcs -> dec_func','multiple_funcs',1,'p_multiple_funcs','PLY.py',283),
  ('multiple_funcs -> dec_func multiple_funcs','multiple_funcs',2,'p_multiple_funcs','PLY.py',284),
  ('dec_func -> FUNCTION type ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc','dec_func',11,'p_dec_func','PLY.py',289),
  ('dec_func -> FUNCTION VOID ID crearSymbolTable PARENOPEN param numeroParam PARENCLOSE startFunc body exitFunc','dec_func',11,'p_dec_func','PLY.py',290),
  ('crearSymbolTable -> empty','crearSymbolTable',1,'p_crearSymbolTable','PLY.py',295),
  ('param -> typeParam ID','param',2,'p_param','PLY.py',312),
  ('param -> typeParam ID COLON param','param',4,'p_param','PLY.py',313),
  ('param -> empty','param',1,'p_param','PLY.py',314),
  ('typeParam -> INT','typeParam',1,'p_typeParam','PLY.py',338),
  ('typeParam -> FLOAT','typeParam',1,'p_typeParam','PLY.py',339),
  ('typeParam -> CHAR','typeParam',1,'p_typeParam','PLY.py',340),
  ('numeroParam -> empty','numeroParam',1,'p_numeroParam','PLY.py',349),
  ('startFunc -> empty','startFunc',1,'p_startFunc','PLY.py',360),
  ('exitFunc -> empty','exitFunc',1,'p_exitFunc','PLY.py',369),
  ('type -> INT','type',1,'p_type','PLY.py',395),
  ('type -> FLOAT','type',1,'p_type','PLY.py',396),
  ('type -> CHAR','type',1,'p_type','PLY.py',397),
  ('body -> BRACKETOPEN bodyy BRACKETCLOSE','body',3,'p_body','PLY.py',404),
  ('bodyy -> statement','bodyy',1,'p_bodyy','PLY.py',410),
  ('bodyy -> statement bodyy','bodyy',2,'p_bodyy','PLY.py',411),
  ('bodyy -> empty','bodyy',1,'p_bodyy','PLY.py',412),
  ('statement -> dec_variables','statement',1,'p_statement','PLY.py',418),
  ('statement -> assignment','statement',1,'p_statement','PLY.py',419),
  ('statement -> condition','statement',1,'p_statement','PLY.py',420),
  ('statement -> writing','statement',1,'p_statement','PLY.py',421),
  ('statement -> reading','statement',1,'p_statement','PLY.py',422),
  ('statement -> call_func','statement',1,'p_statement','PLY.py',423),
  ('statement -> graph','statement',1,'p_statement','PLY.py',424),
  ('statement -> return','statement',1,'p_statement','PLY.py',425),
  ('statement -> while_loop','statement',1,'p_statement','PLY.py',426),
  ('statement -> max','statement',1,'p_statement','PLY.py',427),
  ('statement -> min','statement',1,'p_statement','PLY.py',428),
  ('statement -> sum','statement',1,'p_statement','PLY.py',429),
  ('statement -> normal','statement',1,'p_statement','PLY.py',430),
  ('statement -> uniforme','statement',1,'p_statement','PLY.py',431),
  ('statement -> poisson','statement',1,'p_statement','PLY.py',432),
  ('statement -> binomial','statement',1,'p_statement','PLY.py',433),
  ('dec_variables -> dec_variabless','dec_variables',1,'p_dec_variables','PLY.py',438),
  ('dec_variabless -> type guardarTipo dec_mvar SEMICOLON dec_variabless','dec_variabless',5,'p_dec_variabless','PLY.py',443),
  ('dec_variabless -> type guardarTipo dec_mvar SEMICOLON','dec_variabless',4,'p_dec_variabless','PLY.py',444),
  ('dec_mvar -> ID guardarID COLON dec_mvar','dec_mvar',4,'p_dec_mvar','PLY.py',451),
  ('dec_mvar -> ID guardarID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',7,'p_dec_mvar','PLY.py',452),
  ('dec_mvar -> ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',10,'p_dec_mvar','PLY.py',453),
  ('dec_mvar -> ID guardarID','dec_mvar',2,'p_dec_mvar','PLY.py',454),
  ('dec_mvar -> ID guardarID BRACEOPEN CTEINT BRACECLOSE','dec_mvar',5,'p_dec_mvar','PLY.py',455),
  ('dec_mvar -> ID guardarID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','dec_mvar',8,'p_dec_mvar','PLY.py',456),
  ('guardarID -> empty','guardarID',1,'p_guardarID','PLY.py',461),
  ('assignment -> variableAssignment EQUAL exp SEMICOLON','assignment',4,'p_assignment','PLY.py',482),
  ('call_func -> ID generarERA PARENOPEN call_funcc PARENCLOSE','call_func',5,'p_call_func','PLY.py',576),
  ('generarERA -> empty','generarERA',1,'p_generarERA','PLY.py',595),
  ('call_funcc -> exp mandarParam','call_funcc',2,'p_call_funcc','PLY.py',608),
  ('call_funcc -> exp mandarParam COLON call_funcc','call_funcc',4,'p_call_funcc','PLY.py',609),
  ('call_funcc -> empty','call_funcc',1,'p_call_funcc','PLY.py',610),
  ('mandarParam -> empty','mandarParam',1,'p_mandarParam','PLY.py',615),
  ('exp -> expp','exp',1,'p_exp','PLY.py',669),
  ('exp -> exp AND expp','exp',3,'p_exp','PLY.py',670),
  ('exp -> exp OR expp','exp',3,'p_exp','PLY.py',671),
  ('expp -> m_exp','expp',1,'p_expp','PLY.py',782),
  ('expp -> expp GREATHERTHAN m_exp','expp',3,'p_expp','PLY.py',783),
  ('expp -> expp LESSTHAN m_exp','expp',3,'p_expp','PLY.py',784),
  ('expp -> expp GREATHEREQUAL m_exp','expp',3,'p_expp','PLY.py',785),
  ('expp -> expp LESSEQUAL m_exp','expp',3,'p_expp','PLY.py',786),
  ('expp -> expp DIFFERENT m_exp','expp',3,'p_expp','PLY.py',787),
  ('expp -> expp SAME m_exp','expp',3,'p_expp','PLY.py',788),
  ('m_exp -> termino','m_exp',1,'p_m_exp','PLY.py',901),
  ('m_exp -> m_exp PLUS termino','m_exp',3,'p_m_exp','PLY.py',902),
  ('m_exp -> m_exp MINUS termino','m_exp',3,'p_m_exp','PLY.py',903),
  ('termino -> factor','termino',1,'p_termino','PLY.py',1015),
  ('termino -> termino MULTIPLY factor','termino',3,'p_termino','PLY.py',1016),
  ('termino -> termino DIVIDE factor','termino',3,'p_termino','PLY.py',1017),
  ('factor -> ID','factor',1,'p_factor','PLY.py',1127),
  ('factor -> CTEINT guardarConstanteInt','factor',2,'p_factor','PLY.py',1128),
  ('factor -> CTFLOAT guardarConstanteFloat','factor',2,'p_factor','PLY.py',1129),
  ('factor -> CTECHAR guardarConstanteChar','factor',2,'p_factor','PLY.py',1130),
  ('factor -> variable','factor',1,'p_factor','PLY.py',1131),
  ('factor -> call_func','factor',1,'p_factor','PLY.py',1132),
  ('factor -> PARENOPEN exp PARENCLOSE','factor',3,'p_factor','PLY.py',1133),
  ('guardarConstanteInt -> empty','guardarConstanteInt',1,'p_guardarConstanteInt','PLY.py',1262),
  ('guardarConstanteFloat -> empty','guardarConstanteFloat',1,'p_guardarConstanteFloat','PLY.py',1272),
  ('guardarConstanteChar -> empty','guardarConstanteChar',1,'p_guardarConstanteChar','PLY.py',1282),
  ('variable -> ID','variable',1,'p_variable','PLY.py',1292),
  ('variable -> ID BRACEOPEN exp BRACECLOSE','variable',4,'p_variable','PLY.py',1293),
  ('variable -> ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE','variable',7,'p_variable','PLY.py',1294),
  ('variableAssignment -> ID','variableAssignment',1,'p_variableAssignment','PLY.py',1302),
  ('variableAssignment -> ID BRACEOPEN exp BRACECLOSE','variableAssignment',4,'p_variableAssignment','PLY.py',1303),
  ('variableAssignment -> ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE','variableAssignment',7,'p_variableAssignment','PLY.py',1304),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd','condition',7,'p_condition','PLY.py',1423),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse','condition',10,'p_condition','PLY.py',1424),
  ('cuadruploIF -> empty','cuadruploIF',1,'p_cuadruploIF','PLY.py',1429),
  ('ifEnd -> empty','ifEnd',1,'p_ifEnd','PLY.py',1449),
  ('cuadruploElse -> empty','cuadruploElse',1,'p_cuadruploElse','PLY.py',1468),
  ('ifEndElse -> empty','ifEndElse',1,'p_ifEndElse','PLY.py',1495),
  ('writing -> PRINT PARENOPEN writingg PARENCLOSE SEMICOLON','writing',5,'p_writing','PLY.py',1509),
  ('writingg -> exp','writingg',1,'p_writingg','PLY.py',1515),
  ('writingg -> exp COLON writingg','writingg',3,'p_writingg','PLY.py',1516),
  ('writingg -> auxString','writingg',1,'p_writingg','PLY.py',1517),
  ('writingg -> auxString COLON writingg','writingg',3,'p_writingg','PLY.py',1518),
  ('auxString -> CTESTRING','auxString',1,'p_auxString','PLY.py',1528),
  ('reading -> READ multivariables SEMICOLON','reading',3,'p_reading','PLY.py',1541),
  ('multivariables -> variable','multivariables',1,'p_multivariables','PLY.py',1547),
  ('multivariables -> variable COLON multivariables','multivariables',3,'p_multivariables','PLY.py',1548),
  ('while_loop -> WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd','while_loop',8,'p_while_loop','PLY.py',1570),
  ('whileMigaja -> empty','whileMigaja',1,'p_whileMigaja','PLY.py',1576),
  ('whileEval -> empty','whileEval',1,'p_whileEval','PLY.py',1585),
  ('whileEnd -> empty','whileEnd',1,'p_whileEnd','PLY.py',1605),
  ('return -> RETURN exp SEMICOLON','return',3,'p_return','PLY.py',1634),
  ('graph -> PLOT PARENOPEN exp PARENCLOSE SEMICOLON','graph',5,'p_graph','PLY.py',1647),
  ('max -> MAX PARENOPEN ID PARENCLOSE SEMICOLON','max',5,'p_max','PLY.py',1657),
  ('min -> MIN PARENOPEN ID PARENCLOSE SEMICOLON','min',5,'p_min','PLY.py',1676),
  ('sum -> SUM PARENOPEN ID PARENCLOSE SEMICOLON','sum',5,'p_sum','PLY.py',1695),
  ('binomial -> BINOMIAL PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON','binomial',9,'p_binomial','PLY.py',1713),
  ('poisson -> POISSON PARENOPEN exp COLON exp PARENCLOSE SEMICOLON','poisson',7,'p_poisson','PLY.py',1753),
  ('uniforme -> UNIFORME PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON','uniforme',9,'p_uniforme','PLY.py',1783),
  ('normal -> NORMAL PARENOPEN exp COLON exp COLON exp PARENCLOSE SEMICOLON','normal',9,'p_normal','PLY.py',1823),
  ('empty -> <empty>','empty',0,'p_empty','PLY.py',1864),
]
