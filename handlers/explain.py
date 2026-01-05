from telegram import Update
from telegram.ext import ContextTypes
from ai.gpt import ask_gpt


async def explain(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not topic:
        await update.message.reply_text(
            "Напиши тему, которую нужно объяснить:\n"
            "/explain Производная функции"
        )
        return

    prompt = f"Объясни тему простыми словами для студента: {topic}. " \
             "Приведи пример и формулы, если нужно, кратко и понятно."

    response = ask_gpt(prompt)
    await update.message.reply_text(response)
