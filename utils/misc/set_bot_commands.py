from aiogram import types


async def set_default_commands(dp):

    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Mulai ulang bot / Restart a bot"),
            types.BotCommand("next", "Teman bicara berikutnya / Next partner"),
            types.BotCommand("search", "Mulai mencari / Find a partner"),
            types.BotCommand("stop", "Akhiri dialog / End the dialog"),
            types.BotCommand("sharelink", "Bagikan Profil / Send a link to your Telegram Account"),
        ],
    )


__all__ = [
    "set_default_commands",
]
