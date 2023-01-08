from aiogram import types
from loader import dp, admins
from keyboards.inline import admin_btn, send_type, cancel_btn
from states import PromisSendMessage
from aiogram.dispatcher import FSMContext
from utils.db_api import DBS
import asyncio

@dp.message_handler(commands="admin", user_id=admins, chat_type=types.ChatType.PRIVATE)
async def hello_admin(msg: types.Message):
    await msg.reply("Helllo Admin", reply_markup=admin_btn)

@dp.callback_query_handler(text=["back", "cancel"], state='*')
async def bot_back(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer("Helllo Admin", reply_markup=admin_btn)

@dp.callback_query_handler(text="sendMessage")
async def send_message(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Xabar jiberiw turin tanlan:", reply_markup=send_type("message"))

@dp.callback_query_handler(text="sendForward")
async def send_message(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Xabar jiberiw turin tanlan:", reply_markup=send_type("forward"))


@dp.callback_query_handler(lambda call: "sendUsers=" in call.data)
async def process_send_users(call: types.CallbackQuery, state: FSMContext):
    data = str(call.data).split("=")
    await state.update_data(msg_type=data[1])
    await PromisSendMessage.promis.set()
    await call.message.answer("Xabar jiberin':", reply_markup=cancel_btn)

@dp.callback_query_handler(lambda call: 'sendGroups=' in call.data)
async def process_send_groups(call: types.CallbackQuery, state: FSMContext):
    data = str(call.data).split("=")
    await state.update_data(msg_type=data[1])
    await PromisSendMessage.group_promis.set()
    await call.message.answer("Xabar jiberin':", reply_markup=cancel_btn)

@dp.message_handler(state=PromisSendMessage.group_promis)
async def get_message_for_group(msg: types.Message, state: FSMContext):
    get_data = await state.get_data()
    if get_data['msg_type'] == 'message':
        await state.finish()
        await msg.answer("jiberilip atir....")
        n, s = 0, 0
        for x in DBS.group_list(DBS):
            try:
                user_id = x[1]
                await msg.copy_to(user_id, reply_markup=msg.reply_markup)
                s +=1
                await asyncio.sleep(.08)
            except: n +=1
        await msg.answer("Jiberildi: {}\nJiberilmedi: {}".format(s, n))
    elif get_data['msg_type'] == 'forward':
        await state.finish()
        await msg.answer("jiberilip atir....")
        n, s = 0, 0
        for x in DBS.group_list(DBS):
            try:
                user_id = x[1]
                await msg.forward(user_id)
                s +=1
                await asyncio.sleep(.08)
            except: n +=1
        await msg.answer("Jiberildi: {}\nJiberilmedi: {}".format(s, n))


@dp.message_handler(state=PromisSendMessage.promis)
async def get_message(msg: types.Message, state: FSMContext):
    get_data = await state.get_data()
    if get_data['msg_type'] == 'message':
        await state.finish()
        await msg.answer("jiberilip atir....")
        n, s = 0, 0
        for x in DBS.user_list(DBS):
            try:
                user_id = x[0]
                await msg.copy_to(user_id, reply_markup=msg.reply_markup)
                s +=1
                await asyncio.sleep(.08)
            except: n +=1
        await msg.answer("Jiberildi: {}\nJiberilmedi: {}".format(s, n))
    elif get_data['msg_type'] == 'forward':
        await state.finish()
        await msg.answer("jiberilip atir....")
        n, s = 0, 0
        for x in DBS.user_list(DBS):
            try:
                user_id = x[0]
                await msg.forward(user_id)
                s +=1
                await asyncio.sleep(.08)
            except: n +=1
        await msg.answer("Jiberildi: {}\nJiberilmedi: {}".format(s, n))

    

