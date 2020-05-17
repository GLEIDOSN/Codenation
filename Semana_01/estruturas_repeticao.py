# Repetição com for
for i in range(10):
    print(i)

convidados = ['Gleidson', 'Karine', 'Vinicius', 'Carlos']

# Repetição for percorrendo uma lista (rotina mais recomendado)
for convidado in convidados:
    print(convidado + ' esta convidado')

for i in range(len(convidados)):
    convidado = convidados[i]
    print(convidado + ' esta convidado (for range)')

# Repetição While
contador = 0

while contador < 5:
    contador = contador + 1
    print('contador: ' + str(contador))
