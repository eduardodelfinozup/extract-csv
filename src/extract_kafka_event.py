# -*- coding: utf-8 -*-
# !/usr/bin/python3

# pip install pandas

import os, csv
from pathlib import Path

def extractKafkaEvent(readCsv, coluna, limiter):
    colunas = ['TOPIC','DATA']
    gerar_colunas('parametros_extraidos', colunas)

    try:
        var = list()
        for row in readArquivoCsv(readCsv, limiter):
            data = row[coluna]
            var.append(data)

            topic = data.find('topic')
            eventId = data.find('eventId')
            topicEvent = str(data[topic:eventId]).replace('topic:','').replace(',','')

            p1 = data.find('header')
            p2 = data.find('statusReason')
            p3 = data.find('NONE')
            p4 = data.find('PAYMENT_CANCELL')
            p5 = data.find('PAYMENT_FAILED')

            if p3 > 0:
                print(p1, p2, p3)
                nextP = p3 - p2
                kafkaEvent = payload_format(str('{'"'" + data[p1:p2  + nextP + 5] + '}'))
                extractCsv(topicEvent, kafkaEvent)

            elif p4 > 0:
                print(p1, p2, p4)
                nextP = p4 - p2
                kafkaEvent = payload_format(str('{'"'" + data[p1:p2  + nextP + 15] + "'"'}'))
                extractCsv(topicEvent, kafkaEvent)

            elif p5 > 0:
                print(p1, p2, p5)
                nextP = p5 - p2
                kafkaEvent = payload_format(str('{'"'" + data[p1:p2  + nextP + 14] + "'"'}'))
                extractCsv(topicEvent, kafkaEvent)

            else:
                print("Error")

        totalVar = getTotal(var)
        print("TOTAL ENCONTRADO: ", totalVar)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        print("PROCESSAMENTO REALIZADO ...")
        return ''


def extractCsv(topicEvent, kafkaEvent):
    registro = [topicEvent, kafkaEvent]
    gerar_registro_in_csv('parametros_extraidos', registro)
    print(f'{topicEvent}, {kafkaEvent}')

def getTotal(var):
    return len(var)

def format_None(data):
    return data.replace('None','null')

def format_False(data):
    return data.replace('False','false')

def format_True(data):
    return data.replace('True','true')

def format_aspas(data):
    return str(data).replace('\'','"')

def payload_format(data):
    f1 = format_aspas(data)
    f2 = format_False(f1)
    f3 = format_True(f2)
    payload = format_None(f3)
    return payload


def gerar_colunas(name_arquivo_csv, colunas):
    try:
        Path('writer').mkdir(exist_ok=True)

        # TODO: aqui usamos o 'w' para abri-lo para gravação
        with open('./writer/' + name_arquivo_csv + '.csv', 'w', encoding='utf_8', newline='') as saida:

            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            escrever.writerow(colunas)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()


def gerar_registro_in_csv(name_arquivo_csv, rows):
    try:
        # TODO: aqui usamos o 'a' para continuar a gravação
        with open('./writer/' + name_arquivo_csv + '.csv', 'a', encoding='utf_8', newline='') as saida:
            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            escrever.writerow(rows)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()
        if saida.closed:
            print('------------------------------------CARREGADO------------------------------------------------------')


def readArquivoCsv(name_arquivo_csv, limiter):
    try:
        nome_ficheiro = name_arquivo_csv
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'read/' + nome_ficheiro + '.csv')

        with open(my_file, encoding='utf_8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=limiter)
            csv_reader.__next__()

            listRow = list()
            for row in csv_reader:
                listRow.append(row)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        return listRow


def main():
    try:
        readCsv = 'BUG410'
        coluna = 0
        limiter = ','

        if not readCsv:

            print('Voce esqueceu passar o nome do arquivo csv')

        else:

            extractKafkaEvent(readCsv, coluna, limiter)

    except Exception as ex:

        print('ERROR: %s' % ex)

    finally:
        print('OK')


if __name__ == '__main__':
    main()
