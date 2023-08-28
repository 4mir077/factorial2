#@factt_bot
#https://web.telegram.org/a/#6235943714
import telebot
bot = telebot.TeleBot('6235943714:AAEcJVapcCLCkTdue_uFk0akn3B8-P9aFvo')
import threading
import functools

result = 0

@functools.lru_cache()
def calculate_factorial(n):
    global result
    result = 1
    for i in range(1, n+1):
        result *= i
    calculate_factorial.cache_clear()

@bot.message_handler(commands=["start"])
@functools.lru_cache()
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я могу посчитать факториал, введите число')
    start.cache_clear()

@bot.message_handler(content_types=['text'])
@functools.lru_cache()
def get_text_messages(message):
    try:
        num = int(message.text)
        
        if num > 1000: 
            bot.send_message(message.chat.id, message.text[:5])
        elif num < -1000:
            bot.send_message(message.chat.id, message.text[:6])
        else:
            thread1 = threading.Thread(target=calculate_factorial, args=(num,))
            thread2 = threading.Thread(target=calculate_factorial, args=(num,))

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()

            bot.send_message(message.chat.id, 'Факториал числа ' + message.text + ': ' + str(result))
    except:
        bot.send_message(message.chat.id, 'Вы ввели не число, попробуйте еще раз')
    get_text_messages.cache_clear()
    

bot.polling(none_stop=True, interval=0)