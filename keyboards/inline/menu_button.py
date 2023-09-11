from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from apps.main.models import *


async def main_menu():
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"📆 Dars jadvali bilan tanishish")
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def filial_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2)
    key1 = KeyboardButton(text=f"Institut")
    key2 = KeyboardButton(text=f"Farg'ona filiali")
    key3 = KeyboardButton(text=f"Samarqand filiali")
    key4 = KeyboardButton(text=f"Nukus filiali")
    key5 = KeyboardButton(text=f"⬅️ Orqaga")
    keyboard.add(key1, key2, key3, key4)
    keyboard.add(key5)
    keyboard.resize_keyboard = True
    return keyboard


async def group_keyboard(filial):
    keyboard = ReplyKeyboardMarkup(row_width=2)
    keys = []
    groups = StudyGroup.objects.filter(filial=filial).all()
    for group in groups:
        key = KeyboardButton(text=group.name)
        keyboard.add(key)
    back_to_key = KeyboardButton(text=f"⬅️ Orqaga")
    keyboard.add(back_to_key)
    keyboard.resize_keyboard = True
    return keyboard


async def get_teachers_or_back():
    keyboard = ReplyKeyboardMarkup(row_width=1)
    key = KeyboardButton(text=f"👨‍🏫 O'qituvchilar ro'yxatiga o'tish")
    back_to_key = KeyboardButton(text=f"⬅️ Orqaga")
    keyboard.add(key, back_to_key)
    keyboard.resize_keyboard = True
    return keyboard


async def phone_keyboard():
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"📞 Raqamni ulashish", request_contact=True)
    key2 = KeyboardButton(text=f"⬅️ Orqaga")
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def back_key():
    keyboard = ReplyKeyboardMarkup()
    key1 = KeyboardButton(text=f"⬅️ Orqaga")
    keyboard.add(key1)
    keyboard.resize_keyboard = True
    return keyboard


async def menu_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2)
    key1 = KeyboardButton(text=f"Mening hisobim/Bonuslarim")
    key2 = KeyboardButton(text=f"QrCode")
    key3 = KeyboardButton(text=f"Joriy aksiyalar")
    key4 = KeyboardButton(text=f"To'lovlar tarixi")
    key5 = KeyboardButton(text=f"Yangiliklar")
    key6 = KeyboardButton(text=f"Izoh qoldirish")
    keyboard.add(key1, key2, key3, key4, key5, key6)
    keyboard.resize_keyboard = True
    return keyboard

