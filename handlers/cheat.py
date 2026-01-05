from telegram import Update
from telegram.ext import ContextTypes
from ai.gpt import ask_gpt


async def cheat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args)

    if not topic:
        await update.message.reply_text(
            "Напиши тему:\n/cheat Законы Ньютона"
        )
        return

    prompt = (
        f"Сделай краткую шпаргалку для студента по теме: {topic}. "
        "Используй пункты, формулы и примеры. Максимально кратко."
    )

    response = ask_gpt(prompt)
    await update.message.reply_text(response)
