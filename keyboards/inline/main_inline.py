from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from utils.db_api.database import *


async def sale_keyboard():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"➕ Qo'shilish", callback_data="enter")],
            [InlineKeyboardButton(text=f"⬅️ Oldingi", callback_data="back"),
             InlineKeyboardButton(text=f"Keyingi ➡️", callback_data="next")],
        ]
    )
    return markup



async def check_user_membership():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="MINSPORT INSTITUT", url="https://t.me/minsport_institut")],
            [InlineKeyboardButton(text="✅ Tekshirish", callback_data="check")],
        ]
    )
    return markup


async def sale_confirm(sale_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=f"MINSPORT INSTITUT", callback_url="https://t.me/minsport_institut")],
            [InlineKeyboardButton(text=f"✅ Tekshirish", callback_data="check")],
        ]
    )
    return markup


async def year_keyboard(years):
    inline_keyboard = []
    for i in years:
        inline_keyboard.append([InlineKeyboardButton(text=f"{i}", callback_data=i)])
    inline_keyboard.append([InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"back_menu")])
    markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return markup


Moths = {1: 'Yanvar', 2: 'Fevral', 3: 'Mart', 4: 'Aprel', 5: 'May', 6: 'Iyun', 7: 'Iyul', 8: 'Avgust', 9: 'Sentabr',
         10: 'Oktyabr', 11: 'Noyabr', 12: 'Dekabr', }


async def month_keyboard(date):
    inline_keyboard = []
    for i in date:
        inline_keyboard.append([InlineKeyboardButton(text=f"{Moths[i]}", callback_data=i)])
    inline_keyboard.append([InlineKeyboardButton(text="🔙 Orqaga", callback_data=f"back_menu")])
    markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return markup


async def teachers_keyboard(objects):
    inline_keyboard = []
    for obj in objects:
        inline_keyboard.append([InlineKeyboardButton(text=f"{obj.name}", callback_data=obj.id)])
    inline_keyboard.append([
        InlineKeyboardButton(text="⬅️ Orqaga", callback_data=f"back"),
        InlineKeyboardButton(text="➡️ Oldinga", callback_data=f"next"),
    ])
    markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    return markup
