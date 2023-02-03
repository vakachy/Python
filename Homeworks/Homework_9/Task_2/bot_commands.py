from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time
from spy import *

def start_command(update: Update, context: CallbackContext):
    """Sends greeting from the bot to the user."""
    update.message.reply_text(
        f"Hi,{update.effective_user.first_name}!\nI'm Botty!\nUse /help to see what I can do...")

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Hi, {update.effective_user.first_name}!\nWhat's up!")

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"/hi -- greeting from Botty\n\
/time -- get to know your date & local time\n\
/help -- list of commands")

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Today's date & current time:\n{time.ctime()}")
