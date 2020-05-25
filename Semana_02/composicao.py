# Classe Cliente com um construtor (__init__) recebendo dois parametros
# e atribuindo a duas variáveis da classe
class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class CarrinhoCompras:
    def __init__(self, cliente, produtos):
        self.numero_Pedido = '123'
        self.produtos = produtos
        self.cliente = cliente

# Usando property você pode chamar este método como um atributo
# (Ex: objeto.valor_carinho)
    @property
    def valor_carinho(self):
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        return total

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def fechar_carrinho(self):
        print(f"Fechando o pedido: {self.numero_Pedido}")
        print(f"valor do carrinho: {self.valor_carinho}")
        print(f"Nome cliente: {self.cliente.nome}")
        print("Obrigado pela compra")


cliente = Cliente("Gleidson", "123456")

televisao = Produto("Televisão", 1000.90)
maquina_cafe = Produto("Máquina de Café", 89.80)

produtos = [televisao, maquina_cafe]

carrinho = CarrinhoCompras(cliente, produtos)

teclado = Produto("Teclado Mecânico", 175.20)
carrinho.adicionar_produto(teclado)

carrinho.remover_produto(televisao)

print(carrinho.valor_carinho)
print(carrinho.fechar_carrinho())
