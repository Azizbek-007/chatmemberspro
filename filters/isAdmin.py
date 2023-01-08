from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import bot, bot_id

class IsAdmin(BoundFilter):

    async def check(self, message: types.Message):
        get_chat = await bot.get_chat_member(message.chat.id, bot_id)
        if get_chat.status == 'administrator': return True