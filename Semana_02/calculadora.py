class Calculadora():
    def __init__(self):
        self.bateria = Bateria()
        self.entrada = TeclasCalculadora()
        self.operacoes = Operacoes()
        self.display = Display()

    def novaOperacao(self, valor1, valor2):
        self.entrada.valorEntrada(valor1, valor2)
        self.bateria.uso()

    def soma(self):
        soma = self.operacoes.soma(self.entrada.getValor())
        self.display.mostraTexto(soma)
        self.bateria.uso()


class Bateria():
    def __init__(self):
        self.pcBateria = 100
        self.gasto = 0.9

    def uso(self):
        self.pcBateria = self.pcBateria*self.gasto
        self.getBateriaFraca()

    def getBateriaFraca(self):
        print(" tem " + str(self.pcBateria) + "% de bateria")
        if(self.pcBateria < 55):
            print("bateria fraca")
            return True
        else:
            return False


class TeclasCalculadora():
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0

    def valorEntrada(self, v1, v2):
        self.valor1 = v1
        self.valor2 = v2

    def getValor(self):
        return [self.valor1, self.valor2]


class Operacoes():
    def soma(self, valores):
        val = 0
        for v in valores:
            val += v
        return val

    def substração(self, valores):
        val = 0
        for v in valores:
            val -= v
        return val


class Display():
    def __init__(self):
        self.brilhoTela = 20
        self.textoTela = "0"

    def mostraTexto(self, textoTela):
        self.textoTela = textoTela
        print(self.textoTela)


cal1 = Calculadora()

cal1.novaOperacao(10, 20)

cal1.soma()

cal1.novaOperacao(15, 20)

cal1.soma()

cal1.novaOperacao(20, 20)

cal1.soma()
