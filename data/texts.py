stop_chat = [
    [
        """
Anda telah menyelesaikan obrolan Ketik /search untuk menemukan teman baru""",
        """
Teman anda telah menyelesaikan obrolan Ketik /search untuk menemukan teman baru""",
    ],
    [
        """
You have finished the dialog 😞
Type /search to find the next one""",
        """
Your partner has finished the conversation 😞
Type /search to find the next one""",
    ],
]

unavailable_command = [
    "Anda sedang dalam obrolan💬",
    "you are in chat💬",
]

user_banned = [
    "Kami telah membatasi penggunaan obrolan Anda.\nAlasan: {}.\n\n"
    "Anda akan dapat menggunakan obrolan lagi di {}",
    "We have restricted your use of the chat.\nReason: {}.\n\n"
    "You will be able to use the chat again on {}",
]
user_unbanned = [
    "Anda tidak diblokir.\nKami harap Anda memahami aturan dan tidak akan melanggarnya lagi",
    "You are unblocked.\nWe hope you are familiar with the rules and will not break them again",
]

start_menu = [
    """
Senang melihat Anda di obrolan telegram anonim

Perintah yang tersedia:
/next - mitra berikutnya
/search - Mencari pasangan
/stop - Akhiri dialog
/sharelink - Kirim tautan Akun Telegram Anda

jangan lupa gabung di grub @teman_online3""",
    """
Glad to see you in anonymous telegram chat

Available commands:
/next - Next partner
/search - Find a partner
/stop - End the dialog
/sharelink - Send a link to your Telegram Account

don't forget to join the group @teman_online3""",
]

sharelink = [
    [
        "Anda tidak memiliki pasangan.",
        "Tautan Anda telah dikirim ke mitra.",
        "Ini link akun telegram saya.",
        "Dikirim dengan",
    ],
    [
        "You don't have a partner.",
        "Your link has been sent to a partner.",
        "Here is the link to my telegram account.",
        "Sent with",
    ],
]
complain = [
    "Anda dapat menilai pasangan Anda. Ini akan membantu Anda menemukan orang yang tepat untuk diajak bicara",
    "You can rate your partner.This will help you find the right people to talk to",
]
not_partner = ["Anda tidak memiliki pasangan.", "You don't have a partner."]
already_have_partner = [
    "Anda sudah memiliki pasangan.\n/next - mitra berikutnya",
    "You already have a partner.\n/next - next partner",
]
already_searching = [
    "Anda sudah memiliki pasangan.\n/stop - hentikan pencarian",
    "You already have a partner.\n/stop - stop search",
]
stop_search = [
    [
        """
Anda telah menyelesaikan pencarian 😞
Ketik /search untuk menemukan yang berikutnya""",
    ],
    [
        """
You have finished the search 😞
Type /search to find the next one""",
    ],
]
female_search = [
    [
        """
Pasangan Ditemukan 🐵
/next — mitra berikutnya
/stop — Akhiri dialog""",
        "Mencari perempuan...",
    ],
    [
        """
The partner is found 🐵
/next - next partner
/stop - End the dialog""",
        "Searching female...",
    ],
]
male_search = [
    [
        """
Pasangan Ditemukan 🐵
/next — Mitra berikutnya
/stop — Akhiri dialog""",
        "Mencari laki-laki...",
    ],
    [
        """
The partner is found 🐵
/next — Next partner
/stop — End the dialog""",
        "Searching male...",
    ],
]
search = [
    [
        """
Pasangan Ditemukan 🐵
/next — Mitra berikutnya
/stop — Akhiri dialog""",
        "Mencari...",
    ],
    [
        """
The partner is found 🐵
/next - next partner
/stop - End the dialog""",
        "Searching...",
    ],
]

reasons = [
    [
        "Distribusi iklan atau materi penipuan",
        "penjualan atau promosi",
        "Distribusi pornografi anak",
        "Menghina lawan bicara atau perilaku kasar",
        "berkompromi atau tindakan lainnya",
    ],
    [
        "Distribution of advertisements or scam materials",
        "Sale",
        "Distribution of child pornography",
        "Insulting the interlocutor or rude behavior",
        "compromise or other actions",
    ],
]
language_key = {
    "id": [0, "✅ Bahasa berhasil dipilih", "Pilih jenis kelamin Anda"],
    "en": [1, "✅ Language selected successfully", "Choose your gender"],
}


__all__ = [
    "already_have_partner",
    "already_searching",
    "complain",
    "female_search",
    "language_key",
    "male_search",
    "not_partner",
    "reasons",
    "search",
    "sharelink",
    "start_menu",
    "stop_chat",
    "stop_search",
    "unavailable_command",
    "user_banned",
    "user_unbanned",
]
