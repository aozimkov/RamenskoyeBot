import config
import dictionary
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, dictionary.hello)

@bot.message_handler(content_types=['text'])
def handle_echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__=='__main__':
    bot.polling(none_stop=True)
    bot.polling(interval=3)
