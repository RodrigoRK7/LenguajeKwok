class Cuadruplos:
    def __init__(self, operador, operandoIzq, operandoDer, temporal):
        self.operador = operador
        self.operandoIzq = operandoIzq
        self.operandoDer = operandoDer
        self.temporal = temporal
    
    def get(self):
        return [self.operador, self.operandoIzq, self.operandoDer, self.temporal]
    
    def editTemporal(self, temporal):
        self.temporal = temporal

