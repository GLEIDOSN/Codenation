# Criando uma lista com três dados
lista_convidados = ['Gleidson', 'Karine', 'Isabele']

print(lista_convidados)

# Adicionado um elemento a lista
lista_convidados.append('Carlos')

print(lista_convidados)

# Removendo o elemento da lista procurando pelo nome
lista_convidados.remove('Carlos')

print(lista_convidados)

# Imprimindo o elemento da posição "0" da lista
print(lista_convidados[0])

print(lista_convidados[2])

# Desta forma ele irá imprimir o último registro da lista
print(lista_convidados[-1])

# Python permite você criar uma lista com divervos tipo de dados
lista_convidados.append(30)

print(lista_convidados)

# tuple - É uma lista que não é mutável, ou seja, não consegue adicionar
# nem remover elementos
tupla1 = (1, 2, 3)
tupla2 = (1, 2, 3, 4, 5)

print(tupla1)

# Soma das duas tuplas
# * Trabalhar com tuplas é muito mais rápido para pesquisa pois ela não
# precisa se preocupar com exclusão e adição de elementos

tupla3 = tupla1 + tupla2

print(tupla3)

# Chave -> valor, podemos adicionar e excluir , ou seja, ela é mutável
dados_pessoais = {'nome': 'Superman', 'Cidade': 'Caucaia'}
# Adicionando
dados_pessoais['veiculo'] = 'Corolla'

print(dados_pessoais)
# Deletando
del dados_pessoais['Cidade']

print(dados_pessoais)
