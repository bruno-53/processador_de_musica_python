#IMPORTAR BIBLIOTECAS NECESSARIAS
from processador import processar_texto
from varrer_pagina_artista import varrer_pagina
import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

#PARAMETROS PARA INCLUSÃO E CONSULTA
artista = 'racionais-mc'
varrer_pagina(artista)
arquivo_link = open('links.txt','r',encoding="utf8").read()
links = arquivo_link.split()
contador = 0 #SE FOR COLOCAR EM UMA BASE DE DADOS JÁ EXISTENTE PREENCHER COM -1

#LOOP DE PROCESSAMENTO DE PALAVRAS NA LETRA
for musica in links:
    contador +=1
    link = "https://www.letras.mus.br"+musica
    if link.find('/album:') <= 0:
        album = link[(link.find("#")+7):-5].upper().replace("-"," ")
        ano = link[-4:len(link)]

        site = BeautifulSoup(requests.get(link).text, "html.parser")
        letra_processada = processar_texto(site.find('div', class_="cnt-letra").get_text(separator = " "))

        df = pd.DataFrame({

            "NOME_ARTISTA":site.find('title').get_text().split(sep =" - ")[1],
            "GENERO_MUSICA": site.find_all('span', itemprop="name")[1].get_text(),
            "NOME_MUSICA":site.find('title').get_text().split(sep =" - ")[0],
            "ALBUM":album,
            "ANO_ALBUM":ano,
            "QTD_PALAVRAS":(letra_processada[0].split(sep = ':'))[1],
            "PALAVRA_TOP_1":(letra_processada[1].split(sep = ':'))[0],
            "QTD_TOP_1":(letra_processada[1].split(sep = ':'))[1],
            "PALAVRA_TOP_2": (letra_processada[2].split(sep=':'))[0],
            "QTD_TOP_2": (letra_processada[2].split(sep=':'))[1],
            "PALAVRA_TOP_3": (letra_processada[3].split(sep=':'))[0],
            "QTD_TOP_3": (letra_processada[3].split(sep=':'))[1],
            "PALAVRA_TOP_4": (letra_processada[4].split(sep=':'))[0],
            "QTD_TOP_4": (letra_processada[4].split(sep=':'))[1],
            "PALAVRA_TOP_5": (letra_processada[5].split(sep=':'))[0],
            "QTD_TOP_5": (letra_processada[5].split(sep=':'))[1],
            "PALAVRA_TOP_6": (letra_processada[6].split(sep=':'))[0],
            "QTD_TOP_6": (letra_processada[6].split(sep=':'))[1],
            "PALAVRA_TOP_7": (letra_processada[7].split(sep=':'))[0],
            "QTD_TOP_7": (letra_processada[7].split(sep=':'))[1],
            "PALAVRA_TOP_8": (letra_processada[8].split(sep=':'))[0],
            "QTD_TOP_8": (letra_processada[8].split(sep=':'))[1],
            "PALAVRA_TOP_9": (letra_processada[9].split(sep=':'))[0],
            "QTD_TOP_9": (letra_processada[9].split(sep=':'))[1],
            "PALAVRA_TOP_10": (letra_processada[10].split(sep=':'))[0],
            "QTD_TOP_10": (letra_processada[10].split(sep=':'))[1],
            "LETRA_CRUA":site.find('div', class_="cnt-letra").get_text(separator = " "),
            "LINK":link
        }, index=[date.today().strftime('%d/%m/%Y')])

        df.index.name = "DATA_COLETA"

        #TESTE PARA VERIFICAR SE DEVE OU NÃO INCLUIR CABEÇALHO
        if contador == 1:
            df.to_csv('base_music.csv', mode='a', header=True, sep=';')
        else:
            df.to_csv('base_music.csv', mode='a', header=False, sep=';')
    else:
        contador -=1
        continue

print('{} novas músicas foram adicionadas ao arquivo base_music.csv!'.format(contador))
