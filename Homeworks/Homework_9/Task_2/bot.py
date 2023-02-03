
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

updater = Updater('5752771563:AAFVhVnCzRbM2xu7nTl2BDD-f-WIZqZQXno')

updater.dispatcher.add_handler(CommandHandler("start", start_command))
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))

print('server start')
updater.start_polling()
updater.idle()