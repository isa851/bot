from telegram import Update
from telegram.ext import ContextTypes
from ai.gpt import ask_gpt


async def essay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args)

    if not topic:
        await update.message.reply_text(
            "Напиши тему эссе:\n/essay Моя любимая технология"
        )
        return

    prompt = (
        f"Напиши сочинение на тему: {topic}. "
        "Объем минимум 300 слов. "
        "Стиль школьный/студенческий, понятный и связный."
    )

    response = ask_gpt(prompt)
    await update.message.reply_text(response)
