from time import sleep

from decouple import config
from skpy import SkypeEventLoop, SkypeNewMessageEvent

import Calendar
import CommitJoke
import fujam
from ista import ista
from ponto import ponto


class SkypePing(SkypeEventLoop):
    def __init__(self, username, password):
        super(SkypePing, self).__init__(username, password)

    def onEvent(self, event):
        try:
            if not isinstance(event, SkypeNewMessageEvent):
                return
            msg = event.msg.content.lower()
            print(msg)

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
                CommitJoke.main(event.msg.chat.sendMsg)
            elif msg == '#hola':
                event.msg.chat.setTyping()
                event.msg.chat.sendMsg(Calendar.main())
            elif msg.startswith('ponto'):
                event.msg.chat.setTyping()
                params = event.msg.content.split(' ')
                horario = params[1] if len(params) > 1 else '8:30'
                rest_hours = params[2] if len(params) > 2 else '1:00'
                working = params[3] if len(params) > 3 else '8:30'
                event.msg.chat.sendMsg(ponto(horario, working, rest_hours))
        except Exception as e:
            print(e)
            event.msg.chat.setTyping()
            sleep(5)
            event.msg.chat.sendMsg('PAREM DE TENTAR ME MATAR!!!11!!ONZE!!')


if __name__ == '__main__':
    SKYPE_LOGIN = config('SKYPE_LOGIN')
    SKYPE_PASSWORD = config('SKYPE_PASSWORD')

    sk = SkypePing(SKYPE_LOGIN, SKYPE_PASSWORD)
    sk.setPresence()
    sk.loop()
