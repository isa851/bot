from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Объяснить тему", callback_data="explain")],
        [InlineKeyboardButton("Шпаргалка", callback_data="cheat")],
        [InlineKeyboardButton("Тест", callback_data="test")],
        [InlineKeyboardButton("Эссе", callback_data="essay")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выбери, чем я могу помочь:",
        reply_markup=reply_markup
    )
