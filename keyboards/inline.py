from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


lang_btn = InlineKeyboardMarkup(resize_keyboard=True)
lang_btn.add(
    InlineKeyboardButton(text="Indonesia  🇮🇩", callback_data="id"),
    InlineKeyboardButton(text="English 🇬🇧", callback_data="en"),
)


async def gender_btn(lang):
    s = [["👨‍🦱 Laki-laki", "👩‍🦱 Perempuan"], ["👨‍🦱 Male", "👩‍🦱 Female"]]
    gender_btn1 = InlineKeyboardMarkup(resize_keyboard=True)
    gender_btn1.add(
        InlineKeyboardButton(text=f"{s[lang][0]}", callback_data="M"),
        InlineKeyboardButton(text=f"{s[lang][1]}", callback_data="F"),
    )
    return gender_btn1


async def complain_wth_rate_btn(user_id, lang):
    s = ["Keluhan", "Report"]
    complain_btn1 = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)
    complain_btn1.add(
        InlineKeyboardButton(text="👍", callback_data=f"👍_{user_id}"),
        InlineKeyboardButton(text="👎", callback_data=f"👎_{user_id}"),
        InlineKeyboardButton(text=f"{s[lang]}", callback_data=f"report_{user_id}"),
    )
    return complain_btn1


async def ban_btn(user_id, reason, ids):
    ban_btn1 = InlineKeyboardMarkup(row_width=3, resize_keyboard=True)
    ban_btn1.add(
        InlineKeyboardButton(
            text="1d", callback_data=f"ban_{reason}_1_{user_id}_{ids}",
        ),
        InlineKeyboardButton(
            text="2d", callback_data=f"ban_{reason}_2_{user_id}_{ids}",
        ),
        InlineKeyboardButton(
            text="7d", callback_data=f"ban_{reason}_7_{user_id}_{ids}",
        ),
        InlineKeyboardButton(
            text="30d", callback_data=f"ban_{reason}_30_{user_id}_{ids}",
        ),
        InlineKeyboardButton(
            text="60d", callback_data=f"ban_{reason}_60_{user_id}_{ids}",
        ),
        InlineKeyboardButton(
            text="365d", callback_data=f"ban_{reason}_365_{user_id}_{ids}",
        ),
    )
    return ban_btn1


async def complain1_btn(user_id, lang):
    s = [
        ["📰 Periklanan", "💰 Penjualan", "🔞 Pornografi ", "🤬 Menyinggung", "❌ Lainnya"],
        ["📰 Advertising", "💰 Selling", "🔞 Child pornography", "🤬 Insult", "❌ Other"],
    ]
    complain_btn1 = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)
    complain_btn1.add(
        InlineKeyboardButton(
            text=f"{s[lang][0]}", callback_data=f"Advertising_{user_id}",
        ),
        InlineKeyboardButton(text=f"{s[lang][1]}", callback_data=f"Selling_{user_id}"),
        InlineKeyboardButton(text=f"{s[lang][2]}", callback_data=f"CP_{user_id}"),
        InlineKeyboardButton(text=f"{s[lang][3]}", callback_data=f"Insult_{user_id}"),
        InlineKeyboardButton(text=f"{s[lang][4]}", callback_data=f"Other_{user_id}"),
    )
    return complain_btn1


__all__ = [
    "ban_btn",
    "complain1_btn",
    "complain_wth_rate_btn",
    "gender_btn",
    "lang_btn",
]
