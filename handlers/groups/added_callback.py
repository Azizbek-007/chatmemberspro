from aiogram import types
from loader import dp
from utils.db_api.func import DBS

@dp.callback_query_handler(lambda call: call.data.startswith("added="))
async def bot_added_call (call: types.CallbackQuery):
    call_data_userid = call.data.split('=')[1]
    if str(call_data_userid) == str(call.from_user.id):
        count_data = DBS.get_member_count(DBS, call.message.chat.id)
        if count_data != False:
            user_added_count = DBS.my_members(DBS, user_id=call.from_user.id, group_id=call.message.chat.id)
            if user_added_count >= int(count_data): 
                await call.message.delete() 
                permissions =  DBS.get_group_premissions(DBS, call.message.chat.id)
                await dp.bot.restrict_chat_member(
                            chat_id=call.message.chat.id,
                            user_id=call.from_user.id,
                            permissions=permissions
                        )
            else:
                await call.answer(f"{count_data-user_added_count} adam qosiwin'iz kerek!", True)
        else:
            await call.message.delete() 
            permissions =  DBS.get_group_premissions(DBS, call.message.chat.id)
            await dp.bot.restrict_chat_member(
                            chat_id=call.message.chat.id,
                            user_id=call.from_user.id,
                            permissions=permissions
                        )
    else: await call.answer("Aljasip basip aldin'iz")

@dp.callback_query_handler(lambda call: call.data.startswith('added_channel='))
async def bot_add_user_channel(call: types.CallbackQuery):
    call_data_userid = call.data.split('=')[1]
    if call_data_userid == str(call.from_user.id):
        channel_id = DBS.get_channel_id(DBS, call.message.chat.id)
        if channel_id != False:
            get_status = await dp.bot.get_chat_member(channel_id, call.from_user.id)
            if get_status.status == 'left':
                await call.answer("Ele kanalg'a ag'za bolmadin'iz", True)
            else:
                await call.message.delete() 
                permissions =  DBS.get_group_premissions(DBS, call.message.chat.id)
                await dp.bot.restrict_chat_member(
                                chat_id=call.message.chat.id,
                                user_id=call.from_user.id,
                                permissions=permissions
                            )
        else: 
            await call.message.delete() 
            permissions =  DBS.get_group_premissions(DBS, call.message.chat.id)
            await dp.bot.restrict_chat_member(
                                chat_id=call.message.chat.id,
                                user_id=call.from_user.id,
                                permissions=permissions
                            )
    else: await call.answer("Aljasip basip aldin'iz")