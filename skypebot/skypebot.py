import re

from actions import cama
from actions import fujam
from actions import hola
from actions.dict import dict
from actions.ista import ista
from actions.ponto import ponto


KEYWORDS = {
    'help': ('@ro help', '<at id="8:live:976d89d0eaa03977">Ro</at> help'),
    'fujam': ('fujam', '#fujam', 'fujam para as colinas'),
    'commit': ('#commit',),
    'hola': ('#hola',),
}


def handle(event):
    message = event.msg.content.lower()

    keywords_mapping = (
        (_ponto, message.startswith('ponto')),
        (_ista, message.endswith('ista')),
        (_pregunton, message.endswith('???')),
        (_radical, 'é disso que eu gosto' in message),
        (_radical, 'é disso q eu gosto' in message),
        (_piorou, 'tava ruim' in message),
        (_piorou, 'tava meio ruim' in message),
        (_dict, '#dict' in message),
        (_help, message in KEYWORDS['help']),
        (_fujam, message in KEYWORDS['fujam']),
        (_commit, message in KEYWORDS['commit']),
        (_hola, message in KEYWORDS['hola']),
    )

    for function, match in keywords_mapping:
        if match:
            event.msg.chat.setTyping()
            function(event)
            break


def _radical(event):
    event.msg.chat.sendMsg('RADICAAAAL!!!')


def _help(event):
    help = """
    - ? - Amigo pregunton (mariachilove)
    - #commit - #CAMA
    - #hola - Hola
    - ponto {chegada} {?saida_intervalo},{volta_intervalo?} {?horas a trabalhar?} - ponto
    - #ista - ista
    """
    event.msg.chat.sendMsg(help)


def _ista(event):
    event.msg.chat.sendMsg(ista())


def _fujam(event):
    event.msg.chat.sendMsg(fujam.switch_two())


def _piorou(event):
    event.msg.chat.sendMsg('agora parece q piorou')


def _pregunton(event):
    event.msg.chat.sendMsg('AAAAAAAAH QUE AMIGO TAN PREGUNTON!!!')
    event.msg.chat.sendMsg('(mariachilove)')


def _commit(event):
    cama.main(event.msg.chat.sendMsg)


def _hola(event):
    event.msg.chat.sendMsg(hola.main())


def _ponto(event):
    params = event.msg.content.split(' ')
    horario = params[1]
    rest_hours = params[2] if len(params) > 2 else '1:00'
    working = params[3] if len(params) > 3 else '8:30'
    event.msg.chat.sendMsg(ponto(horario, working, rest_hours))


def _dict(event):
    regex_pattern = '</legacyquote>([a-záàâãéèêíïóôõöúç]*)<legacyquote>'
    msg = event.msg.content.lower()

    word = re.findall(regex_pattern, msg)[0]
    try:
        event.msg.chat.sendMsg('{}\n{}'.format(*dict(word)))
    except IndexError:
        event.msg.chat.sendMsg('Não achei essa palavra: {}'.format(word))
