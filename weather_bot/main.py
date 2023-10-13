import telebot
from telebot import types
from utils import get_weather

# Replace 'YOUR_TOKEN' with your actual Telegram bot token
TOKEN = '6477909679:AAGeHDayf5q7sU_gFA7fZF1JnC25Y4OL25Q'

# Create a bot instance
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Нажми кнопку 'Получить данные о погоде'.", reply_markup=create_inline_keyboard())


@bot.message_handler(commands=['get_weather'])
def handle_get_weather(message):
    bot.reply_to(message, "Введи город, для которого хочешь получить погоду.")
    bot.register_next_step_handler(message, handle_city_input)


def handle_city_input(message):
    weather = get_weather(message.text)
    bot.reply_to(message, f"Информация о погоде для города {message.text}: {weather}")


@bot.message_handler(func=lambda message: True)
def handle_text_input(message):
    bot.reply_to(message, "I'm sorry, I didn't understand that. Press '/get_weather' to start.",
                 reply_markup=create_inline_keyboard())


def create_inline_keyboard():
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Get Weather", callback_data='get_weather_button')
    markup.add(button)
    return markup


@bot.callback_query_handler(func=lambda call: call.data == 'get_weather_button')
def handle_get_weather_button(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Введи город, для которого хочешь получить погоду.")
    bot.register_next_step_handler(call.message, handle_city_input)


if __name__ == "__main__":
    bot.polling()
