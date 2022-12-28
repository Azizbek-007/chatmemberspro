from aiogram import types
from loader import dp

@dp.my_chat_member_handler()
async def get_admin_update(msg: types.Message):
    if msg.old_chat_member.status == "administrator":
        await dp.bot.send_message(chat_id=msg.chat.id, text="Bot gruppaga admin boldi")