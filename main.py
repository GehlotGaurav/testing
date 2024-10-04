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
        try:
            updates = await context.bot.get_updates(offset=offset)
            if not updates:
                break
            for update in updates:
                if update.message and (update.message.sticker or update.message.photo or update.message.video or update.message.document):
                    print(f"Trying to delete message ID {update.message.message_id}")
                    await context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
            offset += len(updates)
        except Exception as e:
            print(f"Error: {e}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('delete_media', delete_media))

    application.run_polling()

if __name__ == '__main__':
    main()
