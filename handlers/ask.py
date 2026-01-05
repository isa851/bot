from telegram import Update
from telegram.ext import ContextTypes
from ai.gpt import ask_gpt

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    action = context.user_data.get("action")

    if action:
        prompts = {
            "explain": f"Объясни тему простыми словами: {text}",
            "cheat": f"Сделай краткую шпаргалку по теме: {text}",
            "test": (
                f"Создай тест из 5 вопросов по теме: {text}. "
                "4 варианта ответа, в конце правильные."
            ),
            "essay": f"Напиши сочинение на тему: {text}. Стиль школьный/студенческий."
        }
        response = ask_gpt(prompts[action])
        context.user_data["action"] = None
    else:
        prompt = f"Ты AI-помощник для студента. Ответь на вопрос или задание:\n{text}"
        response = ask_gpt(prompt)

    await update.message.reply_text(response)
