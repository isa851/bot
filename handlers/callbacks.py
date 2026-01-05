from telegram import Update
from telegram.ext import ContextTypes
from ai.gpt import ask_gpt


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    action = query.data
    context.user_data["action"] = action

    messages = {
        "explain": "Напиши тему, которую нужно объяснить",
        "cheat": "Напиши тему для шпаргалки",
        "test": "Напиши тему для теста",
        "essay": "Напиши тему эссе",
    }

    await query.message.reply_text(messages[action])
