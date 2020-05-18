from asyncore import dispatcher
from itertools import chain
from os import name
import  cv2
import tele as tele
import telepot
#import updater as updater

#from telegram.ext import CommandHandler
#from telegram.ext import *
import re
import image
from nltk import interval_distance
from telepot.exception import TelegramError
import telebot
#import pyTelegramBotAPI
#from win32com.server import dispatcher

import newconstants
import detect_face_image
import detect_face_image2

import requests as requests
import config
import json
import pprint
import random
import telebot
import sys
import time
import telegram
import requests




#foto = 'https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g/sendphoto?chat_id=814781595&photo=AgADAgAD5KwxG-h1wUi3lPTs40-S9tCpwg8ABAEAAwIAA20AA_fjAgABFgQ'

#https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g/getUpdates

#po2 = 'https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g/sendphoto?chat_id=814781595&photo=AgADAgADhqwxG4E3yEjqZ7QE3IIZsaYiwQ4ABAEAAwIAA3gAA65MAQABFgQ'
URL = 'https://api.telegram.org/bot909185060:AAHMMywktcc18wD14yA-jFvJMnSi--S3x7g'


chat_id = '814781595'

foto = 'AAQCAAMEBAAC6HXBSFVC4Yyt3bbPC0HKDgAEAQAHbQADuTUAAhYE'
message1 = 'Hello world!'
message2 = 'This ChatBot was created for face detection which is a computer technology ' \
           'used in a variety of applications that identifies human faces in digital images.'
#mebot = 'https://core.telegram.org/file/811140327/1/zlN4goPTupk/9ff2f2f01c4bd1b013'
mebot = 'https://24gadget.ru/uploads/posts/2017-03/1490967481_biometric-samsung-galaxy-s8-005.png'

message3 = 'I am Bot!'
message4 = 'See youuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
message5 = 'Thank you for talking to me, bye bye.' \
           ' Obrigada por ter falado comigo, tchau tchau.' \
           ' Спасибо, что поговорили со мной, пока, пока.'
message6 = 'Barack Obama and Bill Gates'
message7 = '14:09'
message8 = 'João Lourenço and Vladimir Putin'
#Mygroup_id='-424267332'

group_id_site = 'https://web.telegram.org/#/im?p=s1201883098_18052776823377465520'


file_id ='AgADAgAD5KwxG-h1wUi3lPTs40-S9tCpwg8ABAEAAwIAA3kAA_XjAgABFgQ'

bot = telebot.TeleBot(newconstants.token)

site = 'https://web.telegram.org/#/im?p=g154513121'

test = bot.send_message(chat_id, message1)

print(bot)

test = bot.send_message(chat_id, 'Write hi')


@bot.message_handler(commands=['start'])
def handler_text(message):
    bot.send_photo(chat_id, mebot)
    bot.send_message(message.chat.id, message2)
    test = bot.send_message(chat_id, 'Write again hi')

@bot.message_handler(commands=['time'])
def handler_text(message):
    bot.send_photo(chat_id, mebot)
    bot.send_message(message.chat.id, message7)
    test = bot.send_message(chat_id, 'Write again hi')


@bot.message_handler(content_types=['text'])
def handler_text(message):
    print(message)
    if message.text == "hi":
        bot.send_message (chat_id, "hi, user")
        test = bot.send_message(chat_id, 'Write a/prin/b')

    elif message.text == "a":
        bot.send_message (chat_id, "Do you want to know about meBot????")
        test = bot.send_message(chat_id, 'Write yes/not')
    elif message.text == "yes":
        bot.send_message(chat_id, "cool, go start")
        test = bot.send_message(chat_id, 'Click in /start')

    elif message.text == "prin":
        bot.send_photo(chat_id,'https://www.google.com/imgres?imgurl=http%3A%2F%2Fwww.prin.ru%2Fimages%2Fnews%2Fprin%2F2019%2F10.17%2Fprin_multicanal.jpg&imgrefurl=http%3A%2F%2Fwww.prin.ru%2Fnews1%2Ftehpodderzhka_prin_stala_multikanalnoj%2F&tbnid=uCkXOGyOouVgeM&vet=10CHMQMyidAWoXChMIuO7tpOP45gIVAAAAAB0AAAAAEBE..i&docid=WJuT_3f3OZWEBM&w=853&h=400&itg=1&q=%D0%BF%D1%80%D0%B8%D0%BD&ved=0CHMQMyidAWoXChMIuO7tpOP45gIVAAAAAB0AAAAAEBE')
        test = bot.send_message(chat_id, 'Write again hi')
    elif message.text == "b":
        bot.send_photo(chat_id, 'https://image.cnbcfm.com/api/v1/image/104924313-obama-gates.jpg?v=1532563706&w=1400&h=950')

        bot.send_message(chat_id, "Would you like to know who they are????")
        test = bot.send_message(chat_id, 'Write y/n')

    elif message.text == "y":
        bot.send_photo(chat_id, open(detect_face_image.exportImage(), 'rb'))#chat_id,detect_face_image.exportImage())

        #im = bot.send_photo(chat_id, 'https://image.cnbcfm.com/api/v1/image/104924313-obama-gates.jpg?v=1532563706&w=1400&h=950')
       # bot.send_message(chat_id, "cool, go start")
        #test = bot.send_message(chat_id, '')
       # bot = telebot.TeleBot(detect_face_image.img)
       #  test = bot.send_message(chat_id, 'test.jpg')
       #cv2.imshow('img', img)
        bot.send_message(message.chat.id, message6)
        bot.send_message(chat_id, "Want to see more photo????")
        test = bot.send_message(chat_id, 'Write ye/no')
    #elif message.text == "n":
       # bot.send_photo(chat_id, open(detect_face_video.exportImage(), 'rb'))

    elif message.text == "ye":
        bot.send_photo(chat_id, open(detect_face_image2.exportImage(), 'rb'))
        bot.send_message(message.chat.id, message8)
        test = bot.send_message(chat_id, 'Write again hi')


    else:
        bot.send_message(chat_id, message5)

        #img = cv2.imread('test.jpg')


bot.polling(none_stop=True, interval=0)

