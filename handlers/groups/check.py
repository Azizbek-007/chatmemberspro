from aiogram import types
from loader import dp
from utils.db_api import DBS
from lang.message import lang
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['check'], is_reply=True, chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_chek_member(msg: types.Message):
    reply_user = msg.reply_to_message.from_user
    reply_user_count = DBS.my_members(DBS, user_id=reply_user.id)
    if int(reply_user_count) == 0:
        await msg.answer(f"<a href='tg://user?id={msg.from_id}'>{msg.from_user.full_name}</a> еле адам қоспаған!")
    else:
        text = lang.get("reply_user_count").get("uz")
        await msg.answer(text.format(reply_user.id, reply_user.first_name, reply_user_count[0]))
    
@dp.message_handler(IsAdmin(), commands=['check'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_check_fix(msg: types.Message):
    await msg.answer("Группаға ким қанша адам қосқанын билиў ушын, сол адамға reply етип, /check буйрығын киритиң!")
