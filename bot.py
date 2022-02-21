import telebot
from telebot import types
import random
from config import TOKEN
from text import AUTHOR_INFO
from text import HELP_INFO

bot = telebot.TeleBot(TOKEN)

# Create buttons
buttons = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
flip_coin_button = types.KeyboardButton("🪙  -  Бросить монетку")
author_info_button = types.KeyboardButton("🧑🏻‍💻  -  Об Авторе")
help_info_button = types.KeyboardButton("🆘  -  Помощь")
buttons.add(flip_coin_button, author_info_button, help_info_button)


# Start handler
@bot.message_handler(commands="start")
def send_welcome_message(message):
	bot.reply_to(message, "Hello", reply_markup=buttons)


# Flip coin handler
@bot.message_handler(content_types=['text'])
def flip_coin(message):
	if message.text == "🪙  -  Бросить монетку":
		r_list = ["eagle", "reshka"]

		with open("eagle.mp4", "rb") as file:
			e = file.read()

		with open("reshka.mp4", "rb") as file:
			r = file.read()

		if random.choice(r_list) == "eagle":
			bot.send_video(message.chat.id, e, "eagle.mp4")
		else:
			bot.send_video(message.chat.id, r, "reshka.mp4")

	if message.text == "🧑🏻‍💻  -  Об Авторе":
		bot.send_message(message.chat.id, AUTHOR_INFO)

	if message.text == "🆘  -  Помощь":
		bot.send_message(message.chat.id, HELP_INFO)


if __name__ == '__main__':
	bot.polling(none_stop=True)
