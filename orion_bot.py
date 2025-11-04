import telebot

# Вставь сюда свой токен вместо текста внутри кавычек:
bot = telebot.TeleBot("8297505001:AAFNnYHyxe46-w6MBEvcu0ThnouRJoXuHjA")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я Orion — твой AI-ассистент. 🌌")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"Ты сказал: {message.text}")

print("Orion запущен...")
bot.polling()