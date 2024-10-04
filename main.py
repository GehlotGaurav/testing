import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = '7744724902:AAHZ4xsKvqBqtCoh5tJpE5W-oezL4aXoxp8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I can delete all media and stickers in this group.')

async def delete_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    offset = 0
    while True:
        messages = await context.bot.get_history(chat_id=chat_id, offset=offset)
        if not messages:
            break
        for message in messages:
            if message.sticker or message.photo or message.video or message.document:
                await context.bot.delete_message(chat_id=chat_id, message_id=message.message_id)
        offset += len(messages)

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('delete_media', delete_media))

    application.run_polling()

if __name__ == '__main__':
    main()
