import importlib

from decouple import config
from skpy import SkypeEventLoop, SkypeNewMessageEvent

import skypebot


class SkypePing(SkypeEventLoop):
    def __init__(self, username, password):
        super(SkypePing, self).__init__(username, password)

    def onEvent(self, event):
        try:
            if not isinstance(event, SkypeNewMessageEvent):
                return
            if event.msg.userId == self.userId:
                return

            msg = event.msg.content.lower()
            print(msg)

            importlib.reload(skypebot)
            skypebot.handle(event)

        except Exception as e:
            print(e)
            print('PAREM DE TENTAR ME MATAR!!!11!!ONZE!!')


if __name__ == '__main__':
    SKYPE_LOGIN = config('SKYPE_LOGIN')
    SKYPE_PASSWORD = config('SKYPE_PASSWORD')

    sk = SkypePing(SKYPE_LOGIN, SKYPE_PASSWORD)
    sk.setPresence()
    sk.loop()
