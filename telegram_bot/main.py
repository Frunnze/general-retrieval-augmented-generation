from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler
)
import os
from dotenv import load_dotenv

from handlers.start import start

load_dotenv()

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()