idade = 30

print('Minha Idade é ' + str(idade))

print('Minha Idade é {}'.format(idade))

# f é um novo recurso do Python e bem mais eficiente que os outros acima
print(f'Minha Idade é: {idade}')

nome = 'Gleidson Freitas'

# f usando com limitação de caractere
# f preenchendo com zero a esqueda na idade
print(F'Meu Nome é {nome:.8} e tenho {idade:05} anos de idade')

dinheiro = 2.50
# f informando ponto flutuante com 2 casas decimais
print(f'Eu tenho {dinheiro:.2f} R$')

lista_itens = ['garfo', 'faca', 'colher']

# f pegando valores de uma lista
print(f'Eu almoço com {lista_itens[0]}, {lista_itens[1]} e também com '
      f'{lista_itens[-1]}')

# f fazendo cálculos matemáticoa
print(f'Eu terei {idade + 30} daqui a 30 anos')
