import telebot
import datetime
import time
import threading
import random


bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message, "Привет!  Я чат-бот, который будет напоминать тебе пить водичку!")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=["fact"])
def fact_message(message):
    list_1 = ["Вода составляет около 71% поверхности Земли и около 60% человеческого тела.", "Чистая вода сама по себе без запаха и вкуса - любые запахи и вкусы, которые мы ощущаем, обусловлены примесями в воде.", " Вода обладает высокой теплоемкостью, что позволяет ей поглощать и отдавать тепло, что играет важную роль в регуляции климата."]
    random_fact = random.choice(list_1)
    bot.reply_to(message, f"Лови факт о воде: {random_fact}")


@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, "Список доступных команд:\n/start - начать диалог\n/help - показать эту справку\n/fact -узнать полезный факт о воде")


def send_reminders(chat_id):
    rem_1 = "09:00"
    rem_2 = "14:00"
    rem_3 = "20:20"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == rem_1 or now == rem_2 or now == rem_3:
            bot.send_message(chat_id, "Пора попить воды.")
            time.sleep(60)
        time.sleep(1)


bot.polling(non_stop=True)
