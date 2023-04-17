from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler, CallbackContext, \
    ConversationHandler
from telegram import Update
from functions import *

conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start)
    ],
    states={
        'state_region':[
            CallbackQueryHandler(command_region)
        ],
       'state_tuman': [
           CallbackQueryHandler(command_tuman)
       ],
        'state_tugarak': [
            CallbackQueryHandler(command_tugarak)
        ],
        "kursga_yozilish":[
            CallbackQueryHandler(command_qabul)
        ],
        'state_name': [
            CallbackQueryHandler(command_back),
            MessageHandler(Filters.text, command_name)
        ],
        'state_phone': [
            MessageHandler(Filters.contact,command_contact)
        ]
    },
    fallbacks=[
        CommandHandler('start', start)
    ]
)
updater = Updater("5668235966:AAFhARqv2VikIaPkW3sEf8lVVhT9aZ-ZeOY")
updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
