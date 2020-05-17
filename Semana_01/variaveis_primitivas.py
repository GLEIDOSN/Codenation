nome = 'Gleidson'     # Tipo string
idade = 30            # Tipo inteiro
altura = 1.90         # Tipo flutuante
tutor = True          # Tipo Booleana
trabalhando = None    # None indica que a variável não tem valor

print(nome)           # Comando print irá imprimir no Terminal a variável
print(idade)
print(altura)
print(tutor)
print(trabalhando)

nova_idade = idade + 30
nome_cidade = nome + ' Ceará'
altura_sem_tenis = altura - 5.0

# Simulando o erro, python reconhece os tipo de variáveis e neste caso não é
# permitido somar uma variável do tipo string com uma variável do tipo inteiro,
# comentado para rodar os outros comandos
# resultado = nome + idade

print(nova_idade)
print(nome_cidade)
print(altura_sem_tenis)
# print(resultado)

# Comando para rodar o programa no terminal - python variaveis_primitivas.py
# (nome do arquivo que vc quer compilar)
# Atalho no Pycharm para rodar o programa - Ctrl + Shift + F10
# Dicas: caso dê erro de "IdentationErro: unexpected ident", é porque você
# inseriu espaços na frente de cada linha, retire e rode novamente.
