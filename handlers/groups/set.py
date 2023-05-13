from aiogram import types
from loader import dp, bot_id
from utils.db_api import DBS
from filters import IsAdmin

@dp.message_handler(IsAdmin(), commands="set", chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_set(msg: types.Message):
    await msg.delete()
    channel_username = msg.text.split(' ')
    if len(channel_username) == 2:
        channel_username = channel_username[1]
        if channel_username[0] == '@' and len(channel_username) > 3  and len(channel_username) < 33:
            ps_admin = await dp.bot.get_chat_member(channel_username, bot_id)
            if ps_admin.status == 'administrator':
                channel_data = await dp.bot.get_chat(channel_username)
                if DBS.group_insert_channel(DBS, channel_data.id, msg.chat.id):
                    group_data= await dp.bot.get_chat(msg.chat.id)
                    DBS.set_group_premissions(DBS, msg.chat.id, group_data.permissions)
                    await msg.answer("✅ Канал қосылды!")
            else: await msg.answer("⛔️ Бот {} каналға админ емессиз!".format(channel_username))
        else: await msg.answer("⛔️ Юзернеймди қәте киритдиңиз!")
    else: await msg.answer("Дурыс жазың!\n\nМысалы: /set (username)")


@dp.message_handler(IsAdmin(), commands='unset', chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_unset(msg: types.Message):
    await msg.delete()
    DBS.group_unset_channel(DBS, msg.chat.id)
    await msg.answer("⛔️ Канал өширилди!")

@dp.message_handler(IsAdmin(), commands='channel', chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def bot_get_channel_data(msg: types.Message):
    await msg.delete()
    channel_id = DBS.get_channel_id(DBS, group_id=msg.chat.id)
    if channel_id !=False:
        channel_data = await dp.bot.get_chat(chat_id=channel_id)
        await msg.answer(f"[{channel_data.title}]({channel_data.invite_link}) канал группаға бириктирилген!", parse_mode="markdown", disable_web_page_preview=True)
    else: await msg.answer("Группаға канал бириктирилмеген!")

