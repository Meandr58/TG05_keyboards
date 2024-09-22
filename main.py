import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
import keyboard as kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!', reply_markup=kb.keyboard_main)

@dp.message(F.text == "Привет!")
async def hello_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока!")
async def bye_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}!')

@dp.message(Command("links"))
async def links(message: Message):
    await message.answer(f'Что хотите выбрать?', reply_markup=kb.inline_keyboard_test)

@dp.message(Command("builder"))
async def builder(message: Message):
    await message.answer("А это билдер!", reply_markup=await kb.builder_keyboard())

@dp.message(Command("dynamic"))
async def dynamic(message: Message):
    await message.answer("Динамическая клавиатура:", reply_markup=await kb.dynamic_keyboard())

# Обработчик callback_data "show_more", который заменяет кнопку на две новые
@dp.callback_query(F.data == "show_more")
async def show_more(callback: CallbackQuery):
    await callback.message.edit_text("Выберите опцию:", reply_markup=await kb.more_options_keyboard())

# Обработчик для кнопки "Опция 1"
@dp.callback_query(F.data == "option_1")
async def option_1(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 1")

# Обработчик для кнопки "Опция 2"
@dp.callback_query(F.data == "option_2")
async def option_2(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали Опцию 2")



@dp.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer("Этот бот выполняет команды:\n/start\n/links\n/dynamic\n/help")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

