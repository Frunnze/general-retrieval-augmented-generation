from telegram import (
    Update, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)
from telegram.ext import ContextTypes

from ..requests.topics import get_topics


async def select_topic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    topics = get_topics()
    if not topics:
        await update.message.reply_text("No topics available.")
        return
    keyboard = [[InlineKeyboardButton(t, callback_data=t)] for t in topics]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Choose a topic:", reply_markup=reply_markup
    )
    context.user_data["chosen_topics"] = []


async def receive_topic_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    topic = query.data

    # Store chosen topic
    context.user_data["chosen_topics"].append(topic)

    # Get current keyboard and remove chosen topic
    keyboard = query.message.reply_markup.inline_keyboard
    new_keyboard = [btn for btn in keyboard if btn[0].callback_data != topic]
    reply_markup = InlineKeyboardMarkup(new_keyboard) if new_keyboard else None

    selected_topics = ", ".join(context.user_data["chosen_topics"])
    await query.edit_message_text(
        f"Selected topics so far: {selected_topics}",
        reply_markup=reply_markup
    )