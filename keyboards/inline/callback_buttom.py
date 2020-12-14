from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

#Поделится с другом
send_bot = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Поделиться ботом👍🏼", switch_inline_query=f"\n"
                                                                            f"https://t.me/money_zaim_bot\n"
                                                                             f"Смотри какой крутой бот 😊")
    ]
])

show_search = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍Показать результат поиска ",  callback_data="show_credit")
    ]
])

popular_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Под 0%",  callback_data="crediplus")
    ],
    [
        InlineKeyboardButton(text="С плохой кредитной историей",  callback_data="gotivochka3")
    ],
    [
        InlineKeyboardButton(text="Лучшие займы",  callback_data="next_variant")
    ],
    [
        InlineKeyboardButton(text="Все варианты",  callback_data="give_next")
    ]
])


#______________________менюшка для кредитив____________---

first_klick = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить деньги",  url="https://rozetka.com.ua/")
    ],
    [
        InlineKeyboardButton(text="Еще варианты",  callback_data="give_next")
    ],
    
])

second_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить деньги",  url="https://rozetka.com.ua/")
    ],
    [
        InlineKeyboardButton(text="Назад",  callback_data="show_credit"),
        InlineKeyboardButton(text="Еще варианты",  callback_data="next_variant")
    ],
    
])

there_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить деньги",  url="https://rozetka.com.ua/")
    ],
    [
        InlineKeyboardButton(text="Назад",  callback_data="give_next"),
        InlineKeyboardButton(text="Еще варианты",  callback_data="gotivochka3")
    ],
    
])

foo_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить деньги",  url="https://rozetka.com.ua/")
    ],
    [
        InlineKeyboardButton(text="Назад",  callback_data="next_variant"),
        InlineKeyboardButton(text="Еще варианты",  callback_data="crediplus")
    ],
    
])

five_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить деньги",  url="https://rozetka.com.ua/")
    ],
    [
        InlineKeyboardButton(text="Назад",  callback_data="gotivochka3"),
        InlineKeyboardButton(text="Еще варианты",  callback_data="evrogroshi")
    ],
    
])

six_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить деньги",  url="https://rozetka.com.ua/")
    ],
    [
        InlineKeyboardButton(text="Назад",  callback_data="crediplus"),
        InlineKeyboardButton(text="Еще варианты",  callback_data="zeccredit")
    ],
    
])

seven_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить деньги",  url="https://rozetka.com.ua/")
    ],
    [
        InlineKeyboardButton(text="Назад",  callback_data="crediplus"),
        InlineKeyboardButton(text="Еще варианты",  callback_data="done")
    ],
    
])

