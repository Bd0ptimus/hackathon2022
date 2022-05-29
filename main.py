from pickle import FALSE
import telebot
import os
import voice_recog
import soundfile as sf
import ffmpeg
import config
import find_topics
import codecs

from telebot import types 
#from pydub import AudioSegment


TOKEN = str(config.Config().telegram_token())
API_KEY = os.getenv(TOKEN)

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands = ['test'])
def test(message):
    bot.reply_to(message, "123")

'''
@bot.message_handler(commands = ['hello'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    button1 = types.KeyboardButton("Post it somewhere")
    markup.add(button1)
    bot.send_message(message.chat.id, "Hello", reply_markup = markup)
'''

#write text in txt
def write_file(string):
    with codecs.open("SMMOperatorInterFace/bin/Debug/net6.0-windows/customer_input.txt", "a", "utf-8") as stream:   # or utf-8
        stream.write(string)

#Prepare for voice
@bot.message_handler(content_types=['voice', 'text'])
def voice_processing(message):
    if message.content_type == 'voice':
        print('voice!')
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('voice_store/voice.ogg','wb') as new_file:
            new_file.write(downloaded_file)
        voice_recog.store_voice_file()
        text_result = voice_recog.yandex_voice_recognition()
        bot.send_message(message.chat.id, "#от_заказчика\n"+ text_result )
        #print("Go to prepare for searching")
        #find_topics.prepare_data_for_searching(text_result)
        write_file("\n\n"
        + text_result)

    else:
        print('text!')
    
    
    

bot.polling()