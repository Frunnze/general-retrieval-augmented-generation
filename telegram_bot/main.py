from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
import os
from dotenv import load_dotenv

from app.handlers.start import start
from app.handlers.add_topic import add_topic_conv_handler
from app.handlers.select_chat_topics import select_topic, receive_topic_choice

load_dotenv()

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text("Select chat topics"), select_topic))
    app.add_handler(CallbackQueryHandler(receive_topic_choice))
    app.add_handler(add_topic_conv_handler)
    app.run_polling()