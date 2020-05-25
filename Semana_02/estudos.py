class Operacoes:
    def __init__(self, listaValores):
        self.listaValores = listaValores

    def soma(self):
        total = 0
        for valor in self.listaValores:
            total = total.__add__(valor)
        print(f"Soma Total: {total}")

    def subtracao(self):
        total = 0
        for valor in self.listaValores:
            total = total.__sub__(valor)
        print(f"Subtração Total: {total}")

    def multiplicacao(self):
        total = 0
        for valor in self.listaValores:
            total = total.__mul__(valor)
        print(f"Multiplicação Total: {total}")





op = Operacoes([1,2])
op.soma()
