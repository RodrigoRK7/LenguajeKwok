
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BINOMIAL BRACECLOSE BRACEOPEN BRACKETCLOSE BRACKETOPEN CHAR COLON CTEINT CTESTRING CTFLOAT DIFFERENT DIVIDE ELSE EQUAL FLOAT FOR FUNCTION GREATHEREQUAL GREATHERTHAN ID IF INT LESSEQUAL LESSTHAN MAIN MAX MIN MINUS MULTIPLY NORMAL OR PARENCLOSE PARENOPEN PLOT PLUS POISSON PRINT PROGRAM READ RETURN SAME SEMICOLON SUM UNIFORME VAR VOID WHILE\n    start_program : PROGRAM ID SEMICOLON vars multiple_funcs main_body\n    | PROGRAM ID SEMICOLON vars main_body\n    | PROGRAM ID SEMICOLON multiple_funcs main_body\n    | PROGRAM ID SEMICOLON main_body\n    \n    multiple_funcs : dec_func \n    | dec_func multiple_funcs\n    \n    main_body : MAIN body\n    \n    vars : VAR varss\n    \n    varss : type mvar SEMICOLON varss\n    | type mvar SEMICOLON\n    \n    mvar : ID COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    dec_func : FUNCTION type ID PARENOPEN param PARENCLOSE body\n    | FUNCTION VOID ID PARENOPEN param PARENCLOSE body\n    \n    param : type variable\n    | type variable COLON param\n    | empty\n    \n    type : INT\n    | FLOAT\n    | CHAR\n    \n    body : BRACKETOPEN bodyy BRACKETCLOSE\n    \n    bodyy : statement \n    | statement bodyy\n    | empty\n    \n    statement : dec_variables \n    | assignment\n    | condition\n    | writing\n    | reading\n    | call_func\n    | graph\n    | return\n    | while_loop\n    | for_loop\n    | max\n    | min\n    | sum\n    | normal\n    | uniforme\n    | poisson\n    | binomial\n    \n    dec_variables : dec_variabless\n    \n    dec_variabless : type dec_mvar SEMICOLON dec_variabless\n    | type dec_mvar SEMICOLON\n    \n    dec_mvar : ID COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    assignment : variable EQUAL exp SEMICOLON\n    \n    call_func : ID PARENOPEN call_funcc PARENCLOSE\n    \n    call_funcc : exp \n    | exp COLON call_funcc\n    | empty\n    \n    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON\n    \n    \n    exp : exp GREATHERTHAN exp \n    | exp LESSTHAN exp \n    | exp GREATHEREQUAL exp \n    | exp LESSEQUAL exp \n    | exp DIFFERENT exp \n    | exp SAME exp\n    | exp AND exp\n    | exp OR exp\n    | m_exp\n    \n    m_exp : t m_expp \n    \n    m_expp : PLUS appendPLUS m_exp\n        | MINUS appendMINUS m_exp\n        | empty\n    \n    appendPLUS : empty\n    \n    appendMINUS : empty\n    \n    appendMULTIPLY : empty\n    \n    appendDIVIDE : empty\n    \n    t : f termino\n    \n    termino : MULTIPLY appendMULTIPLY t \n        | DIVIDE appendDIVIDE t \n        | empty\n    \n    f : PARENOPEN exp PARENCLOSE \n    | ID\n    | CTEINT\n    | CTFLOAT \n    | variable\n    | call_func\n    \n    variable : ID \n    | ID BRACEOPEN exp BRACECLOSE \n    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE\n    \n    condition : IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd\n        | IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse\n    \n    cuadruploIF : empty \n    \n    cuadruploElse : empty \n    \n    ifEnd : empty \n    \n    ifEndElse : empty \n    \n    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON\n    \n    writingg : exp\n    | exp COLON writingg\n    | auxString\n    | auxString COLON writingg\n    \n    auxString : CTESTRING\n       \n    \n    reading : READ multivariables SEMICOLON\n       \n    \n    multivariables : variable\n    | variable COLON multivariables\n       \n    \n    while_loop : WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd\n       \n    \n    whileMigaja : empty\n       \n    \n    whileEval : empty\n       \n    \n    whileEnd : empty\n       \n    \n    for_loop : FOR PARENOPEN for_assignment SEMICOLON exp SEMICOLON for_assignment PARENCLOSE body\n       \n    \n    for_assignment : variable EQUAL exp\n       \n    \n    return : RETURN exp SEMICOLON\n       \n    \n    max : MAX PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    min : MIN PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    sum : SUM PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    param_dist : variable\n    | variable COLON param_dist\n       \n    \n    binomial : BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    poisson : POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    uniforme : UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    normal : NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,13,14,21,25,71,],[0,-4,-2,-3,-7,-1,-25,]),'ID':([2,16,17,18,19,22,23,24,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,55,65,69,71,73,74,75,79,80,81,86,94,95,96,97,98,99,100,101,115,116,122,123,124,125,126,127,128,129,130,132,133,136,137,140,151,152,154,159,162,163,165,166,177,178,179,180,181,182,183,184,187,188,193,197,204,207,211,212,220,221,222,223,225,226,227,234,238,240,243,245,247,251,253,254,258,259,260,261,262,],[3,27,-22,-23,-24,53,66,67,53,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,78,87,103,27,-25,87,87,87,87,87,87,87,78,87,87,87,78,78,78,78,-103,78,-112,87,87,87,87,87,87,87,87,-122,-122,-122,-122,87,-48,103,78,-55,87,87,-56,87,87,-74,87,-75,87,-76,87,-77,87,87,78,-47,27,-97,87,-60,-113,-114,-115,-121,-120,-119,-118,-122,78,103,-91,-95,-122,27,-106,-109,-122,-110,103,-92,-96,]),'SEMICOLON':([3,26,27,76,77,78,82,83,84,85,87,88,89,90,91,102,103,107,109,131,134,135,138,141,158,161,164,165,167,168,169,170,171,172,173,174,175,176,185,189,190,191,192,194,195,196,198,213,214,215,216,218,219,228,233,242,246,250,256,257,263,],[4,68,-14,115,-104,-88,122,-69,-122,-122,-83,-84,-85,-86,-87,151,-52,-11,159,-70,-73,-78,-81,187,-15,207,-105,-56,-89,212,-61,-62,-63,-64,-65,-66,-67,-68,-82,220,221,222,223,225,226,227,-49,-71,-72,-79,-80,238,-111,-53,-12,-16,-90,-50,-54,-13,-51,]),'VAR':([4,],[8,]),'MAIN':([4,5,6,9,12,15,20,68,71,106,230,231,],[10,10,10,-5,10,-8,-6,-10,-25,-9,-17,-18,]),'FUNCTION':([4,5,9,15,68,71,106,230,231,],[11,11,11,-8,-10,-25,-9,-17,-18,]),'INT':([8,11,22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,68,71,104,105,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,229,234,243,245,247,253,254,258,259,261,262,],[17,17,17,17,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,17,-25,17,17,-103,-112,17,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,17,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'FLOAT':([8,11,22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,68,71,104,105,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,229,234,243,245,247,253,254,258,259,261,262,],[18,18,18,18,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,18,-25,18,18,-103,-112,18,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,18,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'CHAR':([8,11,22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,68,71,104,105,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,229,234,243,245,247,253,254,258,259,261,262,],[19,19,19,19,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,19,-25,19,19,-103,-112,19,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,19,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'BRACKETOPEN':([10,160,201,202,205,206,217,236,237,252,255,],[22,-122,22,22,22,-93,-122,22,-108,22,22,]),'VOID':([11,],[24,]),'BRACKETCLOSE':([22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,72,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[-122,71,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-27,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'IF':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[50,50,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'PRINT':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[51,51,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'READ':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[52,52,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'PLOT':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[54,54,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'RETURN':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[55,55,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'WHILE':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[56,56,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'FOR':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[57,57,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'MAX':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[58,58,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'MIN':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[59,59,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'SUM':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[60,60,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'NORMAL':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[61,61,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'UNIFORME':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[62,62,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'POISSON':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[63,63,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'BINOMIAL':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,115,122,151,159,165,197,207,212,220,221,222,223,225,226,227,234,243,245,247,253,254,258,259,261,262,],[64,64,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-103,-112,-48,-55,-56,-47,-97,-60,-113,-114,-115,-121,-120,-119,-118,-122,-91,-95,-122,-106,-109,-122,-110,-92,-96,]),'COLON':([27,77,78,83,84,85,87,88,89,90,91,103,112,113,114,118,131,134,135,138,147,158,165,167,169,170,171,172,173,174,175,176,185,200,213,214,215,216,228,242,246,256,],[69,116,-88,-69,-122,-122,-83,-84,-85,-86,-87,152,162,163,-102,166,-70,-73,-78,-81,193,204,-56,-89,-61,-62,-63,-64,-65,-66,-67,-68,-82,229,-71,-72,-79,-80,240,251,-90,260,]),'BRACEOPEN':([27,53,78,87,103,158,167,228,],[70,80,80,80,153,203,211,239,]),'EQUAL':([49,53,78,142,167,246,],[73,-88,-88,188,-89,-90,]),'PARENOPEN':([50,51,53,54,55,56,57,58,59,60,61,62,63,64,66,67,73,74,75,79,80,81,86,87,92,93,95,96,97,123,124,125,126,127,128,129,130,132,133,136,137,140,162,163,166,177,178,179,180,181,182,183,184,187,188,211,],[74,75,79,81,86,-122,94,95,96,97,98,99,100,101,104,105,86,86,86,86,86,86,86,79,140,-107,86,86,86,86,86,86,86,86,86,86,86,-122,-122,-122,-122,86,86,86,86,86,-74,86,-75,86,-76,86,-77,86,86,86,]),'CTEINT':([55,70,73,74,75,79,80,81,86,95,96,97,123,124,125,126,127,128,129,130,132,133,136,137,140,153,162,163,166,177,178,179,180,181,182,183,184,187,188,203,211,239,],[88,108,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,-122,-122,-122,-122,88,199,88,88,88,88,-74,88,-75,88,-76,88,-77,88,88,232,88,249,]),'CTFLOAT':([55,73,74,75,79,80,81,86,95,96,97,123,124,125,126,127,128,129,130,132,133,136,137,140,162,163,166,177,178,179,180,181,182,183,184,187,188,211,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,-122,-122,-122,-122,89,89,89,89,89,-74,89,-75,89,-76,89,-77,89,89,89,]),'ELSE':([71,234,244,245,],[-25,-122,252,-94,]),'CTESTRING':([75,162,163,],[114,114,114,]),'PARENCLOSE':([78,79,83,84,85,87,88,89,90,91,104,105,110,111,112,113,114,117,118,119,121,131,134,135,138,139,143,144,145,146,147,148,149,150,155,156,157,165,166,167,169,170,171,172,173,174,175,176,185,186,200,208,209,210,213,214,215,216,219,224,229,241,246,248,],[-88,-122,-69,-122,-122,-83,-84,-85,-86,-87,-122,-122,160,161,-98,-100,-102,165,-57,-59,168,-70,-73,-78,-81,185,189,190,191,192,-116,194,195,196,201,-21,202,-56,-122,-89,-61,-62,-63,-64,-65,-66,-67,-68,-82,217,-19,-99,-101,-58,-71,-72,-79,-80,-111,-117,-122,-20,-90,255,]),'GREATHERTHAN':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[123,-69,-122,-122,-83,-84,-85,-86,-87,123,123,123,123,123,123,-70,-73,-78,-81,123,123,123,123,-56,-89,123,123,123,123,123,123,123,123,-82,123,-71,-72,-79,-80,123,123,123,-90,]),'LESSTHAN':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[124,-69,-122,-122,-83,-84,-85,-86,-87,124,124,124,124,124,124,-70,-73,-78,-81,124,124,124,124,-56,-89,124,124,124,124,124,124,124,124,-82,124,-71,-72,-79,-80,124,124,124,-90,]),'GREATHEREQUAL':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[125,-69,-122,-122,-83,-84,-85,-86,-87,125,125,125,125,125,125,-70,-73,-78,-81,125,125,125,125,-56,-89,125,125,125,125,125,125,125,125,-82,125,-71,-72,-79,-80,125,125,125,-90,]),'LESSEQUAL':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[126,-69,-122,-122,-83,-84,-85,-86,-87,126,126,126,126,126,126,-70,-73,-78,-81,126,126,126,126,-56,-89,126,126,126,126,126,126,126,126,-82,126,-71,-72,-79,-80,126,126,126,-90,]),'DIFFERENT':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[127,-69,-122,-122,-83,-84,-85,-86,-87,127,127,127,127,127,127,-70,-73,-78,-81,127,127,127,127,-56,-89,127,127,127,127,127,127,127,127,-82,127,-71,-72,-79,-80,127,127,127,-90,]),'SAME':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[128,-69,-122,-122,-83,-84,-85,-86,-87,128,128,128,128,128,128,-70,-73,-78,-81,128,128,128,128,-56,-89,128,128,128,128,128,128,128,128,-82,128,-71,-72,-79,-80,128,128,128,-90,]),'AND':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[129,-69,-122,-122,-83,-84,-85,-86,-87,129,129,129,129,129,129,-70,-73,-78,-81,129,129,129,129,-56,-89,129,129,129,129,129,129,129,129,-82,129,-71,-72,-79,-80,129,129,129,-90,]),'OR':([82,83,84,85,87,88,89,90,91,109,110,112,118,120,121,131,134,135,138,139,143,144,145,165,167,169,170,171,172,173,174,175,176,185,186,213,214,215,216,218,219,235,246,],[130,-69,-122,-122,-83,-84,-85,-86,-87,130,130,130,130,130,130,-70,-73,-78,-81,130,130,130,130,-56,-89,130,130,130,130,130,130,130,130,-82,130,-71,-72,-79,-80,130,130,130,-90,]),'BRACECLOSE':([83,84,85,87,88,89,90,91,108,120,131,134,135,138,165,167,169,170,171,172,173,174,175,176,185,199,213,214,215,216,232,235,246,249,],[-69,-122,-122,-83,-84,-85,-86,-87,158,167,-70,-73,-78,-81,-56,-89,-61,-62,-63,-64,-65,-66,-67,-68,-82,228,-71,-72,-79,-80,242,246,-90,256,]),'PLUS':([84,85,87,88,89,90,91,135,138,165,167,185,215,216,246,],[132,-122,-83,-84,-85,-86,-87,-78,-81,-56,-89,-82,-79,-80,-90,]),'MINUS':([84,85,87,88,89,90,91,135,138,165,167,185,215,216,246,],[133,-122,-83,-84,-85,-86,-87,-78,-81,-56,-89,-82,-79,-80,-90,]),'MULTIPLY':([85,87,88,89,90,91,165,167,185,246,],[136,-83,-84,-85,-86,-87,-56,-89,-82,-90,]),'DIVIDE':([85,87,88,89,90,91,165,167,185,246,],[137,-83,-84,-85,-86,-87,-56,-89,-82,-90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start_program':([0,],[1,]),'vars':([4,],[5,]),'multiple_funcs':([4,5,9,],[6,12,20,]),'main_body':([4,5,6,12,],[7,13,14,25,]),'dec_func':([4,5,9,],[9,9,9,]),'varss':([8,68,],[15,106,]),'type':([8,11,22,29,68,104,105,151,229,],[16,23,65,65,16,154,154,65,154,]),'body':([10,201,202,205,236,252,255,],[21,230,231,234,247,258,259,]),'mvar':([16,69,204,251,],[26,107,233,257,]),'bodyy':([22,29,],[28,72,]),'statement':([22,29,],[29,29,]),'empty':([22,29,56,79,84,85,104,105,132,133,136,137,160,166,217,229,234,247,258,],[30,30,93,119,134,138,156,156,178,180,182,184,206,119,237,156,245,254,262,]),'dec_variables':([22,29,],[31,31,]),'assignment':([22,29,],[32,32,]),'condition':([22,29,],[33,33,]),'writing':([22,29,],[34,34,]),'reading':([22,29,],[35,35,]),'call_func':([22,29,55,73,74,75,79,80,81,86,95,96,97,123,124,125,126,127,128,129,130,140,162,163,166,177,179,181,183,187,188,211,],[36,36,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'graph':([22,29,],[37,37,]),'return':([22,29,],[38,38,]),'while_loop':([22,29,],[39,39,]),'for_loop':([22,29,],[40,40,]),'max':([22,29,],[41,41,]),'min':([22,29,],[42,42,]),'sum':([22,29,],[43,43,]),'normal':([22,29,],[44,44,]),'uniforme':([22,29,],[45,45,]),'poisson':([22,29,],[46,46,]),'binomial':([22,29,],[47,47,]),'dec_variabless':([22,29,151,],[48,48,197,]),'variable':([22,29,52,55,73,74,75,79,80,81,86,94,95,96,97,98,99,100,101,116,123,124,125,126,127,128,129,130,140,154,162,163,166,177,179,181,183,187,188,193,211,238,],[49,49,77,90,90,90,90,90,90,90,90,142,90,90,90,147,147,147,147,77,90,90,90,90,90,90,90,90,90,200,90,90,90,90,90,90,90,90,90,147,90,142,]),'multivariables':([52,116,],[76,164,]),'exp':([55,73,74,75,79,80,81,86,95,96,97,123,124,125,126,127,128,129,130,140,162,163,166,187,188,211,],[82,109,110,112,118,120,121,139,143,144,145,169,170,171,172,173,174,175,176,186,112,112,118,218,219,235,]),'m_exp':([55,73,74,75,79,80,81,86,95,96,97,123,124,125,126,127,128,129,130,140,162,163,166,177,179,187,188,211,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,213,214,83,83,83,]),'t':([55,73,74,75,79,80,81,86,95,96,97,123,124,125,126,127,128,129,130,140,162,163,166,177,179,181,183,187,188,211,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,215,216,84,84,84,]),'f':([55,73,74,75,79,80,81,86,95,96,97,123,124,125,126,127,128,129,130,140,162,163,166,177,179,181,183,187,188,211,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'whileMigaja':([56,],[92,]),'dec_mvar':([65,152,240,260,],[102,198,250,263,]),'writingg':([75,162,163,],[111,208,209,]),'auxString':([75,162,163,],[113,113,113,]),'call_funcc':([79,166,],[117,210,]),'m_expp':([84,],[131,]),'termino':([85,],[135,]),'for_assignment':([94,238,],[141,248,]),'param_dist':([98,99,100,101,193,],[146,148,149,150,224,]),'param':([104,105,229,],[155,157,241,]),'appendPLUS':([132,],[177,]),'appendMINUS':([133,],[179,]),'appendMULTIPLY':([136,],[181,]),'appendDIVIDE':([137,],[183,]),'cuadruploIF':([160,],[205,]),'whileEval':([217,],[236,]),'ifEnd':([234,],[243,]),'cuadruploElse':([234,],[244,]),'whileEnd':([247,],[253,]),'ifEndElse':([258,],[261,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start_program","S'",1,None,None,None),
  ('start_program -> PROGRAM ID SEMICOLON vars multiple_funcs main_body','start_program',6,'p_start_program','PLY.py',107),
  ('start_program -> PROGRAM ID SEMICOLON vars main_body','start_program',5,'p_start_program','PLY.py',108),
  ('start_program -> PROGRAM ID SEMICOLON multiple_funcs main_body','start_program',5,'p_start_program','PLY.py',109),
  ('start_program -> PROGRAM ID SEMICOLON main_body','start_program',4,'p_start_program','PLY.py',110),
  ('multiple_funcs -> dec_func','multiple_funcs',1,'p_multiple_funcs','PLY.py',126),
  ('multiple_funcs -> dec_func multiple_funcs','multiple_funcs',2,'p_multiple_funcs','PLY.py',127),
  ('main_body -> MAIN body','main_body',2,'p_main_body','PLY.py',131),
  ('vars -> VAR varss','vars',2,'p_vars','PLY.py',136),
  ('varss -> type mvar SEMICOLON varss','varss',4,'p_varss','PLY.py',142),
  ('varss -> type mvar SEMICOLON','varss',3,'p_varss','PLY.py',143),
  ('mvar -> ID COLON mvar','mvar',3,'p_mvar','PLY.py',152),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',6,'p_mvar','PLY.py',153),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',9,'p_mvar','PLY.py',154),
  ('mvar -> ID','mvar',1,'p_mvar','PLY.py',155),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE','mvar',4,'p_mvar','PLY.py',156),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','mvar',7,'p_mvar','PLY.py',157),
  ('dec_func -> FUNCTION type ID PARENOPEN param PARENCLOSE body','dec_func',7,'p_dec_func','PLY.py',165),
  ('dec_func -> FUNCTION VOID ID PARENOPEN param PARENCLOSE body','dec_func',7,'p_dec_func','PLY.py',166),
  ('param -> type variable','param',2,'p_param','PLY.py',177),
  ('param -> type variable COLON param','param',4,'p_param','PLY.py',178),
  ('param -> empty','param',1,'p_param','PLY.py',179),
  ('type -> INT','type',1,'p_type','PLY.py',186),
  ('type -> FLOAT','type',1,'p_type','PLY.py',187),
  ('type -> CHAR','type',1,'p_type','PLY.py',188),
  ('body -> BRACKETOPEN bodyy BRACKETCLOSE','body',3,'p_body','PLY.py',194),
  ('bodyy -> statement','bodyy',1,'p_bodyy','PLY.py',199),
  ('bodyy -> statement bodyy','bodyy',2,'p_bodyy','PLY.py',200),
  ('bodyy -> empty','bodyy',1,'p_bodyy','PLY.py',201),
  ('statement -> dec_variables','statement',1,'p_statement','PLY.py',206),
  ('statement -> assignment','statement',1,'p_statement','PLY.py',207),
  ('statement -> condition','statement',1,'p_statement','PLY.py',208),
  ('statement -> writing','statement',1,'p_statement','PLY.py',209),
  ('statement -> reading','statement',1,'p_statement','PLY.py',210),
  ('statement -> call_func','statement',1,'p_statement','PLY.py',211),
  ('statement -> graph','statement',1,'p_statement','PLY.py',212),
  ('statement -> return','statement',1,'p_statement','PLY.py',213),
  ('statement -> while_loop','statement',1,'p_statement','PLY.py',214),
  ('statement -> for_loop','statement',1,'p_statement','PLY.py',215),
  ('statement -> max','statement',1,'p_statement','PLY.py',216),
  ('statement -> min','statement',1,'p_statement','PLY.py',217),
  ('statement -> sum','statement',1,'p_statement','PLY.py',218),
  ('statement -> normal','statement',1,'p_statement','PLY.py',219),
  ('statement -> uniforme','statement',1,'p_statement','PLY.py',220),
  ('statement -> poisson','statement',1,'p_statement','PLY.py',221),
  ('statement -> binomial','statement',1,'p_statement','PLY.py',222),
  ('dec_variables -> dec_variabless','dec_variables',1,'p_dec_variables','PLY.py',226),
  ('dec_variabless -> type dec_mvar SEMICOLON dec_variabless','dec_variabless',4,'p_dec_variabless','PLY.py',232),
  ('dec_variabless -> type dec_mvar SEMICOLON','dec_variabless',3,'p_dec_variabless','PLY.py',233),
  ('dec_mvar -> ID COLON dec_mvar','dec_mvar',3,'p_dec_mvar','PLY.py',241),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',6,'p_dec_mvar','PLY.py',242),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',9,'p_dec_mvar','PLY.py',243),
  ('dec_mvar -> ID','dec_mvar',1,'p_dec_mvar','PLY.py',244),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE','dec_mvar',4,'p_dec_mvar','PLY.py',245),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','dec_mvar',7,'p_dec_mvar','PLY.py',246),
  ('assignment -> variable EQUAL exp SEMICOLON','assignment',4,'p_assignment','PLY.py',255),
  ('call_func -> ID PARENOPEN call_funcc PARENCLOSE','call_func',4,'p_call_func','PLY.py',272),
  ('call_funcc -> exp','call_funcc',1,'p_call_funcc','PLY.py',276),
  ('call_funcc -> exp COLON call_funcc','call_funcc',3,'p_call_funcc','PLY.py',277),
  ('call_funcc -> empty','call_funcc',1,'p_call_funcc','PLY.py',278),
  ('graph -> PLOT PARENOPEN exp PARENCLOSE SEMICOLON','graph',5,'p_graph','PLY.py',282),
  ('exp -> exp GREATHERTHAN exp','exp',3,'p_exp','PLY.py',287),
  ('exp -> exp LESSTHAN exp','exp',3,'p_exp','PLY.py',288),
  ('exp -> exp GREATHEREQUAL exp','exp',3,'p_exp','PLY.py',289),
  ('exp -> exp LESSEQUAL exp','exp',3,'p_exp','PLY.py',290),
  ('exp -> exp DIFFERENT exp','exp',3,'p_exp','PLY.py',291),
  ('exp -> exp SAME exp','exp',3,'p_exp','PLY.py',292),
  ('exp -> exp AND exp','exp',3,'p_exp','PLY.py',293),
  ('exp -> exp OR exp','exp',3,'p_exp','PLY.py',294),
  ('exp -> m_exp','exp',1,'p_exp','PLY.py',295),
  ('m_exp -> t m_expp','m_exp',2,'p_m_exp','PLY.py',315),
  ('m_expp -> PLUS appendPLUS m_exp','m_expp',3,'p_m_expp','PLY.py',326),
  ('m_expp -> MINUS appendMINUS m_exp','m_expp',3,'p_m_expp','PLY.py',327),
  ('m_expp -> empty','m_expp',1,'p_m_expp','PLY.py',328),
  ('appendPLUS -> empty','appendPLUS',1,'p_appendPLUS','PLY.py',339),
  ('appendMINUS -> empty','appendMINUS',1,'p_appendMINUS','PLY.py',345),
  ('appendMULTIPLY -> empty','appendMULTIPLY',1,'p_appendMULTIPLY','PLY.py',351),
  ('appendDIVIDE -> empty','appendDIVIDE',1,'p_appendDIVIDE','PLY.py',357),
  ('t -> f termino','t',2,'p_t','PLY.py',363),
  ('termino -> MULTIPLY appendMULTIPLY t','termino',3,'p_termino','PLY.py',383),
  ('termino -> DIVIDE appendDIVIDE t','termino',3,'p_termino','PLY.py',384),
  ('termino -> empty','termino',1,'p_termino','PLY.py',385),
  ('f -> PARENOPEN exp PARENCLOSE','f',3,'p_f','PLY.py',396),
  ('f -> ID','f',1,'p_f','PLY.py',397),
  ('f -> CTEINT','f',1,'p_f','PLY.py',398),
  ('f -> CTFLOAT','f',1,'p_f','PLY.py',399),
  ('f -> variable','f',1,'p_f','PLY.py',400),
  ('f -> call_func','f',1,'p_f','PLY.py',401),
  ('variable -> ID','variable',1,'p_variable','PLY.py',422),
  ('variable -> ID BRACEOPEN exp BRACECLOSE','variable',4,'p_variable','PLY.py',423),
  ('variable -> ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE','variable',7,'p_variable','PLY.py',424),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body ifEnd','condition',7,'p_condition','PLY.py',436),
  ('condition -> IF PARENOPEN exp PARENCLOSE cuadruploIF body cuadruploElse ELSE body ifEndElse','condition',10,'p_condition','PLY.py',437),
  ('cuadruploIF -> empty','cuadruploIF',1,'p_cuadruploIF','PLY.py',441),
  ('cuadruploElse -> empty','cuadruploElse',1,'p_cuadruploElse','PLY.py',449),
  ('ifEnd -> empty','ifEnd',1,'p_ifEnd','PLY.py',455),
  ('ifEndElse -> empty','ifEndElse',1,'p_ifEndElse','PLY.py',465),
  ('writing -> PRINT PARENOPEN writingg PARENCLOSE SEMICOLON','writing',5,'p_writing','PLY.py',475),
  ('writingg -> exp','writingg',1,'p_writingg','PLY.py',481),
  ('writingg -> exp COLON writingg','writingg',3,'p_writingg','PLY.py',482),
  ('writingg -> auxString','writingg',1,'p_writingg','PLY.py',483),
  ('writingg -> auxString COLON writingg','writingg',3,'p_writingg','PLY.py',484),
  ('auxString -> CTESTRING','auxString',1,'p_auxString','PLY.py',498),
  ('reading -> READ multivariables SEMICOLON','reading',3,'p_reading','PLY.py',506),
  ('multivariables -> variable','multivariables',1,'p_multivariables','PLY.py',511),
  ('multivariables -> variable COLON multivariables','multivariables',3,'p_multivariables','PLY.py',512),
  ('while_loop -> WHILE whileMigaja PARENOPEN exp PARENCLOSE whileEval body whileEnd','while_loop',8,'p_while_loop','PLY.py',524),
  ('whileMigaja -> empty','whileMigaja',1,'p_whileMigaja','PLY.py',529),
  ('whileEval -> empty','whileEval',1,'p_whileEval','PLY.py',536),
  ('whileEnd -> empty','whileEnd',1,'p_whileEnd','PLY.py',545),
  ('for_loop -> FOR PARENOPEN for_assignment SEMICOLON exp SEMICOLON for_assignment PARENCLOSE body','for_loop',9,'p_for_loop','PLY.py',558),
  ('for_assignment -> variable EQUAL exp','for_assignment',3,'p_for_assignment','PLY.py',563),
  ('return -> RETURN exp SEMICOLON','return',3,'p_return','PLY.py',568),
  ('max -> MAX PARENOPEN exp PARENCLOSE SEMICOLON','max',5,'p_max','PLY.py',573),
  ('min -> MIN PARENOPEN exp PARENCLOSE SEMICOLON','min',5,'p_min','PLY.py',578),
  ('sum -> SUM PARENOPEN exp PARENCLOSE SEMICOLON','sum',5,'p_sum','PLY.py',583),
  ('param_dist -> variable','param_dist',1,'p_param_dist','PLY.py',588),
  ('param_dist -> variable COLON param_dist','param_dist',3,'p_param_dist','PLY.py',589),
  ('binomial -> BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON','binomial',5,'p_binomial','PLY.py',594),
  ('poisson -> POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON','poisson',5,'p_poisson','PLY.py',599),
  ('uniforme -> UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON','uniforme',5,'p_uniforme','PLY.py',604),
  ('normal -> NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON','normal',5,'p_normal','PLY.py',609),
  ('empty -> <empty>','empty',0,'p_empty','PLY.py',614),
]
