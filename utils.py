# -*- coding: utf-8 -*-

from telebot import types

def info_keyboard(info_kb_keys):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)

    for item in info_kb_keys:
        markup.add(item)

    return markup




