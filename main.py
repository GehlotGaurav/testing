from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = '7744724902:AAHZ4xsKvqBqtCoh5tJpE5W-oezL4aXoxp8'

def delete_media_and_stickers(update, context):
    chat_id = update.effective_chat.id
    for message in context.bot.get_chat_history(chat_id):
        if message.photo or message.video or message.audio or message.document or message.sticker:
            context.bot.delete_message(chat_id, message.message_id)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('delete_media_and_stickers', delete_media_and_stickers))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
