#Важно! Перед запуском бота установим !pip install pyTelegramBotAPI

import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot_token = '6067519772:AAGxmq1cH2-KUr28WGszCvTmxV61csYJIbU' # замените на токен вашего бота

bot = telebot.TeleBot(bot_token)

# создаем список сериалов с названием и ссылкой на них
top10 = [
        {'title': 'Жестокая ночь/Violent Night', 'description': '2022г, боевик, комедия, триллер, США', 'link': 'https://t.ixfilm.org/48260-zhestokaja-noch-2022.html', 'image': 'https://lordfilm.film/uploads/posts/2022-12/1670956446-2065462914.jpg' },
        {'title': 'Топ Ган: Мэверик/Top Gun: Maverick', 'description': '2022г, боевик, драма, США, Гонконг, Китай', 'link': 'https://t.ixfilm.org/47495-top-gan-mjeverik-2022.html', 'image': 'https://lordfilm.film/uploads/posts/2022-06/1654517012-1901584630.jpg'},
        {'title': 'Дом Дракона/House of the Dragon', 'description': '2022г, боевик, драма, мелодрама, приключения, фэнтези, США', 'link': 'https://t.ixfilm.org/47888-dom-drakona-2022.html', 'image': 'https://lordfilm.film/uploads/posts/2022-08/1661446284-1480524006.jpg'},
        {'title': 'Медленные лошади/Slow Horses', 'description': '2022г, драма, триллер, Великобритания, США', 'link': 'https://t.ixfilm.org/47269-medlennye-loshadi-2022.html', 'image': 'https://lordfilm.film/uploads/posts/2022-04/1649759630_cc2964ff7117f880.jpg'},
        {'title': 'Уэнсдэй/Wednesday', 'description': '2022г, детектив, комедия, семейный, триллер, фэнтези, США', 'link': 'https://rezka.ag/series/fantasy/51874-uenzdey-2022.html', 'image': 'https://static.hdrezka.ac/i/2022/11/25/m97fe70560ba8eu82n36t.png'},
        {'title': 'Разделение/Severance', 'description': '2022г, детектив, драма, триллер, фантастика, США', 'link': 'https://hd.ixfilm.org/47153-razdelenie-2022.html', 'image': 'https://lordfilm.film/uploads/posts/2022-03/1647815576-803534129.jpg'},
        {'title': 'Медведь/The Bear', 'description': '2022г, комедия, США', 'link': 'https://hd.ixfilm.org/47736-medved-2022.html', 'image': 'https://lordfilm.film/uploads/posts/2022-07/1658034003-1232947.jpg'},
        {'title': 'Одни из нас/The Last of Us', 'description': '2023г, боевик, драма, приключения, триллер, ужасы, фантастика, Канада, США', 'link': 'https://hd.ixfilm.org/48345-odni-iz-nas-2023.html', 'image': 'https://lordfilm.film/uploads/posts/2023-01/1673876585-1909180673.jpg'},
        {'title': 'Покерфейс/Poker Face', 'description': '2023г, детектив, драма, триллер, США', 'link': 'https://rezka.ag/series/drama/54024-pokerfeys-2023.html', 'image': 'https://avatars.mds.yandex.net/get-kinopoisk-image/4774061/cc3d845f-01f3-4c06-b7e3-89d7a7ce4fb2/600x900'},
        {'title': 'Операция «Фортуна»: Искусство побеждать/Operation Fortune: Ruse de guerre', 'description': '2023г, боевик, комедия, триллер, США, Китай', 'link': 'https://rezka.ag/films/action/44774-operaciya-fortuna-iskusstvo-pobezhdat-2023.html', 'image': 'https://static.hdrezka.ac/i/2022/2/11/l634adeb5f5e8bp33j89q.png'}
        ]
# создаем функцию, которая будет вызываться при отправке команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # создаем объект InlineKeyboardMarkup
    keyboard = InlineKeyboardMarkup()
    
    # создаем кнопки для каждого сериала
    for series in top10:
        # создаем отдельную клавиатуру с кнопками для каждого сериала
        series_keyboard = InlineKeyboardMarkup()
        series_keyboard.add(InlineKeyboardButton(text='Смотреть', url=series['link']))
        keyboard.add(InlineKeyboardButton(text=series['title'], callback_data=series['title']))
        
        # отправляем сообщение с описанием сериала и клавиатурой с кнопкой
        bot.send_message(
            message.chat.id,
            text=f"{series['title']}\n\n{series['description']}\n\n{series['image']}",
            reply_markup=series_keyboard
        )

    # отправляем сообщение с общей клавиатурой
    bot.send_message(message.chat.id, text='Выберите сериал:', reply_markup=keyboard)

#запускаем бота
bot.polling()