from aiogram import types
from loader import dp, admins
from keyboards.inline import admin_btn, send_type, cancel_btn

@dp.message_handler(commands="admin", user_id=admins)
async def hello_admin(msg: types.Message):
    await msg.reply("Helllo Admin", reply_markup=admin_btn)

@dp.callback_query_handler(text=["back", "cancel"])
async def bot_back(call: types.CallbackQuery):
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
async def process_send_users(call: types.CallbackQuery):
    await call.message.answer("Xabar jiberin':", reply_markup=cancel_btn)