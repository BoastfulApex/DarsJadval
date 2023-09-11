from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from keyboards.inline.menu_button import *
from keyboards.inline.main_inline import *
from utils.db_api.database import *
import datetime


@dp.message_handler(state='main_menu')
async def menu(message: types.Message, state: FSMContext):
    keyboard = await filial_keyboard()
    await message.answer(text="Iltimos siz o'qiyotgan filialni tanlang 👇", reply_markup=keyboard)
    await state.set_state('get_filial')


@dp.message_handler(state='get_filial')
async def menu(message: types.Message, state: FSMContext):
    if message.text == "⬅️ Orqaga":
        keyboard = await main_menu()
        await message.answer("Iltimos kerakli bo'limni tanlang 👇", reply_markup=keyboard)
        await state.set_state('main_menu')
    elif message.text not in ["Institut",
                              "Nukus Filiali",
                              "Samarqand filiali",
                              "Farg'ona filali"]:
        keyboard = await filial_keyboard()
        await message.answer(text="Iltimos siz o'qiyotgan filialni tanlang 👇", reply_markup=keyboard)
        await state.set_state('get_filial')
    else:
        await state.update_data(filial=message.text)
        keyboard = await group_keyboard(message.text)
        await message.answer("Iltimos kerakli guruhni tanlang 👇", reply_markup=keyboard)
        await state.set_state('get_group')


@dp.message_handler(state='get_group')
async def get_group_name(message: types.Message, state: FSMContext):
    if message.text == "⬅️ Orqaga":
        keyboard = await filial_keyboard()
        await message.answer(text="Iltimos siz o'qiyotgan filialni tanlang 👇", reply_markup=keyboard)
        await state.set_state('get_filial')
    else:
        data = await state.get_data()
        group = await get_group(message.text)
        if group and group is not None:
            photo = open(group.PhotoURL[1:], 'rb')

            current_date = datetime.date.today()

            start_of_week = current_date - datetime.timedelta(days=current_date.weekday())

            end_of_week = start_of_week + datetime.timedelta(days=6)

            start_date_formatted = start_of_week.strftime("%d.%m.%Y")
            end_date_formatted = end_of_week.strftime("%d.%m.%Y")

            week_range = f"{start_date_formatted} - {end_date_formatted}"
            text = f"{group.name} guruhi uchun {week_range} oralig'idagi dars jadvali"
            keyboard = await get_teachers_or_back()
            await message.answer_photo(photo=photo, caption=text, reply_markup=keyboard)
            await state.set_state('get_teachers_or_back')
        else:
            keyboard = await group_keyboard(data['filial'])
            await message.answer("Iltimos kerakli guruhni tanlang 👇", reply_markup=keyboard)
            await state.set_state('get_group')


@dp.message_handler(state='get_teachers_or_back')
async def get_group_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text == "⬅️ Orqaga":
        keyboard = await group_keyboard(data['filial'])
        await message.answer("Iltimos kerakli guruhni tanlang 👇", reply_markup=keyboard)
        await state.set_state('get_group')
    elif message.text == "👨‍🏫 O'qituvchilar ro'yxatiga o'tish":
        index = 1
        await state.update_data(index=1)
        teachers = await get_teachers(filial=data['filial'])
        objects = teachers[(index - 1) * 10: index + 10]
        back_keyboard = await back_key()
        keyboard = await teachers_keyboard(objects)
        text = "👨‍🏫 Kerakli o'qtuvchini tanlang 👇"
        await message.answer(f"O'qituvchilar ro'yxati", reply_markup=back_keyboard)
        await message.answer(text, reply_markup=keyboard)
        await state.set_state('get_teacher')


@dp.callback_query_handler(state='get_teacher')
async def get_teacher(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data == 'next':
        teachers = await get_teachers(data['filial'])
        index = int(data['index']) + 1
        max_index = len(teachers) // 10
        if index > max_index:
            index = 1
        objects = teachers[(index - 1) * 10: index + 10]
        keyboard = await teachers_keyboard(objects)
        await call.message.edit_reply_markup(reply_markup=keyboard)
    elif call.data == 'back':
        teachers = await get_teachers(data['filial'])
        index = int(data['index']) - 1
        if index <= 0:
            index = 1
        objects = teachers[(index - 1) * 10: index + 10]
        keyboard = await teachers_keyboard(objects)
        await call.message.edit_reply_markup(reply_markup=keyboard)
    else:
        teacher = await get_teacher_data(call.data)
        text = f"<b>{teacher.name}</b>\n\n{teacher.zoom_link}\n\n{teacher.description}"
        await call.message.edit_text(text, reply_markup=None)


@dp.message_handler(state='get_teacher')
async def get_teacher(message: types.Message, state: FSMContext):
    if message.text == "⬅️ Orqaga":
        keyboard = await filial_keyboard()
        await message.answer(text="Iltimos siz o'qiyotgan filialni tanlang 👇", reply_markup=keyboard)
        await state.set_state('get_filial')