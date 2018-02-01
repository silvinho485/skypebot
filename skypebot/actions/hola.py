import calendar
import random
from datetime import datetime


def greetings():
    return random.choice([
        "Hola ¿que tal?",
        "Buenos dias/tardes",
        "Buenas",
        "Hola hombre",
        "Konnichiha Vitor-san",
    ])


def before_day():
    return random.choice([
        "como esta en este",
        "espero que tenga un excelente",
        "que le parece este",
        "hoy es",
    ])


def weekday(day):
    return {
        0: 'lunes',
        1: 'martes',
        2: 'miercoles',
        3: 'jueves',
        4: 'viernes',
    }[day]


def joke(day):
    if day == 'jueves':
        habla = "Hoy es dia de conbeber jeje"
    elif day == 'viernes':
        habla = "hoy es viernes e el cuerpo lo sabe :D"
    else:
        phrases = [
            "¿Mucho frio/calor ahi?",
            "Aquí Faro es el amo. :D",
            "¿Como esta el tiempo ahi?",
            "Aca sigue caliente como siempre :/",
        ]
        habla = random.choice(phrases)
    return habla


def main():
    calendar.setfirstweekday(calendar.SUNDAY)
    now = datetime.now()

    weekd = weekday(calendar.weekday(now.year, now.month, now.day))
    msg = "{}. {} {}. {}".format(greetings(), before_day(), weekd, joke(weekd))
    return msg
