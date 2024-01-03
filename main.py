import telebot
import requests

BOT_TOKEN = '6887127603:AAE9CYeUZCH4gv2YT62Hn0G_T0s90RwK8z0'
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')



if __name__ == "__main__":
    bot.polling(none_stop=True)

