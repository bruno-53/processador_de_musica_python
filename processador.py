import unicodedata,string

# A função abaixo normaliza o texto e processa para trazer as palavras que mais aparecem no texto
# Na posição [0] esta a quantidade total de palavras e na 1 a palavra mais falada seguida da quantidade de vezes que ela
# Aparece
def processar_texto(texto):
    contador = {}
    resultado = []
    numeros = []
    texto_normalizado = unicodedata.normalize("NFD",texto).encode("ascii", "ignore").decode("utf-8").translate(str.maketrans('','',string.punctuation)).upper()
    lista_palavras = texto_normalizado.split()
    resultado.append('qtd_t:{}'.format(len(lista_palavras)))
    palavras_ignoradas = [
        'UM', 'SER', 'IR', 'ESTAR', 'TER', 'HAVER', 'FAZER', 'DAR', 'FICAR', 'PODER', 'VER', 'NAO', 'MAIS', 'MUITO',
        'JA','QUANDO', 'MESMO', 'DEPOIS', 'AINDA', 'DOIS', 'PRIMEIRO', 'CEM', 'MIL', 'A', 'O', 'UMA', 'DE', 'EM','PARA',
        'POR', 'COM', 'ATE', 'E', 'MAS', 'OU', 'TAMBEM', 'SE', 'ASSIM', 'COMO', 'PORQUE', 'QUE', 'EU', 'VOCE', 'ELE',
        'ESTE','ESSE', 'ISSO', 'SUA', 'AI', 'AH', 'AU', 'UI', 'HUM', ';', '.', ',','DO','AS','AO','DA','DAS','OS',
        'NO','ELA','NA']
    top = 0
    for palavra in lista_palavras:
        if (palavra not in contador) and (palavra not in palavras_ignoradas):
            contador[palavra] = 1
            if palavra.isdigit():
                numeros.append(palavra)
        elif palavra not in palavras_ignoradas:
            contador[palavra] +=1
    for palavra in sorted(contador,key=contador.get,reverse=True):
        top += 1
        if top <= 10:
            resultado.append('{}:{}'.format(palavra,contador[palavra]))
    return resultado

