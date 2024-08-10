import telebot
import requests
import json
import datetime

print("Вас приветствует Автобусный трекер (by Kostz)")

API_TOKEN = 'ваш токен'
ALLOWED_CHAT_IDS = [id, id, id]

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id in ALLOWED_CHAT_IDS:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(telebot.types.KeyboardButton("Следующий автобус (ваша осановка) 🚌"))
        markup.add(telebot.types.KeyboardButton("Следующий автобус (ваша остановка) 🚌"))
        bot.send_message(message.chat.id, 'Выберите нужную опцию:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Вы не авторизованы для использования этого бота.')


@bot.message_handler(func=lambda message: message.text == "Следующий автобус (ваша осановка) 🚌")
def avtobus_school(message):
    if message.chat.id in ALLOWED_CHAT_IDS:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Вот следующие автобусы:', reply_markup=markup)

        url = 'https://moscowtransport.app/ваша остановка'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Service-Name':'transport',
            'Access-Control-Allow-Methods':'GET,POST,PATCH,PUT,DELETE,OPTIONS',
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Request-Header':'XAuthToken,DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range',
            'Method-Name':'transport_stop_v2_card'
        }

        params = {}
        r = requests.get(url, params=params, headers = headers)

        js = json.loads(r.text)

        for item in js['routePath']:
            times = ''
            if item['number'] == '944' or item['number'] == '926':
                for bus in item['externalForecast']:
                    tmin = bus['time'] // 60
                    tsec = bus['time'] % 60
                    times = times + '\n🕘 '+str(tmin) + ' минут(ы)  ' + str(tsec)+' секунд(ы)'
                bot.send_message(message.chat.id, ('🚌' + item['number']))
                bot.send_message(message.chat.id, (times))
    else:
        bot.send_message(message.chat.id, 'Вы не авторизованы для использования этой команды.')

@bot.message_handler(func=lambda message: message.text == "Следующий автобус (ваша остановка) 🚌")
def avtobus_sevostopol(message):
    if message.chat.id in ALLOWED_CHAT_IDS:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Вот следующие автобусы:', reply_markup=markup)

        url = 'https://moscowtransport.app/ваша остановка'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Service-Name':'transport',
            'Access-Control-Allow-Methods':'GET,POST,PATCH,PUT,DELETE,OPTIONS',
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Request-Header':'XAuthToken,DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range',
            'Method-Name':'transport_stop_v2_card',
            'Server':'nginx'
        }

        params = {}
        r = requests.get(url, params=params, headers = headers)

        js = json.loads(r.text)

        for item in js['routePath']:
            times = ''
            if item['number'] == '944' or item['number'] == '926':
                for bus in item['externalForecast']:
                    tmin = bus['time'] // 60
                    tsec = bus['time'] % 60
                    times = times + '\n🕘 '+str(tmin) + ' минут(ы)  ' + str(tsec)+' секунд(ы)'
                bot.send_message(message.chat.id, ('🚌' + item['number']))
                bot.send_message(message.chat.id, (times))
    else:
        bot.send_message(message.chat.id, 'Вы не авторизованы для использования этой команды.')

@bot.message_handler(func=lambda message: message.text == "Следующий автобус (ваша остановка) 🚌")
def avtobus_school(message):
    if message.chat.id in ALLOWED_CHAT_IDS:
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, 'Вот следующие автобусы:', reply_markup=markup)

        url = 'https://moscowtransport.app/ваша остановка'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Service-Name':'transport',
            'Access-Control-Allow-Methods':'GET,POST,PATCH,PUT,DELETE,OPTIONS',
            'Access-Control-Allow-Origin':'*',
            'Access-Control-Request-Header':'XAuthToken,DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range',
            'Method-Name':'transport_stop_v2_card'
        }

        params = {}
        r = requests.get(url, params=params, headers = headers)

        js = json.loads(r.text)

        for item in js['routePath']:
            times = ''
            for bus in item['externalForecast']:
                tmin = bus['time'] // 60
                tsec = bus['time'] % 60
                times += f'\n🕘 {tmin} минут(ы) {tsec} секунд(ы)'

            if times.strip():  # Проверка, что строка times не пустая после удаления возможных пробелов и символов перевода строки
                bot.send_message(message.chat.id, f'🚌 {item["number"]}')  # Показывает номер остановки
                bot.send_message(message.chat.id, times)  # Показывает информацию о времени
            else:
                bot.send_message(message.chat.id, f'🚌 {item["number"]}')
                bot.send_message(message.chat.id, 'Нет расписания')
    else:
        bot.send_message(message.chat.id, 'Нет расписания')

bot.polling()
