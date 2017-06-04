# -*- coding: utf-8 -*-
import config
from SQLighter import SQLighter
import dictionary
import telebot

bot = telebot.TeleBot(config.token)

""" Хендлеры обработки команд и сообщений"""
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, dictionary.hello)

""" Тестирует связь с бд """
@bot.message_handler(commands=['dbtest'])
def dbtest(message):
    db = SQLighter(config.database_name)
    categories_num = db.count_categories()
    db.close()
    result = "Соединение с базой успешно установлено.\nКоличество категорий в бд: %s " % categories_num
    bot.send_message(message.chat.id, result)

""" Эхо текст """
@bot.message_handler(content_types=['text'])
def handle_echo_msg(message):
    bot.send_message(message.chat.id, message.text)


""" Запуск цикла постоянного прослушивания """
if __name__=='__main__':
    bot.polling(none_stop=True)
    bot.polling(interval=3)
