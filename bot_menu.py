import telebot
import os
import random
from telebot import types
# Getting Bot Token From Secrets
BOT_TOKEN = '6654572893:AAFDNNtyUqBA3DSVGxg9A6bPudpxJKsi9x0'
# Creating Telebot Object
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start'])
def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🔅 Рандомное число')
        key3 = types.KeyboardButton('➡️ Другое')
        markup.add(key1,key3)
        bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == '🔅 Рандомное число':
        bot.send_message(message.chat.id, 'Ваше число: ' + str(random.randint(0, 100000)))


    elif message.text == '➡️ Другое':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🤖 Полная инфа о боте')
        key2 = types.KeyboardButton('🐱 Хочу увидеть котиков')
        back = types.KeyboardButton('◀️ Назад')
        markup.add(key1,key2,back)
        bot.send_message(message.chat.id, '➡️ Другое'.format(message.from_user), reply_markup=markup)

    elif message.text == '🐱 Хочу увидеть котиков':
        cats = ['https://rabotatam.ru/uploads/monthly_2017_04/large.58f1bdeda1c5c_.jpg.91c33c120ad86a4dbf2c50dd44d00890.jpg', 
                'https://w.forfun.com/fetch/ef/ef5d5a59c4a4d9d1deb9a3722b744951.jpeg', 
                'https://chudo-prirody.com/uploads/posts/2021-08/1628905019_37-p-skachat-foto-milikh-kotikov-41.jpg',
                ]
        random_index = cats[random.randint(0, len(cats) - 1)]
        bot.send_message(message.chat.id, 'Ваш котик:')
        bot.send_photo(message.chat.id, random_index)
    
    elif message.text == '🤖 Полная инфа о боте':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🔅 Рандомное число')
        key3 = types.KeyboardButton('➡️ Другое')
        markup.add(key1,key3)
        bot.send_message(message.chat.id, '◀️ Назад\nМы еще не до писали функционал для этой кнопки.\nМы безграмотные)'.format(message.from_user), reply_markup=markup)
         
    
    elif message.text == '◀️ Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = types.KeyboardButton('🔅 Рандомное число')
        key3 = types.KeyboardButton('➡️ Другое')
        markup.add(key1,key3)
        bot.send_message(message.chat.id, '◀️ Назад'.format(message.from_user), reply_markup=markup)      



bot.polling()