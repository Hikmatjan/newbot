from Database import *
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
def all_regions_button():
    button = []
    # res bitta qatorni taxlaydi:
    res = []
    data = get_regions()
    for i in data:
        res.append(InlineKeyboardButton(text = i[1], callback_data=f'{i[0]}'))
        if len(res) == 3:
            button.append(res)
            res = []
    if len(res) > 0:
        button.append(res)
    return InlineKeyboardMarkup(button)
def tumans_byregion_button(region_id):
    button = []
    res = []
    data = get_tumans(region_id=region_id)
    print(data)
    for i in data:
        res.append(InlineKeyboardButton(i[1], callback_data=f'{i[0]}'))
        if len(res) == 3:
            button.append(res)
            res = []
    if len(res) > 0:
        button.append(res)
    button.append([InlineKeyboardButton("Orqaga", callback_data='back')])
    return InlineKeyboardMarkup(button)
def tugarak_bytuman_button(tuman_id):
    button = []
    res = []
    data = get_tugaraks(tuman_id)
    for i in data:
        res.append(InlineKeyboardButton(i[1], callback_data=f'{i[0]}'))
        if len(res) == 2:
            button.append(res)
            res = []
    if len(res) > 0:
        button.append(res)
    button.append([InlineKeyboardButton("Orqaga", callback_data='back')])
    return InlineKeyboardMarkup(button)


def tugarak_button():
    button = [
        [InlineKeyboardButton('to\'garakka yozilish', callback_data='bron')],
        [InlineKeyboardButton('Orqaga', callback_data='back')]
    ]
    return  InlineKeyboardMarkup(button)

def back_button():
    button = [
        [InlineKeyboardButton('Orqaga', callback_data='back')]
    ]
    return InlineKeyboardMarkup(button)


