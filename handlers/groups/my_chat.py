from aiogram import types
from loader import dp

@dp.my_chat_member_handler()
async def get_admin_update(msg: types.Message):
    if msg.old_chat_member.status == "administrator":
        await dp.bot.send_message(chat_id=msg.chat.id, 
            text="🤖<b> Бот - группаға админ қылынды </b>✅\n\n"
            "👮🏻‍♂️ Мен группада ислеўге тайынман!\n\n"
            "⚠️ <b>Ескертпе: Егер сиз ботты группадан шығарып тасласаңыз, бәрше группа мағлыўматлар базасы өширип тасланады!</b> 🗑")