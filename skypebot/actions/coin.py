# based on https://github.com/vbuaraujo/hombre-cabron/blob/master/handler.py
import json
import os
import random
from unicodedata import normalize


MISERIBANK_DATA = "{}/rbcoinbank.json".format(os.path.dirname(__file__))
COIN_MIN_MINE = -1
COIN_MAX_MINE = 1


def add(event):
    data = _load_miseribank_data()
    max_rand_mine = data['max_rand_mine']
    if random.randint(1, int(max_rand_mine)) != 1 and event.msg.content != 'RB©OIN MISERAR':
        data['max_rand_mine'] -= 1
        _save_miseribank_data(data)
        return
    name = '{} ({})'.format(event.msg.user.name.first, event.msg.userId)
    value = random.uniform(COIN_MIN_MINE, COIN_MAX_MINE)
    users = data['users']

    users[name] = users.get(name, 0) + value
    data['max_rand_mine'] = 100
    _save_miseribank_data(data)
    event.msg.chat.sendMsg("{}: {} MSR ({:+})".format(name, users[name], value))


def status(event):
    data = _load_miseribank_data()
    users = sorted(_load_miseribank_data()['users'].items(),
                  key=lambda item: (-item[1], item[0]))
    output_format = '{:12} |   {}\n'
    output = 'Ro Bot ©oin™\n'
    output += 'Probabilidade de minerar: {}%\n'.format(_get_probability_of_mining(data))
    for name, value in users:
        formatted_value = '{:f}'.format(value).rstrip('0').rstrip('.')
        output += output_format.format(name, formatted_value)

    event.msg.chat.sendMsg('{code}\n' + output + '{code}')


def _get_probability_of_mining(data):
    max_rand_mine = data['max_rand_mine']
    return round(1/int(max_rand_mine)*100, 2)


def _load_miseribank_data():
    with open(MISERIBANK_DATA, 'r') as f:
        return json.load(f)


def _save_miseribank_data(data):
    with open(MISERIBANK_DATA, 'w') as f:
        return json.dump(data, f)
