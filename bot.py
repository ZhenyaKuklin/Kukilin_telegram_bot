#1 Импорт библиотек

import logging

import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

#2 инициализация объектов


TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


#3 Обработка команды старт


@dp.message(Command(commands=['start']))
async def procces_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


#4 Обработка команды старт
@dp.message(Command(commands=['help']))
async def procces_command_help(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'С чем тебе нужна помощь?'
    logging.info(f'{user_name} {user_id} обратился за помощью')
    await message.answer(text=text)

#5 Обработка все сообщений
@dp.message()
async def send_first(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=text)


#6 Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)