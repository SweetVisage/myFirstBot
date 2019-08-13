
import telebot
import config
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
Token = config.Token
bot = telebot.TeleBot(Token)



@bot.message_handler(func=lambda message: True)
def fn_message(message):
    calc_message = len(message.text)
    if "привет" in message.text:
        bot.reply_to(message, "ТЫ ГДЕ ВОТ ЩАС?")
    elif "а ты?" in message.text:
        bot.reply_to(message, 'НА МЕМОРИАЛЕ')


bot.polling()
