from datetime import datetime
from operator import itemgetter
import math

# Constantes
ENCARGO_PERMANENTE = 0.36
TAXA_LIGACAO_DIURNA = 0.09
TAXA_LIGACAO_NOTURNA = 0.00
SEGUNDOS = 60.0
DIURNO = {'Inicio': 6, 'Fim': 22}
NOTURNO = {'Inicio': 22, 'Fim': 6}

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000}
]


def calcula_valor(tempo_Inicial, tempo_Final):
    total = round(ENCARGO_PERMANENTE, 2)
    duracao = math.floor((tempo_Final - tempo_Inicial).total_seconds()
                         / SEGUNDOS)
    if DIURNO['Inicio'] <= tempo_Final.hour <= DIURNO['Fim']:
        total = (duracao * TAXA_LIGACAO_DIURNA) + ENCARGO_PERMANENTE
        return total
    else:
        return total


def classify_by_phone_number(records):
    lista = {}
    record_result = []
    for rec in records:
        data_ini = datetime.fromtimestamp(rec['start'])
        dat_fim = datetime.fromtimestamp(rec['end'])
        total = calcula_valor(data_ini, dat_fim)
        if rec['source'] not in lista:
            lista[rec['source']] = total
        else:
            lista[rec['source']] = lista[rec['source']] + total

    lista_ord = sorted(lista.items(), key=itemgetter(1), reverse=True)
    for i in lista_ord:
        record_result.append({'source': i[0], 'total': round(i[1], 2)})
    return record_result


print(classify_by_phone_number(records))
