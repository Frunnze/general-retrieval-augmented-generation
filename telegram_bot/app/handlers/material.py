from telegram import (
    Update, 
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ContextTypes, 
    ConversationHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
import os

from ..requests.topics import get_topics
from ..requests.material import upload_pdf


SAVE_CHOSEN_TOPIC, UPLOAD_MATERIAL = 1, 2

async def ask_to_choose_topic_for_material(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    topics = get_topics()
    if not topics:
        await update.message.reply_text("No topics available!")
        return
    keyboard = [[InlineKeyboardButton(t, callback_data=t)] for t in topics]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Choose a topic:",
        reply_markup=reply_markup
    )
    return SAVE_CHOSEN_TOPIC


async def save_chosen_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    topic = query.data
    context.user_data["upload_topic"] = topic
    await query.edit_message_text(f"Selected topic: {topic}. Now, upload a PDF.")
    return UPLOAD_MATERIAL


async def upload_material(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.document:
        document = update.message.document
        if document.mime_type == "application/pdf":
            file = await context.bot.get_file(document.file_id)
            tmp_dir = "./tmp"
            os.makedirs(tmp_dir, exist_ok=True)
            file_path = f"{tmp_dir}/{document.file_name}"
            await file.download_to_drive(file_path)
            await update.message.reply_text("PDF downloaded")
            upload_pdf(file_path, context.user_data["upload_topic"])
            if os.path.exists(file_path):
                os.remove(file_path)
        else:
            await update.message.reply_text("Upload a PDF file")
    else:
        await update.message.reply_text("Upload a PDF file!")
    return ConversationHandler.END


upload_material_conv_handler = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Text("Add material"), 
            ask_to_choose_topic_for_material
        )
    ],
    states={
        SAVE_CHOSEN_TOPIC: [
            CallbackQueryHandler(save_chosen_topic),
        ],
        UPLOAD_MATERIAL: [
            MessageHandler(filters.Document.PDF, upload_material)
        ]
    },
    fallbacks=[]
)