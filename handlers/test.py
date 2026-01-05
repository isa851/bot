from telegram import Update
from telegram.ext import ContextTypes
from ai.gpt import ask_gpt


async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    action = context.user_data.get("action")
    text = update.message.text

    if not action:
        await update.message.reply_text("Нажми кнопку из меню 👇")
        return

    prompts = {
        "explain": f"Объясни тему простыми словами: {text}",
        "cheat": f"Сделай краткую шпаргалку по теме: {text}",
        "test": (
            f"Создай тест из 5 вопросов по теме: {text}. "
            "4 варианта ответа, в конце правильные."
        ),
        "essay": (
            f"Напиши сочинение на тему: {text}. "
            "Подходит для школы или колледжа."
        ),
    }

    response = ask_gpt(prompts[action])
    await update.message.reply_text(response)

    context.user_data["action"] = None
