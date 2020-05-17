idade = 20

# Condição if ou else
if idade < 18:
    print('Menor de Idade')
else:
    print('Maior de Idade')

veiculo = {'tipo': 'moto2', 'marca': 'Honda', 'potencia_motor': 140}

# Condição if com and
if veiculo['tipo'] == 'moto2' and veiculo['marca'] == 'Honda':
    print('O veículo é uma moto')
else:
    print('O veículo não é uma moto')

# Imprimindo o resultado de uma condição
resultado = veiculo['tipo'] == 'moto'

print(resultado)

# Condição if com or
if veiculo['tipo'] == 'moto' or veiculo['potencia_motor'] < 120:
    print('Você tem um veículo muito rápido')
else:
    print('Seu veículo não é rápido')

if (veiculo['tipo'] == 'moto' and veiculo['potencia_motor'] > 120) or \
        veiculo['marca'] == 'Honda':
    print('O seu veículo é muito bom')

# Condição if com elseif
if veiculo['tipo'] == 'moto':
    print('moto')
elif veiculo['tipo'] == 'carro':
    print('carro')
elif veiculo['tipo'] == 'moto2':
    print('moto2')

condicao = [1, 2, 3]

# Comando para verificar quantidades de elemento dentro de uma lista (len)
if len(condicao):
    print('verdadeiro')
else:
    print('falso')

print(len(condicao))
