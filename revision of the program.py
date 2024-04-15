import telebot

# Создание экземпляра бота с токеном вашего бота
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Функция для отправки сообщения с примером кода
def send_code_example(message, example_text):
    bot.reply_to(message, example_text)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-помощник по Python. Задавайте вопросы, и я постараюсь помочь вам.")

# Примеры кода
for_example_text = """
Пример использования цикла for в Python:
for i in range(5):
    print(i)
"""

while_example_text = """
Пример использования цикла while в Python:
i = 0
while i < 5:
    print(i)
    i += 1
"""

continue_example_text = """
Пример использования оператора continue в цикле for в Python:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
"""

print_example_text = """
Пример использования функции print() в Python:
print("Привет, мир!")
"""

# Обработчик команды /for
@bot.message_handler(commands=['for'])
def for_example(message):
    send_code_example(message, for_example_text)

# Обработчик команды /while
@bot.message_handler(commands=['while'])
def while_example(message):
    send_code_example(message, while_example_text)

# Обработчик команды /continue
@bot.message_handler(commands=['continue'])
def continue_example(message):
    send_code_example(message, continue_example_text)

# Обработчик команды /print
@bot.message_handler(commands=['print'])
def print_example(message):
    send_code_example(message, print_example_text)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Здесь можно добавить код для обработки запроса и предоставления соответствующих подсказок
    reply = "Прости, я не могу тебе помочь сейчас. Попробуйте позже."
    bot.reply_to(message, reply)

# Запуск бота
bot.polling()
