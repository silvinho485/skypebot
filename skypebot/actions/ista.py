import os
import random
import tempfile

import requests


TEMPDIR = tempfile.gettempdir()
TEMP_WORDS_FILE = os.path.join(TEMPDIR, 'ista_words')


def ista():
    words = _read_words_from_cache()
    if not words:
        words = _get_words_from_web()

    return random.choice(words).upper()


def _get_words_from_web():
    URL = 'https://rhymit-3232c.firebaseio.com/v6/pt/termination/{page}/common.json'
    page = 'ista-1'
    words = []

    while page:
        json_response = requests.get(URL.format(page=page)).json()
        words += json_response['data'].split(', ')
        page = json_response.get('next', None)

    _save_words_in_cache(words)

    return words


def _save_words_in_cache(words):
    with open(TEMP_WORDS_FILE, 'w') as file:
        file.write('\n'.join(words))


def _read_words_from_cache():
    if not os.path.exists(TEMP_WORDS_FILE):
        return None

    with open(TEMP_WORDS_FILE, 'r') as file:
        words = file.read().splitlines()

    return words
