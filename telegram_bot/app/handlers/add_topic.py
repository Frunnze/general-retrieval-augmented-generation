from telegram import Update
from telegram.ext import (
    ContextTypes, 
    ConversationHandler,
    MessageHandler,
    filters
)

from ..requests.topics import add_topic_name


TOPIC_NAME = 1

async def add_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> 1:
    await update.message.reply_text("What is the topic name?")
    return TOPIC_NAME


async def receive_topic_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    topic_name = update.message.text
    add_topic_name(topic_name)
    await update.message.reply_text(f"Topic name '{topic_name}' was added!")


add_topic_conv_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Text("Add topic"), add_topic)],
    states={
        TOPIC_NAME: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND, 
                receive_topic_name
            )
        ]
    },
    fallbacks=[]
)