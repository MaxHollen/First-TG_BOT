import telebot
import webbrowser

bot = telebot.TeleBot('6167521741:AAFyjt7s7aM0kRghrbXJa0gnESo5vAd6LNE')

@bot.message_handler(commands=['web'])
def web(message):
    webbrowser.open('https://berserk.ru/')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')

@bot.message_handler(commands=['help'])
def help_command(help):
    bot.send_message(help.chat.id, '<b>Весь список доступных команд здесь -></b> <em>/help</em>:\n'
                                   '<em>/help</em> - вызвать помощь\n'
                                   '<em>/start</em> - начать общение\n', parse_mode='html')

@bot.message_handler(commands=['img'])
def img_com(img):
    bot.send_photo(img.chat.id, "http://dreamworlds.ru/uploads/posts/2010-09/1284611024_murini.jpg")

@bot.message_handler(commands=['mes'])
def mes(message):
    bot.send_message(message.chat.id, message)


#В КОНЦЕ ДЕРЖАТЬ!!!!
@bot.message_handler()
def info(message):
    if message.text.lower == "привет" or "хай" or "приве" or "здравствуй" or "здравствуйте" or "hi" or "hello":
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name} {message.from_user.last_name}!")

bot.polling(none_stop=True)