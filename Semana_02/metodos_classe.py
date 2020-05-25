class Imprssora:
    def __init__(self):
        self.a = 10

    @classmethod
    def imprimir_folha(cls):
        print("folha impressa")

    @classmethod
    def imprimir_livro(cls, paginas):
        for i in range(paginas):
            cls.imprimir_folha()

    @classmethod
    def imprimir_a(cls):
        print(cls.a)


Imprssora.imprimir_folha()

print("=====================================================")
Imprssora.imprimir_livro(5)

impressora = Imprssora()

impressora.imprimir_folha()

print("======================")

impressora.imprimir_a()
