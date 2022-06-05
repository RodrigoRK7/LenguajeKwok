class Cuadruplos:
    def __init__(self, operador, operandoIzq, operandoDer, temporal):
        self.operador = operador
        self.operandoIzq = operandoIzq
        self.operandoDer = operandoDer
        self.temporal = temporal
    
    def get(self):
        return [self.operador, self.operandoIzq, self.operandoDer, self.temporal]
    
    def getOperador(self):
        return self.operador
    
    def getOperandoIzq(self):
        return self.operandoIzq
    
    def getOperandoDer(self):
        return self.operandoDer
    
    def getTemporal(self):
        return self.temporal
    

