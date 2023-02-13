from aiogram import types
from loader import dp
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['reset'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_reset(msg: types.Message):
    await msg.delete()
    permissions = DBS.get_group_premissions(DBS, msg.chat.id)
    DBS.reset(DBS, msg.chat.id)
    await dp.bot.set_chat_permissions(msg.chat.id, permissions)
    await msg.answer("✅ Боттағы бәрше сазламалар өз ҳалына қайтарылды!")