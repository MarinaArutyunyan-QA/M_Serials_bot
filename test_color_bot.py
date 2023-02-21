import re
import telegram
import telegram.ext
from telegram.ext import*
# Создаем объект бота
token='5963872203:AAFUqc0jfw-l1qseVpHWdoQ0VGwsLVbetks'
bot = telegram.Bot(token)

# Обработчик команды /start
async def start(update, context):
    await  update.message.reply_text('Привет! Я могу подсказать, какой цвет получится при смешивании двух введенных цветов. Просто введите два цвета через запятую, например: красный, синий.')

# Обработчик сообщений
async def echo(update, context):
    # Получаем текст сообщения
    text = update.message.text

    # Проверяем, что сообщение содержит два цвета, разделенных запятой
    if re.match(r'^\w+,\s*\w+$', text):
        # Разделяем цвета и удаляем пробелы
        colors = [c.strip() for c in text.split(',')]
        # Определяем получившийся цвет
        result = mix_colors(colors[0], colors[1])
        # Отправляем сообщение с результатом
        await update.message.reply_text(f'При смешивании цветов {colors[0]} и {colors[1]} получится цвет {result}.')
    else:
        # Отправляем сообщение с просьбой ввести два цвета
        await update.message.reply_text('Пожалуйста, введите два цвета через запятую, например: красный, синий.')

# Функция для смешивания цветов
def mix_colors(color1, color2):
    # Список возможных цветов и их сочетаний
    color1 = color1.lower()
    color2 = color2.lower()
    colors = {
        ('красный', 'синий'): 'фиолетовый',
        ('красный', 'желтый'): 'оранжевый',
        ('синий', 'желтый'): 'зеленый',
    }
    # Ищем сочетание в списке возможных цветов
    if (color1, color2) in colors:
        return colors[(color1, color2)]
    elif (color2, color1) in colors:
        return colors[(color2, color1)]
    else:
        return 'не удалось определить цвет'


# Создаем диспетчер и добавляем обработчики
application = Application.builder().token(token).build()
application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
# Запускаем бота
print("Я запущен")
application.run_polling()
