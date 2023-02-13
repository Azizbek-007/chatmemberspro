from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands="clear", is_reply=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_clear(msg: types.Message):
    await msg.delete()
    reply_user_id = msg.reply_to_message.from_id
    DBS.clear_all_user(DBS, user_id=reply_user_id)
    await msg.answer("мағлыўматлары тазаланды! ✅")

@dp.message_handler(IsAdmin(), commands="clearall", chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_clear_all(msg: types.Message):
    await msg.delete()
    DBS.clear_all_group(DBS, msg.chat.id)
    await msg.answer(f"<a href='tg://user?id={msg.chat.id}'>{msg.chat.title}</a> группасындағы мағлыўматлар тазаланды!")

@dp.message_handler(IsAdmin(), commands="clear", chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_clear(msg: types.Message):
    await msg.delete()
    await msg.answer("Дурыс жазың!\n\nМысалы: /clear (ID яки reply)")