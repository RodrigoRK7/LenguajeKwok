
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BINOMIAL BRACECLOSE BRACEOPEN BRACKETCLOSE BRACKETOPEN CHAR COLON CTEINT CTESTRING CTFLOAT DIFFERENT DIVIDE ELSE EQUAL FLOAT FOR FUNCTION GREATHEREQUAL GREATHERTHAN ID IF INT LESSEQUAL LESSTHAN MAIN MAX MIN MINUS MULTIPLY NORMAL OR PARENCLOSE PARENOPEN PLOT PLUS POISSON PRINT PROGRAM READ RETURN SAME SEMICOLON SUM UNIFORME VAR VOID WHILE\n    start_program : PROGRAM ID SEMICOLON vars multiple_funcs main_body\n    | PROGRAM ID SEMICOLON vars main_body\n    | PROGRAM ID SEMICOLON multiple_funcs main_body\n    | PROGRAM ID SEMICOLON main_body\n    \n    multiple_funcs : dec_func \n    | dec_func multiple_funcs\n    \n    main_body : MAIN body\n    \n    vars : VAR varss\n    \n    varss : type mvar SEMICOLON varss\n    | type mvar SEMICOLON\n    \n    mvar : ID COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    dec_func : FUNCTION type ID PARENOPEN param PARENCLOSE body\n    | FUNCTION VOID ID PARENOPEN param PARENCLOSE body\n\n    \n    param : type variable\n    | type variable COLON param\n    | empty\n\n    \n    type : INT\n    | FLOAT\n    | CHAR\n    \n    body : BRACKETOPEN bodyy BRACKETCLOSE\n    \n    bodyy : statement \n    | statement bodyy\n    | empty\n\n    \n    statement : dec_variables \n    | assignment\n    | condition\n    | writing\n    | reading\n    | call_func\n    | graph\n    | return\n    | while_loop\n    | for_loop\n    | max\n    | min\n    | sum\n    | normal\n    | uniforme\n    | poisson\n    | binomial\n    \n    dec_variables : dec_variabless\n    \n    dec_variabless : type dec_mvar SEMICOLON dec_variabless\n    | type dec_mvar SEMICOLON\n    \n    dec_mvar : ID COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar\n    | ID \n    | ID BRACEOPEN CTEINT BRACECLOSE \n    | ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE \n    \n    assignment : variable EQUAL exp SEMICOLON\n    \n    call_func : ID PARENOPEN call_funcc PARENCLOSE\n\n    \n    call_funcc : exp \n    | exp COLON call_funcc\n    | empty\n    \n    graph : PLOT PARENOPEN exp PARENCLOSE SEMICOLON\n    \n    \n    exp : exp GREATHERTHAN exp \n    | exp LESSTHAN exp \n    | exp GREATHEREQUAL exp \n    | exp LESSEQUAL exp \n    | exp DIFFERENT exp \n    | exp SAME exp\n    | exp AND exp\n    | exp OR exp\n    | m_exp\n\n    \n    m_exp : t m_expp \n    \n    m_expp : PLUS appendPLUS m_exp\n        | MINUS appendMINUS m_exp\n        | empty\n    \n    appendPLUS : empty\n    \n    appendMINUS : empty\n    \n    appendMULTIPLY : empty\n    \n    appendDIVIDE : empty\n    \n    t : f termino\n    \n    termino : MULTIPLY appendMULTIPLY t \n        | DIVIDE appendDIVIDE t \n        | empty\n    \n    f : PARENOPEN exp PARENCLOSE \n    | ID\n    | CTEINT\n    | CTFLOAT \n    | variable\n    | call_func\n    \n    variable : ID \n    | ID BRACEOPEN exp BRACECLOSE \n    | ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE\n    \n    condition : IF PARENOPEN exp PARENCLOSE body  \n        | IF PARENOPEN exp PARENCLOSE body ELSE body \n    \n    writing : PRINT PARENOPEN writingg PARENCLOSE SEMICOLON\n    \n    writingg : exp\n    | exp COLON writingg\n    | CTESTRING \n    | CTESTRING COLON writingg\n    \n    reading : READ multivariables SEMICOLON\n       \n    \n    multivariables : variable\n    | variable COLON multivariables\n       \n    \n    while_loop : WHILE PARENOPEN exp PARENCLOSE body\n       \n    \n    for_loop : FOR PARENOPEN for_assignment SEMICOLON exp SEMICOLON for_assignment PARENCLOSE body\n       \n    \n    for_assignment : variable EQUAL exp\n       \n    \n    return : RETURN exp SEMICOLON\n       \n    \n    max : MAX PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    min : MIN PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    sum : SUM PARENOPEN exp PARENCLOSE SEMICOLON\n       \n    \n    param_dist : variable\n    | variable COLON param_dist\n       \n    \n    binomial : BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    poisson : POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    uniforme : UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    normal : NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON\n       \n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,13,14,21,25,71,],[0,-4,-2,-3,-7,-1,-25,]),'ID':([2,16,17,18,19,22,23,24,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,52,55,65,69,71,73,74,75,79,80,81,86,92,93,94,95,96,97,98,99,100,113,114,120,121,122,123,124,125,126,127,128,130,131,134,135,149,150,152,157,160,161,163,164,175,176,177,178,179,180,181,182,185,186,191,195,202,203,204,208,209,214,217,218,219,220,222,223,224,233,235,238,243,247,248,],[3,27,-22,-23,-24,53,66,67,53,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,78,87,102,27,-25,87,87,87,87,87,87,87,87,78,87,87,87,78,78,78,78,-98,78,-104,87,87,87,87,87,87,87,87,-114,-114,-114,-114,-48,102,78,-55,87,87,-56,87,87,-74,87,-75,87,-76,87,-77,87,87,78,-47,27,-91,-93,87,-60,-101,-105,-106,-107,-113,-112,-111,-110,78,102,-92,27,-102,102,]),'SEMICOLON':([3,26,27,76,77,78,82,83,84,85,87,88,89,90,91,101,102,106,108,129,132,133,136,139,156,159,162,163,165,166,167,168,169,170,171,172,173,174,183,187,188,189,190,192,193,194,196,210,211,212,213,215,216,225,230,237,239,242,245,246,249,],[4,68,-14,113,-99,-88,120,-69,-114,-114,-83,-84,-85,-86,-87,149,-52,-11,157,-70,-73,-78,-81,185,-15,204,-100,-56,-89,209,-61,-62,-63,-64,-65,-66,-67,-68,-82,217,218,219,220,222,223,224,-49,-71,-72,-79,-80,233,-103,-53,-12,-16,-90,-50,-54,-13,-51,]),'VAR':([4,],[8,]),'MAIN':([4,5,6,9,12,15,20,68,71,105,227,228,],[10,10,10,-5,10,-8,-6,-10,-25,-9,-17,-18,]),'FUNCTION':([4,5,9,15,68,71,105,227,228,],[11,11,11,-8,-10,-25,-9,-17,-18,]),'INT':([8,11,22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,68,71,103,104,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,226,238,247,],[17,17,17,17,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,17,-25,17,17,-98,-104,17,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,17,-92,-102,]),'FLOAT':([8,11,22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,68,71,103,104,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,226,238,247,],[18,18,18,18,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,18,-25,18,18,-98,-104,18,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,18,-92,-102,]),'CHAR':([8,11,22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,68,71,103,104,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,226,238,247,],[19,19,19,19,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,19,-25,19,19,-98,-104,19,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,19,-92,-102,]),'BRACKETOPEN':([10,158,184,199,200,231,244,],[22,22,22,22,22,22,22,]),'VOID':([11,],[24,]),'BRACKETCLOSE':([22,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,72,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[-114,71,-26,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-27,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'IF':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[50,50,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'PRINT':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[51,51,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'READ':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[52,52,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'PLOT':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[54,54,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'RETURN':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[55,55,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'WHILE':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[56,56,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'FOR':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[57,57,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'MAX':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[58,58,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'MIN':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[59,59,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'SUM':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[60,60,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'NORMAL':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[61,61,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'UNIFORME':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[62,62,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'POISSON':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[63,63,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'BINOMIAL':([22,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,71,113,120,149,157,163,195,203,204,209,214,217,218,219,220,222,223,224,238,247,],[64,64,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-25,-98,-104,-48,-55,-56,-47,-91,-93,-60,-101,-105,-106,-107,-113,-112,-111,-110,-92,-102,]),'COLON':([27,77,78,83,84,85,87,88,89,90,91,102,111,112,116,129,132,133,136,145,156,163,165,167,168,169,170,171,172,173,174,183,198,210,211,212,213,225,237,239,245,],[69,114,-88,-69,-114,-114,-83,-84,-85,-86,-87,150,160,161,164,-70,-73,-78,-81,191,202,-56,-89,-61,-62,-63,-64,-65,-66,-67,-68,-82,226,-71,-72,-79,-80,235,243,-90,248,]),'BRACEOPEN':([27,53,78,87,102,156,165,225,],[70,80,80,80,151,201,208,234,]),'EQUAL':([49,53,78,140,165,239,],[73,-88,-88,186,-89,-90,]),'PARENOPEN':([50,51,53,54,55,56,57,58,59,60,61,62,63,64,66,67,73,74,75,79,80,81,86,87,92,94,95,96,121,122,123,124,125,126,127,128,130,131,134,135,160,161,164,175,176,177,178,179,180,181,182,185,186,208,],[74,75,79,81,86,92,93,94,95,96,97,98,99,100,103,104,86,86,86,86,86,86,86,79,86,86,86,86,86,86,86,86,86,86,86,86,-114,-114,-114,-114,86,86,86,86,-74,86,-75,86,-76,86,-77,86,86,86,]),'CTEINT':([55,70,73,74,75,79,80,81,86,92,94,95,96,121,122,123,124,125,126,127,128,130,131,134,135,151,160,161,164,175,176,177,178,179,180,181,182,185,186,201,208,234,],[88,107,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,-114,-114,-114,-114,197,88,88,88,88,-74,88,-75,88,-76,88,-77,88,88,229,88,241,]),'CTFLOAT':([55,73,74,75,79,80,81,86,92,94,95,96,121,122,123,124,125,126,127,128,130,131,134,135,160,161,164,175,176,177,178,179,180,181,182,185,186,208,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,-114,-114,-114,-114,89,89,89,89,-74,89,-75,89,-76,89,-77,89,89,89,]),'ELSE':([71,203,],[-25,231,]),'CTESTRING':([75,160,161,],[112,112,112,]),'PARENCLOSE':([78,79,83,84,85,87,88,89,90,91,103,104,109,110,111,112,115,116,117,119,129,132,133,136,137,138,141,142,143,144,145,146,147,148,153,154,155,163,164,165,167,168,169,170,171,172,173,174,183,198,205,206,207,210,211,212,213,216,221,226,236,239,240,],[-88,-114,-69,-114,-114,-83,-84,-85,-86,-87,-114,-114,158,159,-94,-96,163,-57,-59,166,-70,-73,-78,-81,183,184,187,188,189,190,-108,192,193,194,199,-21,200,-56,-114,-89,-61,-62,-63,-64,-65,-66,-67,-68,-82,-19,-95,-97,-58,-71,-72,-79,-80,-103,-109,-114,-20,-90,244,]),'GREATHERTHAN':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[121,-69,-114,-114,-83,-84,-85,-86,-87,121,121,121,121,121,121,-70,-73,-78,-81,121,121,121,121,121,-56,-89,121,121,121,121,121,121,121,121,-82,-71,-72,-79,-80,121,121,121,-90,]),'LESSTHAN':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[122,-69,-114,-114,-83,-84,-85,-86,-87,122,122,122,122,122,122,-70,-73,-78,-81,122,122,122,122,122,-56,-89,122,122,122,122,122,122,122,122,-82,-71,-72,-79,-80,122,122,122,-90,]),'GREATHEREQUAL':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[123,-69,-114,-114,-83,-84,-85,-86,-87,123,123,123,123,123,123,-70,-73,-78,-81,123,123,123,123,123,-56,-89,123,123,123,123,123,123,123,123,-82,-71,-72,-79,-80,123,123,123,-90,]),'LESSEQUAL':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[124,-69,-114,-114,-83,-84,-85,-86,-87,124,124,124,124,124,124,-70,-73,-78,-81,124,124,124,124,124,-56,-89,124,124,124,124,124,124,124,124,-82,-71,-72,-79,-80,124,124,124,-90,]),'DIFFERENT':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[125,-69,-114,-114,-83,-84,-85,-86,-87,125,125,125,125,125,125,-70,-73,-78,-81,125,125,125,125,125,-56,-89,125,125,125,125,125,125,125,125,-82,-71,-72,-79,-80,125,125,125,-90,]),'SAME':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[126,-69,-114,-114,-83,-84,-85,-86,-87,126,126,126,126,126,126,-70,-73,-78,-81,126,126,126,126,126,-56,-89,126,126,126,126,126,126,126,126,-82,-71,-72,-79,-80,126,126,126,-90,]),'AND':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[127,-69,-114,-114,-83,-84,-85,-86,-87,127,127,127,127,127,127,-70,-73,-78,-81,127,127,127,127,127,-56,-89,127,127,127,127,127,127,127,127,-82,-71,-72,-79,-80,127,127,127,-90,]),'OR':([82,83,84,85,87,88,89,90,91,108,109,111,116,118,119,129,132,133,136,137,138,141,142,143,163,165,167,168,169,170,171,172,173,174,183,210,211,212,213,215,216,232,239,],[128,-69,-114,-114,-83,-84,-85,-86,-87,128,128,128,128,128,128,-70,-73,-78,-81,128,128,128,128,128,-56,-89,128,128,128,128,128,128,128,128,-82,-71,-72,-79,-80,128,128,128,-90,]),'BRACECLOSE':([83,84,85,87,88,89,90,91,107,118,129,132,133,136,163,165,167,168,169,170,171,172,173,174,183,197,210,211,212,213,229,232,239,241,],[-69,-114,-114,-83,-84,-85,-86,-87,156,165,-70,-73,-78,-81,-56,-89,-61,-62,-63,-64,-65,-66,-67,-68,-82,225,-71,-72,-79,-80,237,239,-90,245,]),'PLUS':([84,85,87,88,89,90,91,133,136,163,165,183,212,213,239,],[130,-114,-83,-84,-85,-86,-87,-78,-81,-56,-89,-82,-79,-80,-90,]),'MINUS':([84,85,87,88,89,90,91,133,136,163,165,183,212,213,239,],[131,-114,-83,-84,-85,-86,-87,-78,-81,-56,-89,-82,-79,-80,-90,]),'MULTIPLY':([85,87,88,89,90,91,163,165,183,239,],[134,-83,-84,-85,-86,-87,-56,-89,-82,-90,]),'DIVIDE':([85,87,88,89,90,91,163,165,183,239,],[135,-83,-84,-85,-86,-87,-56,-89,-82,-90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start_program':([0,],[1,]),'vars':([4,],[5,]),'multiple_funcs':([4,5,9,],[6,12,20,]),'main_body':([4,5,6,12,],[7,13,14,25,]),'dec_func':([4,5,9,],[9,9,9,]),'varss':([8,68,],[15,105,]),'type':([8,11,22,29,68,103,104,149,226,],[16,23,65,65,16,152,152,65,152,]),'body':([10,158,184,199,200,231,244,],[21,203,214,227,228,238,247,]),'mvar':([16,69,202,243,],[26,106,230,246,]),'bodyy':([22,29,],[28,72,]),'statement':([22,29,],[29,29,]),'empty':([22,29,79,84,85,103,104,130,131,134,135,164,226,],[30,30,117,132,136,154,154,176,178,180,182,117,154,]),'dec_variables':([22,29,],[31,31,]),'assignment':([22,29,],[32,32,]),'condition':([22,29,],[33,33,]),'writing':([22,29,],[34,34,]),'reading':([22,29,],[35,35,]),'call_func':([22,29,55,73,74,75,79,80,81,86,92,94,95,96,121,122,123,124,125,126,127,128,160,161,164,175,177,179,181,185,186,208,],[36,36,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,]),'graph':([22,29,],[37,37,]),'return':([22,29,],[38,38,]),'while_loop':([22,29,],[39,39,]),'for_loop':([22,29,],[40,40,]),'max':([22,29,],[41,41,]),'min':([22,29,],[42,42,]),'sum':([22,29,],[43,43,]),'normal':([22,29,],[44,44,]),'uniforme':([22,29,],[45,45,]),'poisson':([22,29,],[46,46,]),'binomial':([22,29,],[47,47,]),'dec_variabless':([22,29,149,],[48,48,195,]),'variable':([22,29,52,55,73,74,75,79,80,81,86,92,93,94,95,96,97,98,99,100,114,121,122,123,124,125,126,127,128,152,160,161,164,175,177,179,181,185,186,191,208,233,],[49,49,77,90,90,90,90,90,90,90,90,90,140,90,90,90,145,145,145,145,77,90,90,90,90,90,90,90,90,198,90,90,90,90,90,90,90,90,90,145,90,140,]),'multivariables':([52,114,],[76,162,]),'exp':([55,73,74,75,79,80,81,86,92,94,95,96,121,122,123,124,125,126,127,128,160,161,164,185,186,208,],[82,108,109,111,116,118,119,137,138,141,142,143,167,168,169,170,171,172,173,174,111,111,116,215,216,232,]),'m_exp':([55,73,74,75,79,80,81,86,92,94,95,96,121,122,123,124,125,126,127,128,160,161,164,175,177,185,186,208,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,210,211,83,83,83,]),'t':([55,73,74,75,79,80,81,86,92,94,95,96,121,122,123,124,125,126,127,128,160,161,164,175,177,179,181,185,186,208,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,212,213,84,84,84,]),'f':([55,73,74,75,79,80,81,86,92,94,95,96,121,122,123,124,125,126,127,128,160,161,164,175,177,179,181,185,186,208,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'dec_mvar':([65,150,235,248,],[101,196,242,249,]),'writingg':([75,160,161,],[110,205,206,]),'call_funcc':([79,164,],[115,207,]),'m_expp':([84,],[129,]),'termino':([85,],[133,]),'for_assignment':([93,233,],[139,240,]),'param_dist':([97,98,99,100,191,],[144,146,147,148,221,]),'param':([103,104,226,],[153,155,236,]),'appendPLUS':([130,],[175,]),'appendMINUS':([131,],[177,]),'appendMULTIPLY':([134,],[179,]),'appendDIVIDE':([135,],[181,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start_program","S'",1,None,None,None),
  ('start_program -> PROGRAM ID SEMICOLON vars multiple_funcs main_body','start_program',6,'p_start_program','PLY.py',104),
  ('start_program -> PROGRAM ID SEMICOLON vars main_body','start_program',5,'p_start_program','PLY.py',105),
  ('start_program -> PROGRAM ID SEMICOLON multiple_funcs main_body','start_program',5,'p_start_program','PLY.py',106),
  ('start_program -> PROGRAM ID SEMICOLON main_body','start_program',4,'p_start_program','PLY.py',107),
  ('multiple_funcs -> dec_func','multiple_funcs',1,'p_multiple_funcs','PLY.py',122),
  ('multiple_funcs -> dec_func multiple_funcs','multiple_funcs',2,'p_multiple_funcs','PLY.py',123),
  ('main_body -> MAIN body','main_body',2,'p_main_body','PLY.py',127),
  ('vars -> VAR varss','vars',2,'p_vars','PLY.py',132),
  ('varss -> type mvar SEMICOLON varss','varss',4,'p_varss','PLY.py',138),
  ('varss -> type mvar SEMICOLON','varss',3,'p_varss','PLY.py',139),
  ('mvar -> ID COLON mvar','mvar',3,'p_mvar','PLY.py',148),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',6,'p_mvar','PLY.py',149),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON mvar','mvar',9,'p_mvar','PLY.py',150),
  ('mvar -> ID','mvar',1,'p_mvar','PLY.py',151),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE','mvar',4,'p_mvar','PLY.py',152),
  ('mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','mvar',7,'p_mvar','PLY.py',153),
  ('dec_func -> FUNCTION type ID PARENOPEN param PARENCLOSE body','dec_func',7,'p_dec_func','PLY.py',161),
  ('dec_func -> FUNCTION VOID ID PARENOPEN param PARENCLOSE body','dec_func',7,'p_dec_func','PLY.py',162),
  ('param -> type variable','param',2,'p_param','PLY.py',174),
  ('param -> type variable COLON param','param',4,'p_param','PLY.py',175),
  ('param -> empty','param',1,'p_param','PLY.py',176),
  ('type -> INT','type',1,'p_type','PLY.py',184),
  ('type -> FLOAT','type',1,'p_type','PLY.py',185),
  ('type -> CHAR','type',1,'p_type','PLY.py',186),
  ('body -> BRACKETOPEN bodyy BRACKETCLOSE','body',3,'p_body','PLY.py',192),
  ('bodyy -> statement','bodyy',1,'p_bodyy','PLY.py',197),
  ('bodyy -> statement bodyy','bodyy',2,'p_bodyy','PLY.py',198),
  ('bodyy -> empty','bodyy',1,'p_bodyy','PLY.py',199),
  ('statement -> dec_variables','statement',1,'p_statement','PLY.py',205),
  ('statement -> assignment','statement',1,'p_statement','PLY.py',206),
  ('statement -> condition','statement',1,'p_statement','PLY.py',207),
  ('statement -> writing','statement',1,'p_statement','PLY.py',208),
  ('statement -> reading','statement',1,'p_statement','PLY.py',209),
  ('statement -> call_func','statement',1,'p_statement','PLY.py',210),
  ('statement -> graph','statement',1,'p_statement','PLY.py',211),
  ('statement -> return','statement',1,'p_statement','PLY.py',212),
  ('statement -> while_loop','statement',1,'p_statement','PLY.py',213),
  ('statement -> for_loop','statement',1,'p_statement','PLY.py',214),
  ('statement -> max','statement',1,'p_statement','PLY.py',215),
  ('statement -> min','statement',1,'p_statement','PLY.py',216),
  ('statement -> sum','statement',1,'p_statement','PLY.py',217),
  ('statement -> normal','statement',1,'p_statement','PLY.py',218),
  ('statement -> uniforme','statement',1,'p_statement','PLY.py',219),
  ('statement -> poisson','statement',1,'p_statement','PLY.py',220),
  ('statement -> binomial','statement',1,'p_statement','PLY.py',221),
  ('dec_variables -> dec_variabless','dec_variables',1,'p_dec_variables','PLY.py',225),
  ('dec_variabless -> type dec_mvar SEMICOLON dec_variabless','dec_variabless',4,'p_dec_variabless','PLY.py',231),
  ('dec_variabless -> type dec_mvar SEMICOLON','dec_variabless',3,'p_dec_variabless','PLY.py',232),
  ('dec_mvar -> ID COLON dec_mvar','dec_mvar',3,'p_dec_mvar','PLY.py',240),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',6,'p_dec_mvar','PLY.py',241),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE COLON dec_mvar','dec_mvar',9,'p_dec_mvar','PLY.py',242),
  ('dec_mvar -> ID','dec_mvar',1,'p_dec_mvar','PLY.py',243),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE','dec_mvar',4,'p_dec_mvar','PLY.py',244),
  ('dec_mvar -> ID BRACEOPEN CTEINT BRACECLOSE BRACEOPEN CTEINT BRACECLOSE','dec_mvar',7,'p_dec_mvar','PLY.py',245),
  ('assignment -> variable EQUAL exp SEMICOLON','assignment',4,'p_assignment','PLY.py',254),
  ('call_func -> ID PARENOPEN call_funcc PARENCLOSE','call_func',4,'p_call_func','PLY.py',271),
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
  ('m_exp -> t m_expp','m_exp',2,'p_m_exp','PLY.py',316),
  ('m_expp -> PLUS appendPLUS m_exp','m_expp',3,'p_m_expp','PLY.py',327),
  ('m_expp -> MINUS appendMINUS m_exp','m_expp',3,'p_m_expp','PLY.py',328),
  ('m_expp -> empty','m_expp',1,'p_m_expp','PLY.py',329),
  ('appendPLUS -> empty','appendPLUS',1,'p_appendPLUS','PLY.py',340),
  ('appendMINUS -> empty','appendMINUS',1,'p_appendMINUS','PLY.py',346),
  ('appendMULTIPLY -> empty','appendMULTIPLY',1,'p_appendMULTIPLY','PLY.py',352),
  ('appendDIVIDE -> empty','appendDIVIDE',1,'p_appendDIVIDE','PLY.py',358),
  ('t -> f termino','t',2,'p_t','PLY.py',364),
  ('termino -> MULTIPLY appendMULTIPLY t','termino',3,'p_termino','PLY.py',384),
  ('termino -> DIVIDE appendDIVIDE t','termino',3,'p_termino','PLY.py',385),
  ('termino -> empty','termino',1,'p_termino','PLY.py',386),
  ('f -> PARENOPEN exp PARENCLOSE','f',3,'p_f','PLY.py',397),
  ('f -> ID','f',1,'p_f','PLY.py',398),
  ('f -> CTEINT','f',1,'p_f','PLY.py',399),
  ('f -> CTFLOAT','f',1,'p_f','PLY.py',400),
  ('f -> variable','f',1,'p_f','PLY.py',401),
  ('f -> call_func','f',1,'p_f','PLY.py',402),
  ('variable -> ID','variable',1,'p_variable','PLY.py',423),
  ('variable -> ID BRACEOPEN exp BRACECLOSE','variable',4,'p_variable','PLY.py',424),
  ('variable -> ID BRACEOPEN exp BRACECLOSE BRACEOPEN exp BRACECLOSE','variable',7,'p_variable','PLY.py',425),
  ('condition -> IF PARENOPEN exp PARENCLOSE body','condition',5,'p_condition','PLY.py',437),
  ('condition -> IF PARENOPEN exp PARENCLOSE body ELSE body','condition',7,'p_condition','PLY.py',438),
  ('writing -> PRINT PARENOPEN writingg PARENCLOSE SEMICOLON','writing',5,'p_writing','PLY.py',442),
  ('writingg -> exp','writingg',1,'p_writingg','PLY.py',448),
  ('writingg -> exp COLON writingg','writingg',3,'p_writingg','PLY.py',449),
  ('writingg -> CTESTRING','writingg',1,'p_writingg','PLY.py',450),
  ('writingg -> CTESTRING COLON writingg','writingg',3,'p_writingg','PLY.py',451),
  ('reading -> READ multivariables SEMICOLON','reading',3,'p_reading','PLY.py',456),
  ('multivariables -> variable','multivariables',1,'p_multivariables','PLY.py',461),
  ('multivariables -> variable COLON multivariables','multivariables',3,'p_multivariables','PLY.py',462),
  ('while_loop -> WHILE PARENOPEN exp PARENCLOSE body','while_loop',5,'p_while_loop','PLY.py',467),
  ('for_loop -> FOR PARENOPEN for_assignment SEMICOLON exp SEMICOLON for_assignment PARENCLOSE body','for_loop',9,'p_for_loop','PLY.py',472),
  ('for_assignment -> variable EQUAL exp','for_assignment',3,'p_for_assignment','PLY.py',477),
  ('return -> RETURN exp SEMICOLON','return',3,'p_return','PLY.py',482),
  ('max -> MAX PARENOPEN exp PARENCLOSE SEMICOLON','max',5,'p_max','PLY.py',487),
  ('min -> MIN PARENOPEN exp PARENCLOSE SEMICOLON','min',5,'p_min','PLY.py',492),
  ('sum -> SUM PARENOPEN exp PARENCLOSE SEMICOLON','sum',5,'p_sum','PLY.py',497),
  ('param_dist -> variable','param_dist',1,'p_param_dist','PLY.py',502),
  ('param_dist -> variable COLON param_dist','param_dist',3,'p_param_dist','PLY.py',503),
  ('binomial -> BINOMIAL PARENOPEN param_dist PARENCLOSE SEMICOLON','binomial',5,'p_binomial','PLY.py',508),
  ('poisson -> POISSON PARENOPEN param_dist PARENCLOSE SEMICOLON','poisson',5,'p_poisson','PLY.py',513),
  ('uniforme -> UNIFORME PARENOPEN param_dist PARENCLOSE SEMICOLON','uniforme',5,'p_uniforme','PLY.py',518),
  ('normal -> NORMAL PARENOPEN param_dist PARENCLOSE SEMICOLON','normal',5,'p_normal','PLY.py',523),
  ('empty -> <empty>','empty',0,'p_empty','PLY.py',528),
]
