import telebot
import os

# ✅ TOKEN xavfsiz, Render yoki .env orqali olinadi
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

# ✅ Majburiy obuna kanal username
CHANNEL_ID = "@ramantik_k1no_uzb"  # o'zing yaratgan kanal username

# ✅ Kino bazasi: nom → Telegram video FileID
movies = {
    "avatar": "BQACAgQAAxkBAAIBY2AvatarFileID",
    "avengers": "BQACAgQAAxkBAAIBZ2AvengersFileID",
    "joker": "BQACAgQAAxkBAAIBa3JokerFileID",
    "spiderman": "BQACAgQAAxkBAAIBb4SpidermanFileID",
    "batman": "BQACAgQAAxkBAAIBc5BatmanFileID"
}

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    try:
        # ✅ Majburiy obuna tekshirish
        member = bot.get_chat_member(CHANNEL_ID, message.from_user.id)
        if member.status in ['left', 'kicked']:
            bot.send_message(
                message.chat.id,
                f"❌ Kanalga obuna bo‘lishingiz kerak: {CHANNEL_ID}"
            )
            return
    except:
        bot.send_message(
            message.chat.id,
            "❌ Kanalga ulanishda xato. Administrator bilan bog‘laning."
        )
        return

    bot.send_message(
        message.chat.id,
        "🎬 Kino bot ishlayapti!\nKino nomini yozing."
    )

# Foydalanuvchi yozgan nomga mos kino yuborish
@bot.message_handler(func=lambda m: True)
def send_movie(message):
    try:
        # ✅ Majburiy obuna tekshirish
        member = bot.get_chat_member(CHANNEL_ID, message.from_user.id)
        if member.status in ['left', 'kicked']:
            bot.send_message(
                message.chat.id,
                f"❌ Kanalga obuna bo‘lishingiz kerak: {CHANNEL_ID}"
            )
            return
    except:
        bot.send_message(
            message.chat.id,
            "❌ Kanalga ulanishda xato."
        )
        return

    text = message.text.lower()
    if text in movies:
        bot.send_video(
            message.chat.id,
            movies[text],
            caption="🍿 Marhamat, kino!"
        )
    else:
        bot.send_message(
            message.chat.id,
            "❌ Kino topilmadi. Iltimos boshqa nom yozing."
        )

# ✅ Bot 24/7 ishlashi
bot.infinity_polling()
