from telegram.ext.updater import Updater
from telegram .update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater(
    'APITOKEN', use_context=True)


def begin(update: Update, context: CallbackContext):
    update.message.reply_text('hi this is my first bot! created by Milad')


def help(update: Update, context: CallbackContext):
    update.message.reply_text('''available commands:
    help
    linkedin - to get linkedin profile url
    gmail - to get gmail adress
    START''')


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text('abd.milad@gmail.com')


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text('www.linkedin.com/in/milad-abdollahi420')


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('START', begin))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

updater.start_polling()

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
