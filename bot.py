from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
from config import BOT_TOKEN
from ai.gpt import ask_gpt
from handlers.cheat import cheat
from handlers.test import test
from handlers.menu import show_menu
from handlers.callbacks import handle_callback
from handlers.test import test
from handlers.explain import explain
from handlers.essay import essay
from handlers.ask import ask
from telegram.ext import MessageHandler, filters



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я AI-ассистент для студентов.\n\n"
        "Команды:\n"
        "/explain — объяснить тему\n"
        "/cheat — сделать шпаргалку\n"
        "/test — создать тест\n"
        "/essay — помочь с эссе"
    )
    await show_menu(update, context)  


async def explain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = " ".join(context.args)
    if not topic:
        await update.message.reply_text("Напиши тему: /explain производная")
        return

    response = await ask_gpt(f"Объясни тему простыми словами: {topic}")
    await update.message.reply_text(response)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("explain", explain))
app.add_handler(CommandHandler("test", test))
app.add_handler(CommandHandler("cheat", cheat))
app.add_handler(CommandHandler("essay", essay))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ask))


app.add_handler(CallbackQueryHandler(handle_callback))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, test))

print("Бот запущен")
app.run_polling()
