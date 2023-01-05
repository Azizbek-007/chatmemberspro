from aiogram import types
from loader import dp, bot_id
from utils.db_api import DBS

@dp.message_handler(content_types=[types.ContentType.ANY], chat_type=[types.ChatType.GROUP, types.ChatType.SUPER_GROUP])
async def not_join_channel (msg: types.Message):
    channel_id = DBS.get_channel_id(DBS, msg.chat.id)
    if channel_id != False:
        get_status = await dp.bot.get_chat_member(channel_id, msg.from_id)
        get_data = await dp.bot.get_chat(channel_id)
        if get_status.status == 'left':
            await msg.delete()
            await msg.answer(f"[{get_data.title}]({get_data.invite_link}) Kanalga agza bolmasan'iz gruppada jaza almaysiz", 
                parse_mode="markdown",
                disable_web_page_preview=True
                )
            await dp.bot.restrict_chat_member(
                    chat_id=msg.chat.id,
                    user_id=msg.from_id,
                    can_send_messages=False
                    )