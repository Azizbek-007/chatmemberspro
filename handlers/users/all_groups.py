from aiogram import types
from loader import dp
from utils.db_api.func import DBS
from aiogram.dispatcher import FSMContext
from keyboards.inline import pagination_btn


@dp.callback_query_handler(text='all_groups', chat_type=types.ChatType.PRIVATE)
async def bot_all_group_list(call: types.CallbackQuery, state: FSMContext):
    group_litst = DBS.group_list(DBS)
    i, text, = 0, ""
    form = {}
    for x in group_litst:
        try:
            group_data = await dp.bot.get_chat(x[1])
            group_members_cout = await dp.bot.get_chat_members_count(x[1])
            text += f"<i>{i+1}</i>. <b>Group:</b> {group_data.title} \n<b>" \
                    f"Group id:</b> {x[1]}\n<b>Group user:</b> {group_data.invite_link}\n" \
                    f"<b>Group members:</b> {group_members_cout}\n\n"
            i += 1
            form.update({"_count": x[0]})
            if i == 2: break
        except: pass
    await call.message.answer(text, disable_web_page_preview=False, reply_markup=pagination_btn(form=form.get('_count'), inc=i))


@dp.callback_query_handler(lambda call: 'next=' in call.data)
async def next_pagination(call: types.CallbackQuery):
    data = call.data.split("=")
    form, inc = data[1], int(data[2])
    group_list = DBS.group_list_limited(DBS, form)
    i, text, form = 0, "", {}
    try:
        for x in group_list:
            try:
                group_data = await dp.bot.get_chat(x[1])
                group_members_cout = await dp.bot.get_chat_members_count(x[1])
            except: continue
            text += f"<i>{inc+1}</i>. <b>Group:</b> {group_data.title} \n<b>" \
                    f"Group id:</b> {x[1]}\n<b>Group user:</b> {group_data.invite_link}\n" \
                    f"<b>Group members:</b> {group_members_cout}\n\n"
            inc += 1
            i +=1
            form.update({"_count": x[0]})
            if i == 2: break 
        await call.message.delete()
        await call.message.answer(text, 
            disable_web_page_preview=True, 
            reply_markup=pagination_btn(form=form.get('_count'), inc=inc))
    except Exception:
        await call.answer("Bul aqirg'isi edi:)", True)

@dp.callback_query_handler(lambda call: 'back=' in call.data)
async def back_pagination(call: types.CallbackQuery):
    data = call.data.split("=")
    if int(data[2]) > 0:
        form, inc = data[1], int(data[2])-1
        group_list = DBS.group_list_limited_back(DBS, form)
        i, text, form = 0, "", {}
        try:
            for x in group_list:
                try:
                    group_data = await dp.bot.get_chat(x[1])
                    group_members_cout = await dp.bot.get_chat_members_count(x[1])
                except: continue
                text += f"<i>{inc-1}</i>. <b>Group:</b> {group_data.title} \n<b>" \
                        f"Group id:</b> {x[1]}\n<b>Group user:</b> {group_data.invite_link}\n" \
                        f"<b>Group members:</b> {group_members_cout}\n\n"
                inc -= 1
                i +=1
                form.update({"_count": x[0]})
                if i == 2: break 
            await call.message.delete()
            await call.message.answer(text, 
                disable_web_page_preview=True, 
                reply_markup=pagination_btn(form=form.get('_count'), inc=inc))
        except Exception:
            await call.answer("Bul aqirg'isi edi:)", True)
    else: await call.answer("Bul aqirg'isi edi:)", True)