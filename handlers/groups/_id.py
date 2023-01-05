from aiogram import types
from loader import dp
from lang.message import lang


@dp.message_handler(commands=['id', 'myid', 'gid'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPER_GROUP])
async def get_my_id(msg: types.Message):
    if msg.text in ['id', 'myid']:
        text = lang.get('my_id').get("uz")
        await msg.answer(text.format(msg.from_id, msg.from_user.first_name, msg.from_id))
    else:
        text = lang.get("group_id").get("uz")
        await msg.answer(text.format(msg.chat.id))