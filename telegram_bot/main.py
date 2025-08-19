from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler,
    MessageHandler,
    filters
)
import os
from dotenv import load_dotenv

from app.handlers.start import start
from app.handlers.add_topic import add_topic_conv_handler

load_dotenv()

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(add_topic_conv_handler)
    app.run_polling()