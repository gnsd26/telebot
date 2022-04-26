import telebot, wikipedia
# Создаем экземпляр бота
TGbot = telebot.TeleBot('5126701142:AAG4ICUHlno1OKdgj3D-rFW0G_su7s17eyQ')

wikipedia.set_lang("ru") # Установка рус.яз в wiki

#-----------------------Functions

def WikipediaAdd(s): #функция для обработки запроса на wiki
    try:
        wikiText = wikipedia.page(s).content[:1000].split('.') # получение символов с сайта и разделение строк/ограничение получаемы символов до 1000
        wikiText = wikiText[:-1] # отбрасывание всего после последней точки
        result = ''

        for i in wikiText: # Отсеиваем строки с заголовками (они обозначаются ==)
            if not('==' in i):
                if(len((i.strip()))>3): # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                   result = result+i+'.'
            else:
                break
        result = '@VTK_WIKIBOT made by @gons1de\n\n' + result + '\n' + wikipedia.page(s).url # формирование сообщения
        return result

    except Exception : # Выдается при ошибке
        return 'Не удалось найти информацию по вашему запросу на сайте\nhttps://ru.wikipedia.org/'

@TGbot.message_handler(commands=["start"]) # Обработка команды /start
def start(m, res=False):
    TGbot.send_message(m.chat.id, 'Отправь интересующее тебя слово')

@TGbot.message_handler(content_types=["text"]) # Получение сообщений от пользователя
def handle_text(message):
    TGbot.send_message(message.chat.id, WikipediaAdd(message.text))

TGbot.polling(none_stop=True, interval=0) # Запуск