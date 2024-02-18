import pandas as pd
from bs4 import BeautifulSoup
import requests


def pegar_dados(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    livros = soup.find_all('article', class_='product_pod')

    dados = []

    for livro in livros:
        item = {}
        item['Titulo'] = livro.find('img', class_='thumbnail').attrs['alt']
        item['Preco'] = livro.find('p', class_='price_color').text[1:]
        dados.append(item)
    return dados


def exportar_dados(dados):
    df = pd.DataFrame(dados)
    df.to_excel('livros.xlsx')
    df.to_csv('livros.csv')


if __name__ == '__main__':
    dados = pegar_dados('https://books.toscrape.com/')
    exportar_dados(dados)
    print('Feito.')
