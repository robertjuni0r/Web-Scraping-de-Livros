import pandas as pd
from bs4 import BeautifulSoup
import requests


def pegar_dados(url):
    response = requests.get(url)

    # Utiliza para fazer a analise e retorno em formato de texto
    soup = BeautifulSoup(response.text, 'lxml')

    # Retorna uma lista com toda as informações sobre o livro, pesquisando em todas as article class='product_pod'
    livros = soup.find_all('article', class_='product_pod')

    dados = []

    # Localizar informacoes especificas na pagina, cada livro conta como um dado
    for livro in livros:
        item = {}
        # Procura imagens dentro do article, e retorna o alt para armazenar como titulo
        item['Titulo'] = livro.find('img', class_='thumbnail').attrs['alt']
        # Procura valor do livro, e pula o primeiro caractere para nao pegar cifrao
        item['Preco'] = livro.find('p', class_='price_color').text[1:]

        # Adiciona o dado a lista de dados
        dados.append(item)

    return dados


"""def proxima_pagina():

    for numero_pagina in range (1,51):

        url = f'https://books.toscrape.com/catalogue/page-{numero_pagina}.html'
        response = requests.get(url)

    return pagina"""


def exportar_dados(dados):
    df = pd.DataFrame(dados)
    df.to_excel('livros.xlsx')
    df.to_csv('livros.csv')


if __name__ == '__main__':
    dados = pegar_dados('https://books.toscrape.com/')
    exportar_dados(dados)
    print('Feito.')
