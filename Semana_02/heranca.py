# Criando uma classe com um método
class Animal:
    def fazer_barulho(self):
        print("barulho de animal")


# Criando uma classe com um método com retorno
class Domestico:
    def esta_dormindo(self):
        return True


# Criando uma classe utilizando herança (herdando da classe Animal)
class Mamifero(Animal):
    pass


# Criando uma classe utilizando herança múltipla (herdando de duas classes)
class Cachorro(Mamifero, Domestico):
    def enterrar_osso(self):
        print("O osso foi enterrado")


# Criando uma classe utilizando herança (herdando da classe Mamifero)
# e sobrescrevendo o método fazer barulho da classe herdada
class Gato(Mamifero):
    def fazer_barulho(self):
        print("Miau...miau")


# Criando objetos com as classes Gato() e Cachorro()
gato = Gato()
cachoro = Cachorro()
# Método fazer barulho da classe Gato
gato.fazer_barulho()
# Método fazer barulho da classe Animal
cachoro.fazer_barulho()
# Chamando o método ca classe herdada Doméstico
print(cachoro.esta_dormindo())
# Método criado dentro da classe cachorro
cachoro.enterrar_osso()
