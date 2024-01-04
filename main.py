import telebot
import smtplib
import imaplib

BOT_TOKEN = '6887127603:AAE9CYeUZCH4gv2YT62Hn0G_T0s90RwK8z0'
bot = telebot.TeleBot(BOT_TOKEN)

smtp_server = 'smtp.yandex.ru'
smtp_port = 465
sender_email = 'hdrezkahelper@yandex.ru'
sender_password = 'tutmpsrroewtvjvd'
receiver_email = 'mirror@hdrezka.org'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}! Я помогу тебе получить актуальную ссылку на HDRezka. Введите /send_email ')


@bot.message_handler(commands=['send_email'])
def send_email(message):
    bot.reply_to(message, 'Введите текст письма')
    bot.register_next_step_handler(message, process_email)

def process_email(message):
    email_text = message.text

    try:
        # Отправка письма
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email_text)
        server.quit()

        bot.reply_to(message, 'Письмо успешно отправлено!')
    except Exception as e:
        bot.reply_to(message, f'Произошла ошибка при отправке письма')


if __name__ == "__main__":
    bot.polling(none_stop=True)
