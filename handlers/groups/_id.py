from aiogram import types
from loader import dp
from lang.message import lang
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['id', 'myid'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def get_my_id(msg: types.Message):
    await msg.delete()
    text = lang.get('my_id').get("uz")
    await msg.answer(text.format(msg.from_id, msg.from_user.first_name, msg.from_id))

@dp.message_handler(IsAdmin(), commands=['gid'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def get_group_id(msg: types.Message):
    await msg.delete()
    text = lang.get("group_id").get("uz")
    await msg.answer(text.format(msg.chat.id))