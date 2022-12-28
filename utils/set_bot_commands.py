from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("mymembers", "neshe adam qosqanin'izdi aniqlaysiz"),
            types.BotCommand("check", "check"),
            types.BotCommand("gid", "gruppa idsi")
        ]
    )
