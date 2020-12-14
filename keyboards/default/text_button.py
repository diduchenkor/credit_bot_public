from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Запустить 🚀")
        ],
    ], 
    resize_keyboard=True, one_time_keyboard=True
)


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏪Подобрать банк"),
            KeyboardButton(text="👑Популяриные предложения")
        ],
        [
            KeyboardButton(text="📝Мои настройки")
        ],
        [
            KeyboardButton(text="🛸Поделиться с другом")
        ]
    ], 
    resize_keyboard=True
)