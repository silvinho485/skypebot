import unicodedata

import requests
from bs4 import BeautifulSoup


def dict(word):
    word = _clean_word(word)
    url = f'https://www.dicio.com.br/{word}/'
    # print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')

    description_metatag = soup.find('meta', {'property': 'og:description'})
    description = description_metatag['content']

    result = description.split('Dicionário Online de Português. ')
    return result[1], url


def _clean_word(word):
    word = word.lower()
    word = _remove_accents(word)
    return word


def _remove_accents(word):
    return ''.join(char
                   for char in unicodedata.normalize('NFD', word)
                   if unicodedata.category(char) != 'Mn')
