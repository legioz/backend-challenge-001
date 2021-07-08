# -*- coding: utf-8 -*-
# TODO: remover imports que não são utilizaddos(traceback, timedelta...)
import os, sys, traceback, logging, configparser
import xlsxwriter
from datetime import datetime, timedelta, timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

def main(argv):
    # TODO: seguir padronização da pep8, 2 linhas antes da declaração da função
    greetings()

    print('Press Crtl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    app = Flask(__name__)
    handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    # TODO: Retirar váriaveis de ambiente do código versionado! Adicionalas em um .env fora do versionamento
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123mudar@127.0.0.1:5432/bot_db'
    db = SQLAlchemy(app)
    config = configparser.ConfigParser()
    config.read('/tmp/bot/settings/config.ini')

    var1 = int(config.get('scheduler','IntervalInMinutes'))
    app.logger.warning('Intervalo entre as execucoes do processo: {}'.format(var1))
    scheduler = BlockingScheduler()
    # TODO: adicionar tratativa com valores default para caso algum valor seja removido do .config
    # desta forma não quebra a execução do log
    task1_instance = scheduler.add_job(task1(db), 'interval', id='task1_job', minutes=var1)

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        pass

def greetings():
    # TODO: implementar pep8 nos espaçamentos
    # TODO: utilizar um unico print passando a string completa definida em uma variavel unica
    # invés de ficar chamando a mesma função repetidas vezes...
    # TODO: utilizar "\n" para quebra de linha e a formatação de strings do python para 
    # identação e ajudate nas boras do código
    print('             ##########################')
    print('             # - ACME - Tasks Robot - #')
    print('             # - v 1.0 - 2020-07-28 - #')
    print('             ##########################')

def task1(db):

    # TODO: utilizar f-strings
    file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    # TODO: criar  função para filtrar arquivos muito velhos no diretório e excluir apos determinado tempo
    file_path = os.path.join(os.path.curdir, file_name)
    # TODO: uma possibilidade seria utilizar a lib nativa csv uma vez que só estão sendo salvos
    # registros sem nenhuma tratativa, ou caso fosse realizada uma manipulação poderia
    # fazer a utilização do pandas uma vez que já possue função tambem para escrever um dataframe
    # em um xlsx/csv 
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    # TODO: UTILIZAR ORM invés para realizar a consulta RAW, se fosse uma query de complexidade
    #  absurda que precisasse utilizar RAW por performance não havia necessidade de jogar na ORM,
    #  bastava importar o conector direto e fazer os bindparams passando a CTE da consulta
    orders = db.session.execute('SELECT * FROM users;')
    # TODO: fechar conexão, ou utilizar with
    
    index = 1
    # TODO: substituir ''.format() pelas f-strings, a leitura é melhor e nas versoes
    # do python acima da 3.8 a performance delas é muito melhor do que a dos outros 
    # métodos de formatação

    # TODO: o nome das colunas poderia ser adicionado com o pandas, ou fazer um list prepend insert() caso fosse utilizar a lib csv
    worksheet.write('A{0}'.format(index),'Id')
    worksheet.write('B{0}'.format(index),'Name')
    worksheet.write('C{0}'.format(index),'Email')
    worksheet.write('D{0}'.format(index),'Password')
    worksheet.write('E{0}'.format(index),'Role Id')
    worksheet.write('F{0}'.format(index),'Created At')
    worksheet.write('G{0}'.format(index),'Updated At')
    
    for order in orders:
        index = index + 1

        print('Id: {0}'.format(order[0]))
        worksheet.write('A{0}'.format(index),order[0])
        print('Name: {0}'.format(order[1]))
        worksheet.write('B{0}'.format(index),order[1])
        print('Email: {0}'.format(order[2]))
        worksheet.write('C{0}'.format(index),order[2])
        print('Password: {0}'.format(order[3]))
        worksheet.write('D{0}'.format(index),order[3])
        print('Role Id: {0}'.format(order[4]))
        worksheet.write('E{0}'.format(index),order[4])
        print('Created At: {0}'.format(order[5]))
        worksheet.write('F{0}'.format(index),order[5])
        print('Updated At: {0}'.format(order[6]))
        worksheet.write('G{0}'.format(index),order[6])
        
    workbook.close()
    # TODO: utilizar with e realizar tratativa de excecoes
    print('job executed!')

if __name__ == '__main__':
    # TODO: utilizar a lib nativa Argparser invés de pegar os.argv uma vez que ela já faz as 
    # tratativas
    main(sys.argv)
