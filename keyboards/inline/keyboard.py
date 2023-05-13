from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp

def start_btn(bot_username):
        return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="📊 Есабат", callback_data="statistika"),
        # InlineKeyboardButton(text="Barcha Guruhlar", callback_data="all_groups")
        ).add(
        InlineKeyboardButton(text="➕ Группаға қосыў", url=f"https://t.me/{bot_username}?startgroup=new")
        )

admin_btn = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Send Message", callback_data="sendMessage")).add(
        InlineKeyboardButton("Send Forward Message", callback_data="sendForward")
        ).add(
        InlineKeyboardButton("Update", callback_data="AllUpdate")
        )

def send_type(_type):
        return InlineKeyboardMarkup().add(
                InlineKeyboardButton("Users", callback_data=f"sendUsers={_type}")
        ).add(
        InlineKeyboardButton("Groups", callback_data=f"sendGroups={_type}")
        ).add(
                InlineKeyboardButton("Back", callback_data="back")
        )

cancel_btn = InlineKeyboardMarkup().add(InlineKeyboardButton(text="cancel", callback_data="cancel"))

def added_btn(user_id):
        return InlineKeyboardMarkup().add(
                        InlineKeyboardButton(text="Қостым ✅", callback_data=f"added={user_id}"))

def added_channe_btn(user_id, url):
        return InlineKeyboardMarkup().add(
                InlineKeyboardButton(text="Каналға қосылыў", url=url)
                ).add(
                InlineKeyboardButton(text="Ағза болдым ✅", callback_data=f"added_channel={user_id}"))

def pagination_btn(form, inc):
    return InlineKeyboardMarkup().add(
            InlineKeyboardButton("◀️", callback_data=f"back={form}={inc}"),
            InlineKeyboardButton("▶️", callback_data=f"next={form}={inc}")).add(
            InlineKeyboardButton("cancel", callback_data='cancel_user'))

def share_btn(bot_user):
        return InlineKeyboardMarkup().add(
                        InlineKeyboardButton(text="➕ Ботты группаға қосыў", url=f"https://t.me/{bot_user}?startgroup=new"))
