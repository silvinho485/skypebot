# based on https://github.com/vbuaraujo/hombre-cabron/blob/master/handler.py
import json
import os
import random
from unicodedata import normalize


MISERIBANK_DATA = "{}/rbcoinbank.json".format(os.path.dirname(__file__))
COIN_MIN_MINE = -1
COIN_MAX_MINE = 1
MAX_RAND_MINE = 50
PROBABILITY_OF_MINING = 1/MAX_RAND_MINE*100


def add(event):
    if random.randint(1, MAX_RAND_MINE) != 1 and event.msg.content != 'RB©OIN MISERAR':
        return
    person = event.msg.user.name.first
    name = _normalize_name(person)
    value = random.uniform(COIN_MIN_MINE, COIN_MAX_MINE)
    data = _load_miseribank_data()

    data[name] = data.get(name, 0) + value
    _save_miseribank_data(data)
    event.msg.chat.sendMsg("{}: {} MSR ({:+})".format(name, data[name], value))


def status(event):
    data = sorted(_load_miseribank_data().items(),
                  key=lambda item: (-item[1], item[0]))
    output_format = '{:12} |   {}\n'
    output = 'Ro Bot ©oin™\n'
    output += 'Probabilidade de minerar: {}%\n'.format(PROBABILITY_OF_MINING)
    for name, value in data:
        formatted_value = '{:f}'.format(value).rstrip('0').rstrip('.')
        output += output_format.format(name, formatted_value)

    event.msg.chat.sendMsg('{code}\n' + output + '{code}')


def _remove_diacritics(text):
    return ''.join(normalize('NFD', char)[0] for char in text)


def _normalize_name(text):
    return _remove_diacritics(text).title()


def _load_miseribank_data():
    with open(MISERIBANK_DATA, 'r') as f:
        return json.load(f)


def _save_miseribank_data(data):
    with open(MISERIBANK_DATA, 'w') as f:
        return json.dump(data, f)
