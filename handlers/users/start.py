from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from keyboards.inline.menu_button import *
from keyboards.inline.main_inline import *
from utils.db_api.database import *

import re
import aiohttp
import random


async def generateOTP():
    return random.randint(111111, 999999)


async def send_sms(otp, phone):
    username = 'intouch'
    password = '-u62Yq-s79HR'
    sms_data = {
        "messages": [{"recipient": f"{phone}", "message-id": "abc000000003",
                      "sms": {"originator": "MEGASTAR", "content": {"text": f"Mega Star uchun tasdiqkash kodi: {otp}"}}}]}
    url = "http://91.204.239.44/broker-api/send"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, auth=aiohttp.BasicAuth(login=username, password=password),
                                json=sms_data) as response:
            print(response.status)


async def isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


@dp.message_handler(commands=['start'], state='*')
async def start_func(message: types.Message, state: FSMContext):
    await message.answer(text="Assalomu alaykum 👋. \nJismoniy tarbiya va sport bo‘yicha mutaxassislarni qayta "
                              "tayyorlash va malakasini oshirish instituti botiga xush kelibsiz. ",
                         reply_markup=ReplyKeyboardRemove())
    try:
        channel_username = '@minsport_institut'

        user_id = message.from_user.id
        member = await bot.get_chat_member(chat_id=channel_username, user_id=user_id)

        if member.status == "member" or member.status == "administrator" or member.status == "creator":
            keyboard = await main_menu()
            await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=keyboard)
            await state.set_state('main_menu')
        else:
            markup = await check_user_membership()
            await message.answer("⚠️ Botdan  foydalnish uchun <b>MINSPORT INSTITUT</b> kanaliga a'zo bo'lishingiz kerak",
                                 reply_markup=markup)
            await state.set_state('check_member')
    except Exception as e:
        await message.answer(f"An error occurred: {str(e)}")


@dp.callback_query_handler(state='check_member')
async def check_member(call: types.CallbackQuery, state: FSMContext):
    channel_username = '@minsport_institut'
    user_id = call.from_user.id
    member = await bot.get_chat_member(chat_id=channel_username, user_id=user_id)
    if member.status == "member" or member.status == "administrator" or member.status == "creator":
        await call.message.delete()
        keyboard = await main_menu()
        await bot.send_message(chat_id=user_id, text="Iltimos kerakli bo'limni tanlang 👇", reply_markup=keyboard)
        await state.set_state('main_menu')
    else:
        markup = await check_user_membership()
        await call.message.edit_text("⚠️ Botdan  foydalnish uchun <b>MINSPORT INSTITUT</b> kanaliga a'zo "
                                     "bo'lishingiz kerak", reply_markup=markup)
        await state.set_state('check_member')
