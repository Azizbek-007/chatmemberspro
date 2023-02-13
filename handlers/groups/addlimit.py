from aiogram import types
from loader import dp, bot_id
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands=['add'], chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_addlimit(msg: types.Message):
    add_count = msg.text.split(' ')
    if len(add_count) == 2:
        try: 
            add_count_number = int(add_count[1])
            DBS.add_member_count(DBS, msg.chat.id, add_count_number)
            await msg.answer("Қосылды ✅")
        except TypeError:
            await msg.answer("Дурыс жазың!\n\nМысалы: /addlist 10\n❗️Еслетпе: 10 санының орнына қәлеген санды жазыўыңызға болады.") 
    else: await msg.answer("Дурыс жазың!\n\nМысалы: /addlist 10\n")
    await msg.delete()