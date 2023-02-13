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
            types.BotCommand("top", "top 50"),
            types.BotCommand("set", "set"),
            types.BotCommand("add", "add limit"),
            types.BotCommand("addoff", "unlimit"),
            types.BotCommand("offchan", "offchan"),
            types.BotCommand("onchan", "onchan"),
            types.BotCommand("offads", "offads"),
            types.BotCommand("onads", "onads"),
            types.BotCommand("reset", "reset"),
            types.BotCommand("open", "open"),
            types.BotCommand("close", "close"),
            types.BotCommand("time", "time")
        ]
    )
