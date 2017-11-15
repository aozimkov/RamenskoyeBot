# -*- coding: utf-8 -*-

from telebot import types

def backkey():

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    markup.add('Меню')

    return markup


def main_keyboard(kbkeys):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)

    for row in kbkeys:
        markup.row(*row)



    return markup


def info_keyboard(info_kb_keys):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)

    for item in info_kb_keys:
        markup.add(item)

    return markup




