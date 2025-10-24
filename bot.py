import telebot

TOKEN = "8224074275:AAHznF097vgJuAAoCX8R4EkuxwjI1NPKqm0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلًا! أنا بوتك. ابعتلي أي رسالة وهرجعها لك 😄")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.infinity_polling()
