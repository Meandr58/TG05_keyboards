from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет!"), KeyboardButton(text="Пока!")]
    ],
    resize_keyboard=True
)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Новости", url='https://t.me/s/rian_ru/')],  [InlineKeyboardButton(text="Музыка", url='https://s30sas.storage.yandex.net/get-mp3/4031ebc2baf9c926208dbb322a1fb710c72ad4e2fbce54255c818f64fa643e71/000622a85c2e3058//rmusic/U2FsdGVkX18helv2roir1SYTvBNEqxy6g3PUcyOo7Yew_3ycmxiCaOE9FOhphxMAEOJF5pfiUZJghhZlm6euk00NSmZPurMEdWB5uSf6Tho/4031ebc2baf9c926208dbb322a1fb710c72ad4e2fbce54255c818f64fa643e71/30035?track-id=15502569&play=false')],  [InlineKeyboardButton(text="Видео", url='https://rutube.ru/video/4b03c2e78390ab766c65cf2cf8dd8fc0/?r=plemwd')]
])

testb = ["Первая кнопка", "Вторая кнопка"]


async def builder_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in testb:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=key))  # Используем InlineKeyboardButton с callback_data
    return keyboard.as_markup()  # Возвращаем объект клавиатуры в виде InlineKeyboardMarkup

async def dynamic_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))
    return keyboard.as_markup()

# Кнопки для второй стадии ("Опция 1" и "Опция 2")
async def more_options_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data="option_1"))
    keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data="option_2"))
    return keyboard.as_markup()



