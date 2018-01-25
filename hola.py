#!/bin/python3
import calendar
import time
import random
from datetime import datetime
calendar.setfirstweekday(calendar.SUNDAY)

now = datetime.now()
week_day = ""

def greetings():
    phrases= ["Hola ¿que tal?",
              "Buenos dias/tardes",
              "Buenas",
              "Hola hombre",
              "Konnichiha Vitor-san",]
    return random.choice(phrases)

def before_day():
    phrases = ["como esta en este",
               "espero que tenga un excelente",
               "que le parece este",
               "hoy es",
    ]
    return random.choice(phrases)

def weekday(day):
    mydict = {0:'lunes',
              1:'martes',
              2:'miercoles',
              3:'jueves',
              4:'viernes'}
    return mydict[day]

def joke(day):
    if day == 'jueves':
        habla = "Hoy es dia de conbeber jeje"
    elif day == 'viernes':
        habla = "hoy es viernes e el cuerpo lo sabe :D"
    else:
        phrases= ["¿Mucho frio/calor ahi?",
                  "Aquí Faro es el amo. :D",
                  "¿Como esta el tiempo ahi?",
                  "Aca sigue caliente como siempre :/"
        ]
        habla = random.choice(phrases)
    return habla

def main():
    weekd = weekday(calendar.weekday(now.year, now.month, now.day))
    msg = "{}. {} {}. {}".format(greetings(), before_day(), weekd, joke(weekd))
    return msg
