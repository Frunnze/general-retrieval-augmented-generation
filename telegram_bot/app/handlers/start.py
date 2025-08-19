from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from .main_keyboard import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=main_keyboard,
            resize_keyboard=True
        )
    )