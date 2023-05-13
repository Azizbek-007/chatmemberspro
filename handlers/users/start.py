from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from lang.message import lang
from loader import dp
from keyboards.inline import start_btn
from utils.db_api import DBS



@dp.message_handler(CommandStart(), chat_type=types.ChatType.PRIVATE)
@dp.throttled(rate=5)
async def bot_start(message: types.Message):
    text = lang.get("start").get("uz")
    bot_data = await dp.bot.get_me()
    DBS.user_register(DBS, user_id=message.from_id, user_name=message.from_user.username, full_name=message.from_user.full_name)
    await message.answer(text, reply_markup=start_btn(bot_data.username))

@dp.callback_query_handler(text="statistika")
async def bot_statistika(call: types.CallbackQuery):
    data = DBS.user_and_group_count(DBS)
    text = lang.get("statistika").get("uz").format(data[0], data[1])
    await call.answer(text, show_alert=True)