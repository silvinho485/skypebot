# based on https://github.com/vbuaraujo/hombre-cabron/blob/master/handler.py
import json
import os
import random


MISERIBANK_DATA = "{}/rbcoinbank.json".format(os.path.dirname(__file__))
COIN_MIN_MINE = -0.1
COIN_MAX_MINE = 1


def coin(event):
    data = _load_miseribank_data()

    if random.randint(1, int(data['max_rand_mine'])) == 1:
        _mine(event, data)
    else:
        _increase_probability_of_mining(data)


def status(event):
    data = _load_miseribank_data()
    users = _get_users_sorted(data)

    output_format = '{:12} |   {}\n'
    output = 'Ro Bot ©oin™\n'
    output += 'Probabilidade de minerar: {}%\n\n'.format(_get_probability_of_mining(data))
    for name, value in users:
        formatted_value = '{:f}'.format(value).rstrip('0').rstrip('.')
        output += output_format.format(name, formatted_value)

    event.msg.chat.sendMsg('{code}\n' + output + '{code}')


def _get_probability_of_mining(data):
    max_rand_mine = int(data['max_rand_mine'])
    return round(1/max_rand_mine*100, 2)


def _load_miseribank_data():
    with open(MISERIBANK_DATA, 'r') as f:
        return json.load(f)


def _save_miseribank_data(data):
    with open(MISERIBANK_DATA, 'w') as f:
        return json.dump(data, f)


def _increase_probability_of_mining(data):
    data['max_rand_mine'] -= 1
    _save_miseribank_data(data)


def _get_users_sorted(data):
    return sorted(data['users'].items(),
                  key=lambda item: (-item[1], item[0]))


def _mine(event, data):
    name = '{} ({})'.format(event.msg.user.name.first, event.msg.userId)
    value = random.uniform(COIN_MIN_MINE, COIN_MAX_MINE)
    users = data['users']

    users[name] = users.get(name, 0) + value
    data['max_rand_mine'] = 100
    _save_miseribank_data(data)
    event.msg.chat.sendMsg("{}: {} RB© ({:+})".format(name, users[name], value))
