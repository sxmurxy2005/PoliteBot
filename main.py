from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = TeleBot('7088454922:AAHNYuMENuEbx9rt_9ASR2RDAFXx3iiN3lQ')

class QuizItem():
    def __init__(self, question, options, p, explanation):
        self.question = question
        self.options = options
        self.p = p
        self.explanation = explanation

class Quiz():
    def __init__(self, *items):
        self.is_going = False
        self.items = items
        self.index = 0
    
    def display_question(self, chat_id):
        if self.index < len(self.items):
            item = self.items[self.index]
            markup = ReplyKeyboardMarkup(resize_keyboard = True)
            text = f'🔹 {item.question}'
            for i in range(len(item.options)):
                text += f'\n{str(i + 1)}. {item.options[i]}'
                markup.add(str(i + 1))
            bot.send_message(chat_id, text, reply_markup = markup)
        else:
            self.stop()
            markup = ReplyKeyboardMarkup(resize_keyboard = True)
            markup.add(KeyboardButton('Назад'))
            bot.send_message(chat_id, 'Викторина окончена!', reply_markup = markup)

    def start(self, chat_id):
        self.is_going = True
        self.index = 0
        bot.send_message(chat_id, '🔔 Начинаем! Выбирайте правильные ответы с помощью кнопок!')
        self.display_question(chat_id)
    
    def stop(self):
        self.is_going = False
    
    def accept_answer(self, answer, chat_id):
        if not self.is_going: return False
        item = self.items[self.index]
        if answer not in [str(i + 1) for i in range(len(item.options))]: return False
        if answer == str(item.p + 1):
            bot.send_message(chat_id, '🟢 Правильно!')
        else:
            bot.send_message(chat_id, '🔴 Неправильно!\n' + item.explanation)
        self.index += 1
        self.display_question(chat_id)
        return True

information = '''
    Ниже представлена памятка о том, как общаться в интернете безопасно и вежливо:
    🔸 1. Не доверяйте личной информации: Не раскрывайте свои личные данные, такие как адрес, номер телефона, пароли или пин-коды незнакомым людям в интернете.
    🔸 2. Будьте осмотрительны с фотографиями и видео: Не загружайте личные фотографии или видео, которые могут нарушить вашу частную жизнь или безопасность.
    🔸 3. Избегайте кибербуллинга и провокаций: Не участвуйте в онлайн-драках, не публикуйте оскорбительные комментарии и не распространяйте конфиденциальную информацию о других людях.
    🔸 4. Помните о нормах вежливого общения: Будьте уважительны к собеседникам, избегайте грубых высказываний, используйте позитивный и дружелюбный тон общения.
    🔸 5. Будьте бдительны в отношении мошенников: Не открывайте подозрительные ссылки, не предоставляйте личные данные по запросу и не скачивайте файлы с ненадежных источников.
    🔸 6. Используйте надежные пароли: Создавайте сложные пароли для своих учетных записей, не используйте один пароль для всех сервисов и регулярно меняйте пароли.
    🔸 7. Сообщайте об агрессии и нарушениях: Если вы столкнулись с кибербуллингом, угрозами или другими нарушениями, обратитесь за помощью к модераторам или администрации платформы.
    🔸 8. Обучайте себя и окружающих: Помогайте другим людям разбираться в правилах безопасного и вежливого общения в интернете, делясь своим опытом и знаниями.
    '''
quiz = Quiz(
    QuizItem('Какие личные данные не стоит раскрывать в интернете?', ('Адрес', 'Имя', 'Дата рождения', 'Все вместе'), 3, 'Не стоит раскрывать свой адрес, имя, номер телефона, дату рождения или любую другую личную информацию, которая может быть использована для злоупотреблений или мошенничества.'),
    QuizItem('Что следует делать, если вы столкнулись с кибербуллингом?', ('Игнорировать и перейти на другую страничку', 'Сообщить об этом модераторам или администрации', 'Написать оскорбительный комментарий в ответ', 'Раскрыть больше своей личной информации'), 1, 'Важно сообщить о случаях кибербуллинга модераторам или администрации сайта, чтобы принять меры и защитить себя и других от дальнейших оскорблений и угроз.'),
    QuizItem('Какие правила вежливого общения следует соблюдать в интернете?', ('Использовать грубые выражения', 'Быть уважительным к собеседникам', 'Не отвечать на сообщения', 'Никакие из вышеперечисленных'), 1, 'В интернете так же важно проявлять уважение к другим людям, как и в реальной жизни. Необходимо избегать грубых выражений и оскорблений.'),
    QuizItem('Что нужно делать, если вам приходят подозрительные ссылки или запросы на предоставление личных данных?', ('Открывать все ссылки, чтобы узнать, что за ними скрывается', 'Предоставлять запрошенные данные', 'Сообщать об этом администрации или модераторам', 'Не обращать внимания'), 2, 'Не следует открывать подозрительные ссылки или разглашать свои личные данные. В случае получения подобных запросов, необходимо сообщить об этом администрации сайта.'),
    QuizItem('Зачем важно создавать сложные пароли для учетных записей?', ('Чтобы усложнить жизнь себе', 'Чтобы защитить учетные записи от хакеров и мошенников', 'Чтобы забывать их', 'Все вместе'), 1, 'Сложные пароли сложнее взламывать, что помогает обеспечить безопасность своих учетных записей и предотвратить несанкционированный доступ к личной информации.'),
    QuizItem('Что нужно делать, если вы не согласны с мнением другого человека в интернете?', ('Начать оскорблять и унижать его', 'Выразить свою точку зрения вежливо и уважительно', 'Проигнорировать его сообщение'), 1, 'При несогласии с мнением другого пользователя важно высказывать свою точку зрения вежливо и уважительно, чтобы избежать конфликтов и поддерживать уважительное общение.'),
    QuizItem('Какая из следующих фраз является примером вежливого обращения в интернете?', ('"Что ты несешь, идиот?"', 'Извините, но я не согласен с вашим мнением."', '"Ты ничего не понимаешь, знающие люди говорили бы вот что..."'), 1, 'Вежливое обращение с другими людьми включает в себя уважительное выражение своего мнения без оскорблений и агрессии.')
    )

def display_information(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(KeyboardButton('Назад'))
    bot.send_message(chat_id, information, reply_markup = markup)

def display_main_menu(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(KeyboardButton('Выйти'), KeyboardButton('Полезная информация'), KeyboardButton('Викторина'))
    bot.send_message(chat_id, 'Используйте кнопки!', reply_markup = markup)

def display_goodbye(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(KeyboardButton('/start'))
    bot.send_message(chat_id, "✨ Всего хорошего!", reply_markup = markup)

@bot.message_handler(commands = ['start'])
def on_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, '🚀 Приветствую тебя в Самом Вежливом Боте')
    bot.send_message(chat_id, '❗ Данный чат-бот сделали студенты группы Б9123-01.03.02сп: Шахматов Павел и Кулак Иван')
    bot.send_message(chat_id, '🌎 Основной функционал бота - проведение викторины, в ходе которой пользователь сможет улучшить свое мастерство вежливого и безопасного общения в интернете.')
    display_main_menu(chat_id)

@bot.message_handler(content_types = 'text')
def on_message(message):
    chat_id = message.chat.id
    if message.text == 'Выйти':
        quiz.stop()
        display_goodbye(chat_id)
    elif message.text == 'Полезная информация':
        quiz.stop()
        display_information(chat_id)
    elif message.text == 'Викторина':
        quiz.start(chat_id)
    elif message.text == 'Назад':
        quiz.stop()
        display_main_menu(chat_id)
    elif not quiz.accept_answer(message.text, chat_id):
        bot.send_message(chat_id, '🚫 Некорректное сообщение!')

if __name__ == "__main__":
    bot.infinity_polling()