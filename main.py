# -*- coding: utf-8 -*-
import config
from SQLighter import SQLighter
import utils
import dictionary
import telebot

bot = telebot.TeleBot(config.token)

knownUsers = []

userStep = {}

commands = {
    'start': 'Для начала использования бота',
    'help': 'Посмотреть список команд',
}

""" Main Menu"""
@bot.message_handler(commands = ['start'])
def handle_main(message):
    markup = utils.main_keyboard(dictionary.mainpage_kb)
    result = bot.send_message(message.chat.id, "v 0.0.18a", reply_markup = markup )
    bot.register_next_step_handler(result, process_step)

def process_step(message):

    cid = message.chat.id
    button = message.text
    if button == dictionary.mainpage_kb[0][0]:
        bot.send_message(cid, "http://ramenskoye.ru")
        markup = utils.backkey()
        result = bot.send_message(message.chat.id, "Вернуться в главное меню?" ,reply_markup = markup )
        bot.register_next_step_handler(result, backkey_call)

    elif button == dictionary.mainpage_kb[1][0]:
        news_template = "10 июн 2017 В Раменском запущен новый бот для Telegram http://ramns.ru\n09 июн 2017 Расписание мероприятий на День города"
        # Here's request JSON-logic from ramns api
        bot.send_message(cid, news_template)

    elif button == dictionary.mainpage_kb[1][1]:
        events_template = "Афиша мероприятий:"
        bot.send_message(cid, events_template)

    elif button == dictionary.mainpage_kb[2][0]:
        shop_template = "Раздел предназначен для торговых объявлений"
        bot.send_message(cid, shop_template)

    elif button == dictionary.mainpage_kb[2][1]:
        useful_template = "Расписания, Информация, Контакты городских служб"
        bot.send_message(cid, useful_template)

    else:
        pass    

def backkey_call(message):
    markup = utils.main_keyboard(dictionary.mainpage_kb)
    result = bot.send_message(message.chat.id, "Главное меню" ,reply_markup = markup )

""" Хендлеры обработки команд и сообщений"""
@bot.message_handler(commands = ['help'])
def handle_help(message):
    bot.send_message(message.chat.id, dictionary.hello)

""" Тестирует связь с бд """
@bot.message_handler(commands = ['dbtest'])
def dbtest(message):
    db = SQLighter(config.database_name)
    categories_num = db.count_categories()
    db.close()
    result = "Соединение с базой успешно установлено.\nКоличество категорий в бд: %s " % categories_num
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands = ['info'])
def info(message):
    markup = utils.info_keyboard(dictionary.info_kb_keys)
    result = bot.send_message(message.chat.id, "Выберите интересующую вас информацию",  reply_markup = markup )
    bot.register_next_step_handler(result, process_step)




""" Эхо текст """
#@bot.message_handler(content_types = ['text'])
#def handle_echo_msg(message):
#    bot.send_message(message.chat.id, message.text)


""" Запуск цикла постоянного прослушивания """
if __name__=='__main__':
    bot.polling(none_stop = True)
    bot.polling(interval = 3)
