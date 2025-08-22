from telegram import Update
from telegram.ext import ContextTypes

from ..requests.ai import get_ai_res


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_msg = update.message.text
    topics = context.user_data["chosen_topics"]
    res = get_ai_res(
        topics=topics,
        user_msg=user_msg,
        conv_hist=None
    )
    topics_str = ", ".join(topics)
    await update.message.reply_text(
        text=f"{res} \n\nConsidered topics: {topics_str}"
    )