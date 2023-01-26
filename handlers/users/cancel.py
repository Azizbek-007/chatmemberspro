from aiogram import types
from loader import dp

@dp.callback_query_handler(text='cancel_user')
async def bot_user_cancel(call: types.CallbackQuery):
    await call.answer("Canceled")
    await call.message.delete()