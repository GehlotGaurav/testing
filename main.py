import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

logging.basicConfig(level=logging.INFO)

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I can delete all media and stickers in this group.')

def delete_media(update, context):
    chat_id = update.effective_chat.id
    offset = 0
    while True:
        messages = context.bot.get_history(chat_id=chat_id, offset=offset)
        if not messages:
            break
        for message in messages:
            if message.sticker or message.photo or message.video or message.document:
                context.bot.delete_message(chat_id=chat_id, message_id=message.message_id)
        offset += len(messages)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('delete_media', delete_media))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
