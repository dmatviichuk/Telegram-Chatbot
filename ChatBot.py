import apiai
import logging
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi!')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def echo(update, context):
    request = apiai.ApiAI('a063ee88a1944a4ea121d68f2d6fc626').text_request()
    request.lang = 'en'
    request.session_id = 'AIBot'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        update.message.reply_text(reply_text=update.message.reply_text, text=response)
    else:
        update.message.reply_text(reply_text=update.message.reply_text, text='I don`t understand you!')


def main():
    updater = Updater("1031290417:AAEESoh8Gw1YrXnWB1DtDn_3HZ4j2nEq26I", use_context=True)
    dp = updater.dispatcher
    start_command_handler = CommandHandler('start', start)
    text_message_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(start_command_handler)
    dp.add_handler(text_message_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
