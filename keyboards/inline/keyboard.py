from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_btn(bot_username):
        return InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="📊Statistika", callback_data="statistika"),
        InlineKeyboardButton(text="Barcha Guruhlar", callback_data="all_groups")
        ).add(
        InlineKeyboardButton(text="Guruhga qoshish", url=f"https://t.me/{bot_username}?startgroup=new")
        )