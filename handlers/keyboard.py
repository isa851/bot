from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаём клавиатуру с одной кнопкой /start
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start")] 
    ],
    resize_keyboard=True 
)
