import telebot

TOKEN = "BU_YERGA_TOKEN_KEYIN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎬 Kino bot ishlayapti!\nKino nomini yozing."
    )

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(
        message.chat.id,
        "🍿 Kino tez orada qo‘shiladi"
    )

bot.infinity_polling()
