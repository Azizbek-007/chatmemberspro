from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import bot, bot_id

class IsAdmin(BoundFilter):

    async def check(self, message: types.Message) -> bool:
        get_chat = await bot.get_chat_member(message.chat.id, bot_id)
        is_anonim_admin_us = message.from_user.username
        if (get_chat.status == 'administrator' and is_anonim_admin_us == 'GroupAnonymousBot') or get_chat.status == 'administrator': 
            return True