from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("mymembers", "neshe adam qosqanin'izdi aniqlaysiz"),
            types.BotCommand("check", "check"),
            types.BotCommand("gid", "gruppa idsi"),
            types.BotCommand('id', "user id"),
            types.BotCommand("clear", "user maglumatin tazlaw"),
            types.BotCommand("clearall", "grouppa maglumatin tazalaw"),
            types.BotCommand("toplist", "top 50"),
            types.BotCommand("set", "set"),
            types.BotCommand("addlimit", "add limit"),
            types.BotCommand("unlimit", "unlimit"),
            types.BotCommand("offchan", "offchan")
        ]
    )
