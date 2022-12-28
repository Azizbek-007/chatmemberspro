from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_btn(bot_username):
        return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="📊Statistika", callback_data="statistika"),
        InlineKeyboardButton(text="Barcha Guruhlar", callback_data="all_groups")
        ).add(
        InlineKeyboardButton(text="Guruhga qoshish", url=f"https://t.me/{bot_username}?startgroup=new")
        )

admin_btn = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Send Message", callback_data="sendMessage")).add(
        InlineKeyboardButton("Send Forward Message", callback_data="sendForward")
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