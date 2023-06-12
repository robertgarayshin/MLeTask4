import re

import requests
import telebot
from vosk import Model

import commander
import text_recognizer as recognizer
import punctuation_predictor as punc

model_ru = Model('./vosk-model-ru-0.42')
token = '6224666974:AAGP93-lNUHVpDpEtXMG_7DYPECZLYEiT00'
bot = telebot.TeleBot(token)
print('System started')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Hey! This bot can help you to transcribe voice messages into the text!')


@bot.message_handler(content_types=['voice', 'audio'])
def get_text_messages(message):
    try:
        # TODO: downloader.download(message)
        file_info = bot.get_file(message.voice.file_id)
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

        with open('voice.ogg', 'wb') as f:
            f.write(file.content)
        wavefile = commander.convert()

        transcript = recognizer.recognize(wavefile, model_ru)
        result = punc.predict_ru(transcript)
        commander.remove()
        bot.send_message(message.chat.id,
                         '\n'.join(line.strip() for line in re.findall(r'.{1,150}(?:\s+|$)', result)))
    except Exception as e:
        commander.remove()
        bot.send_message(message.from_user.id, 'Some error occurred while converting voice')
        print(e)


bot.polling(none_stop=True, interval=0)
