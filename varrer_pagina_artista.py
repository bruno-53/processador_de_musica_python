import requests
from bs4 import BeautifulSoup

# A função abaixo varre a pagina de discografia do artista e traz todos os links associados a ela

def varrer_pagina(artista):
    contador = 0
    url = 'https://www.letras.mus.br/{}/discografia/'.format(artista)

    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        play_song_elements = soup.find_all(class_='bt-play-song')
        links = [element['href'] for element in play_song_elements]

        with open('links.txt', 'w') as file:
            for link in links:
                contador +=1
                file.write(link + '\n')

        print('{} links foram salvos em links.txt!'.format(contador))
    else:
        print('Falha ao acessar a página:', response.status_code)
