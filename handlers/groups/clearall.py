from aiogram import types
from loader import dp
from utils.db_api import DBS

@dp.message_handler(commands="clear", is_reply=True)
async def bot_clear(msg: types.Message):
    reply_user_id = msg.reply_to_message.from_id
    DBS.clear_all_user(DBS, user_id=reply_user_id)
    await msg.answer("maglumatlari tazalandi/c")

@dp.message_handler(commands="clearall")
async def bot_clear_all(msg: types.Message):
    DBS.clear_all_group(DBS, msg.chat.id)
    await msg.answer("Gruppa maglumatlari tazalandi")