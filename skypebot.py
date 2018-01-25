import commit_joke
import fujam
import hola
from ista import ista
from ponto import ponto


def handle(event):
    msg = event.msg.content.lower()

    if msg == '@ro help' or msg == '<at id="8:live:976d89d0eaa03977">Ro</at> help':
        event.msg.chat.setTyping()
        help = """
        - ? - Amigo pregunton (mariachilove)
        - #commit - #CAMA
        - #hola - Hola
        - ponto {chegada} {?saida_intervalo},{volta_intervalo?} {?horas a trabalhar?} - ponto
        - #ista - ista
        """
        event.msg.chat.sendMsg(help)
    elif msg[-4:] == 'ista' and event.msg.userId != 'live:976d89d0eaa03977':
        event.msg.chat.setTyping()
        event.msg.chat.sendMsg(ista())
    elif msg in ('fujam', '#fujam', 'fujam para as colinas'):
        event.msg.chat.setTyping()
        event.msg.chat.sendMsg(fujam.switch_two())
    elif msg == '?':
        event.msg.chat.setTyping()
        event.msg.chat.sendMsg('AAAAAAAAH QUE AMIGO TAN PREGUNTON!!!')
        event.msg.chat.sendMsg('(mariachilove)')
    elif msg == '#commit':
        event.msg.chat.setTyping()
        commit_joke.main(event.msg.chat.sendMsg)
    elif msg == '#hola':
        event.msg.chat.setTyping()
        event.msg.chat.sendMsg(hola.main())
    elif msg.startswith('ponto'):
        event.msg.chat.setTyping()
        params = event.msg.content.split(' ')
        horario = params[1] if len(params) > 1 else '8:30'
        rest_hours = params[2] if len(params) > 2 else '1:00'
        working = params[3] if len(params) > 3 else '8:30'
        event.msg.chat.sendMsg(ponto(horario, working, rest_hours))
