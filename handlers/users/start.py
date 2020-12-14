from aiogram import types
from aiogram.types import ContentType, Message

from photos import *
from aiogram.types import InputFile
from keyboards.default.text_button import start_button, menu

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
import sqlite3



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try: 
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    
    photo = InputFile(path_or_bytesio="photos/photo1.jpg")
    await bot.send_photo(chat_id=message.from_user.id,
                        photo=photo,
                        caption=(f'Привет, {message.from_user.full_name}!\n\n'
                        f'Я твой финансовый бот-помошник 😊\n' 
                        f'Я могу помочь тебе получить деньги на самых выгодных условиях под 0%!\n'
                        f'Для этого мне нужно задать пару вопросов.\n\n'
                        f'Жми на кнопку «Запустить»👇'), reply_markup=start_button)


@dp.message_handler(Command("data"))
async def database(message: types.Message):
    count_users = db.count_users()[0]
    await message.answer(
        "\n".join([
            f'Привет, {message.from_user.full_name}!',
            'Ти есть в базе',
            f'В базе <b>{count_users}</b> Пользователей',
        ])
    )


@dp.message_handler(text="Запустить 🚀")
async def user_old(message: types.Message, state:FSMContext):
    await message.answer(f"Сколько вам лет ?\n"
                        f"Напиши свой возраст...")
    await state.set_state("years")


@dp.message_handler(state="years")
async def enter_old(message: types.Message, state: FSMContext):
    years = message.text
    db.update_user_age(age=years, id=message.from_user.id)

    photo = InputFile(path_or_bytesio='photos/photo2.jpg')
    await bot.send_photo(chat_id=message.from_user.id,
                        photo=photo,
                        caption=(f'Благодарю тебя, {message.from_user.full_name}!\n'
                         f'Чтобы подобрать банк, который готов дать тебе деньги\n'
                         f'на самых лучших условиях\n' 
                         f'воспользуйся кнопкой "🏪Подобрать банк"'
                         f'Тестови данние '), reply_markup=menu)
                    
    await state.finish()

@dp.message_handler(text="📝Мои настройки")
async def My_setting(message: Message):
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Страна: Україна\n"
                         f"Возраст: {user}")

