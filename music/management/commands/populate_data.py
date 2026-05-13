from django.core.management.base import BaseCommand
from music.models import Artist, Song


class Command(BaseCommand):
    help = 'Наполняет базу данных артистами СНГ и их песнями'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начинаем наполнение базы данных...')
        
        # Данные артистов СНГ
        artists_data = [
            # Россия
            {
                'name': 'Моргенштерн',
                'country': 'Россия',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Morgenstern_%282020-10%29.jpg/400px-Morgenstern_%282020-10%29.jpg',
                'bio': 'Алишер Тагирович Моргенштерн — российский рэпер, певец, музыкальный продюсер и видеоблогер.',
                'songs': [
                    {'title': 'Cadillac', 'year': 2021, 'album': 'Легендарная пыль'},
                    {'title': 'Дуло', 'year': 2020, 'album': 'Легендарная пыль'},
                    {'title': 'Последняя любовь', 'year': 2021, 'album': ''},
                    {'title': 'Yosemite', 'year': 2021, 'album': ''},
                    {'title': 'Папиному сыну', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Jony (Джонибек Муродов)',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jony_%282020-02-15%29.jpg/400px-Jony_%282020-02-15%29.jpg',
                'bio': 'Джонибек Муродов, более известный под псевдонимом Jony — российский певец и автор песен узбекского происхождения.',
                'songs': [
                    {'title': 'Аллея', 'year': 2019, 'album': 'Список твоих мыслей'},
                    {'title': 'Комета', 'year': 2019, 'album': 'Список твоих мыслей'},
                    {'title': 'Ты меня пленила', 'year': 2020, 'album': ''},
                    {'title': 'Лали', 'year': 2021, 'album': ''},
                    {'title': 'Небесные розы', 'year': 2022, 'album': ''},
                ]
            },
            {
                'name': 'RASA',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/RASA_group.jpg/400px-RASA_group.jpg',
                'bio': 'RASA — российская музыкальная группа, основанная в 2016 году.',
                'songs': [
                    {'title': 'Под фонарём', 'year': 2017, 'album': ''},
                    {'title': 'Королева', 'year': 2018, 'album': ''},
                    {'title': 'Пчеловод', 'year': 2019, 'album': ''},
                    {'title': 'Она не любит виски', 'year': 2020, 'album': ''},
                    {'title': 'Как ты там', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Artik & Asti',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Artik_%26_Asti.jpg/400px-Artik_%26_Asti.jpg',
                'bio': 'Artik & Asti — российская поп-группа, основанная в 2010 году.',
                'songs': [
                    {'title': 'Неделимы', 'year': 2019, 'album': '7 (Part 1)'},
                    {'title': 'Девочка танцуй', 'year': 2020, 'album': '7 (Part 2)'},
                    {'title': 'Истеричка', 'year': 2021, 'album': ''},
                    {'title': 'Гармония', 'year': 2022, 'album': ''},
                    {'title': 'Кукла', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Земфира',
                'country': 'Россия',
                'genre': 'Рок',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Zemfira_2019.jpg/400px-Zemfira_2019.jpg',
                'bio': 'Земфира Талгатовна Рамазанова — российская рок-певица, музыкант, композитор, продюсер и автор песен.',
                'songs': [
                    {'title': 'Хочешь?', 'year': 1999, 'album': 'Земфира'},
                    {'title': 'Ариведерчи', 'year': 1999, 'album': 'Земфира'},
                    {'title': 'Прости меня моя любовь', 'year': 2000, 'album': 'Прости меня моя любовь'},
                    {'title': 'Ромашки', 'year': 2000, 'album': 'Прости меня моя любовь'},
                    {'title': 'Искала', 'year': 2005, 'album': 'Вендетта'},
                ]
            },
            {
                'name': 'Би-2',
                'country': 'Россия',
                'genre': 'Рок',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Bi-2_2019.jpg/400px-Bi-2_2019.jpg',
                'bio': 'Би-2 — советская и российская рок-группа, образованная в 1988 году в Бобруйске.',
                'songs': [
                    {'title': 'Полковнику никто не пишет', 'year': 1998, 'album': 'Би-2'},
                    {'title': 'Серебро', 'year': 2000, 'album': 'Би-2'},
                    {'title': 'Варвара', 'year': 2000, 'album': 'Би-2'},
                    {'title': 'Молитва', 'year': 2003, 'album': 'Молоко'},
                    {'title': 'Лайки', 'year': 2014, 'album': '16+'},
                ]
            },
            
            # Украина
            {
                'name': 'Океан Ельзи',
                'country': 'Украина',
                'genre': 'Рок',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Okean_Elzy_2016.jpg/400px-Okean_Elzy_2016.jpg',
                'bio': 'Океа́н Е́льзи — украинская рок-группа, созданная 12 октября 1994 года во Львове.',
                'songs': [
                    {'title': 'Обійми', 'year': 2013, 'album': 'Земля'},
                    {'title': 'Не твоя війна', 'year': 2016, 'album': 'Без меж'},
                    {'title': 'Відпусти', 'year': 2010, 'album': 'Dolce Vita'},
                    {'title': 'На небі', 'year': 2005, 'album': 'GLORIA'},
                    {'title': 'Майже весна', 'year': 2001, 'album': 'Модель'},
                ]
            },
            {
                'name': 'DOROFEEVA',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/DOROFEEVA_2021.jpg/400px-DOROFEEVA_2021.jpg',
                'bio': 'Наде́жда Влади́мировна Дорофе́ева — украинская певица, дизайнер, блогер и актриса.',
                'songs': [
                    {'title': 'Глубоко', 'year': 2020, 'album': ''},
                    {'title': 'Почему', 'year': 2021, 'album': ''},
                    {'title': 'Любима', 'year': 2022, 'album': ''},
                    {'title': 'Сонцем', 'year': 2023, 'album': ''},
                    {'title': 'Почуття', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'MONATIK',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/MONATIK_2019.jpg/400px-MONATIK_2019.jpg',
                'bio': 'Дмитрий Сергеевич Монатик — украинский певец, танцор, композитор, автор песен.',
                'songs': [
                    {'title': 'Кружит', 'year': 2016, 'album': 'Звучит'},
                    {'title': 'УВЛИУВТ', 'year': 2017, 'album': 'Звучит'},
                    {'title': 'Vitamin D', 'year': 2019, 'album': 'LOVE IT ритм'},
                    {'title': 'Сильно', 'year': 2019, 'album': 'LOVE IT ритм'},
                    {'title': 'ТайУлетаю', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Анна Асти',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Anna_Asti_2022.jpg/400px-Anna_Asti_2022.jpg',
                'bio': 'Анна Асти — украинская певица, бывшая участница группы Artik & Asti.',
                'songs': [
                    {'title': 'Феникс', 'year': 2022, 'album': ''},
                    {'title': 'Царица', 'year': 2022, 'album': ''},
                    {'title': 'По барам', 'year': 2023, 'album': ''},
                    {'title': 'Верю в тебя', 'year': 2023, 'album': ''},
                    {'title': 'Цепи', 'year': 2023, 'album': ''},
                ]
            },
            
            # Беларусь
            {
                'name': 'Max Korzh',
                'country': 'Беларусь',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Max_Korzh_2019.jpg/400px-Max_Korzh_2019.jpg',
                'bio': 'Максим Анатольевич Корж — белорусский рэпер, певец и автор песен.',
                'songs': [
                    {'title': 'Малый повзрослел', 'year': 2013, 'album': 'Живой'},
                    {'title': 'Мотылёк', 'year': 2014, 'album': 'Домашний'},
                    {'title': 'Горы по колено', 'year': 2016, 'album': 'Малый повзрослел 2'},
                    {'title': 'Слово пацана', 'year': 2017, 'album': 'Малый повзрослел 2'},
                    {'title': 'Время', 'year': 2020, 'album': 'Открытка'},
                ]
            },
            {
                'name': 'Беларусы',
                'country': 'Беларусь',
                'genre': 'Поп-рок',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Беларусы',
                'bio': 'Белорусская музыкальная группа.',
                'songs': [
                    {'title': 'Менуэт', 'year': 2018, 'album': ''},
                    {'title': 'Вера', 'year': 2019, 'album': ''},
                ]
            },
            
            # Казахстан
            {
                'name': 'Ninety One',
                'country': 'Казахстан',
                'genre': 'Q-Pop',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Ninety_One_2017.jpg/400px-Ninety_One_2017.jpg',
                'bio': 'Ninety One — казахстанская бой-бенд группа, основанная в 2014 году.',
                'songs': [
                    {'title': 'Айыптама', 'year': 2015, 'album': ''},
                    {'title': 'Қайтадан', 'year': 2016, 'album': ''},
                    {'title': 'Еркелемай', 'year': 2017, 'album': ''},
                    {'title': 'All I Need', 'year': 2018, 'album': ''},
                    {'title': 'Bári Biled', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Dimash Kudaibergen',
                'country': 'Казахстан',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Dimash_Kudaibergen_2019.jpg/400px-Dimash_Kudaibergen_2019.jpg',
                'bio': 'Димаш Кудайберген — казахстанский певец, автор песен и мультиинструменталист.',
                'songs': [
                    {'title': 'SOS d\'un terrien en détresse', 'year': 2017, 'album': ''},
                    {'title': 'Daydidau', 'year': 2017, 'album': ''},
                    {'title': 'Screaming', 'year': 2019, 'album': ''},
                    {'title': 'Be With Me', 'year': 2021, 'album': ''},
                    {'title': 'Okay', 'year': 2022, 'album': ''},
                ]
            },
            
            # Армения
            {
                'name': 'Sirusho',
                'country': 'Армения',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sirusho_2018.jpg/400px-Sirusho_2018.jpg',
                'bio': 'Сирушо — армянская певица, автор песен.',
                'songs': [
                    {'title': 'Qele Qele', 'year': 2008, 'album': ''},
                    {'title': 'PreGomesh', 'year': 2012, 'album': ''},
                    {'title': 'Huh-Hah', 'year': 2016, 'album': ''},
                    {'title': 'Zoma Zoma', 'year': 2018, 'album': ''},
                    {'title': 'Yare Mardun Yare', 'year': 2020, 'album': ''},
                ]
            },
            
            # Азербайджан
            {
                'name': 'Emin Agalarov',
                'country': 'Азербайджан',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Emin_Agalarov_2019.jpg/400px-Emin_Agalarov_2019.jpg',
                'bio': 'Эмин Агаларов — азербайджанский певец и бизнесмен.',
                'songs': [
                    {'title': 'Still', 'year': 2009, 'album': ''},
                    {'title': 'Я лучше всех живу', 'year': 2012, 'album': ''},
                    {'title': 'Забыть тебя', 'year': 2015, 'album': ''},
                    {'title': 'Если ты рядом', 'year': 2018, 'album': ''},
                    {'title': 'Может быть', 'year': 2020, 'album': ''},
                ]
            },
            
            # Грузия
            {
                'name': 'Nina Sublatti',
                'country': 'Грузия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Nina_Sublatti_2015.jpg/400px-Nina_Sublatti_2015.jpg',
                'bio': 'Нина Сублати — грузинская певица, автор песен и фотомодель.',
                'songs': [
                    {'title': 'Warrior', 'year': 2015, 'album': ''},
                    {'title': 'Dark Desire', 'year': 2016, 'album': ''},
                    {'title': 'You Call Me Devil', 'year': 2018, 'album': ''},
                    {'title': 'Vision', 'year': 2020, 'album': ''},
                ]
            },
            
            # Молдова
            {
                'name': 'Carla\'s Dreams',
                'country': 'Молдова',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Carla%27s_Dreams_2016.jpg/400px-Carla%27s_Dreams_2016.jpg',
                'bio': 'Carla\'s Dreams — молдавская музыкальная группа, образованная в 2012 году.',
                'songs': [
                    {'title': 'Sub pielea mea', 'year': 2016, 'album': ''},
                    {'title': 'Acele', 'year': 2017, 'album': ''},
                    {'title': 'Imperfect', 'year': 2018, 'album': ''},
                    {'title': 'Seara de Seara', 'year': 2019, 'album': ''},
                    {'title': 'Pana la Sange', 'year': 2020, 'album': ''},
                ]
            },
            
            # Узбекистан
            {
                'name': 'Shahzoda',
                'country': 'Узбекистан',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Shahzoda_2019.jpg/400px-Shahzoda_2019.jpg',
                'bio': 'Шахзода — узбекская певица и актриса.',
                'songs': [
                    {'title': 'Keragim', 'year': 2003, 'album': ''},
                    {'title': 'Baxtliman', 'year': 2005, 'album': ''},
                    {'title': 'Habibi', 'year': 2012, 'album': ''},
                    {'title': 'Laylim', 'year': 2015, 'album': ''},
                    {'title': 'Birinchi sevgi', 'year': 2018, 'album': ''},
                ]
            },
            
            # Таджикистан
            {
                'name': 'Mehrnigori Rustam',
                'country': 'Таджикистан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Mehrnigori',
                'bio': 'Мехрнигори Рустам — таджикская певица.',
                'songs': [
                    {'title': 'Chashmi Siyoh', 'year': 2015, 'album': ''},
                    {'title': 'Dili Man', 'year': 2017, 'album': ''},
                    {'title': 'Nigori Man', 'year': 2019, 'album': ''},
                ]
            },
            
            # Кыргызстан
            {
                'name': 'Gulzada',
                'country': 'Кыргызстан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Gulzada',
                'bio': 'Гульзада — кыргызская певица.',
                'songs': [
                    {'title': 'Kyzdar ay', 'year': 2016, 'album': ''},
                    {'title': 'Sagyndym', 'year': 2018, 'album': ''},
                    {'title': 'Janym', 'year': 2020, 'album': ''},
                ]
            },
            
            # Туркменистан
            {
                'name': 'Myahri',
                'country': 'Туркменистан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Myahri',
                'bio': 'Мяхри — туркменская певица.',
                'songs': [
                    {'title': 'Aydym', 'year': 2015, 'album': ''},
                    {'title': 'Soygi', 'year': 2017, 'album': ''},
                    {'title': 'Gel', 'year': 2019, 'album': ''},
                ]
            },
            
            # Дополнительные популярные артисты
            {
                'name': 'Сергей Лазарев',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sergey_Lazarev_2019.jpg/400px-Sergey_Lazarev_2019.jpg',
                'bio': 'Сергей Вячеславович Лазарев — российский певец, актёр и телеведущий.',
                'songs': [
                    {'title': 'В самое сердце', 'year': 2013, 'album': ''},
                    {'title': 'You Are the Only One', 'year': 2016, 'album': ''},
                    {'title': 'Сдавайся', 'year': 2017, 'album': ''},
                    {'title': 'Scream', 'year': 2019, 'album': ''},
                    {'title': 'Я не боюсь', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Егор Крид',
                'country': 'Россия',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Egor_Krid_2019.jpg/400px-Egor_Krid_2019.jpg',
                'bio': 'Егор Николаевич Крид — российский рэпер, певец и автор песен.',
                'songs': [
                    {'title': 'Самая самая', 'year': 2014, 'album': ''},
                    {'title': 'Невеста', 'year': 2016, 'album': ''},
                    {'title': 'Потрачу', 'year': 2017, 'album': ''},
                    {'title': 'Цвет настроения синий', 'year': 2018, 'album': ''},
                    {'title': 'Грехи', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'LOBODA',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/LOBODA_2019.jpg/400px-LOBODA_2019.jpg',
                'bio': 'Светлана Сергеевна Лобода — украинская певица, автор песен и композитор.',
                'songs': [
                    {'title': '40 градусов', 'year': 2012, 'album': ''},
                    {'title': 'Парень', 'year': 2014, 'album': ''},
                    {'title': 'Твои глаза', 'year': 2016, 'album': ''},
                    {'title': 'SuperSTAR', 'year': 2019, 'album': ''},
                    {'title': 'Мой', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'The Hardkiss',
                'country': 'Украина',
                'genre': 'Рок',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/The_Hardkiss_2019.jpg/400px-The_Hardkiss_2019.jpg',
                'bio': 'The Hardkiss — украинская рок-группа, образованная в 2011 году.',
                'songs': [
                    {'title': 'Make-Up', 'year': 2013, 'album': ''},
                    {'title': 'Stones', 'year': 2014, 'album': ''},
                    {'title': 'Rain', 'year': 2016, 'album': ''},
                    {'title': 'Журавлi', 'year': 2018, 'album': ''},
                    {'title': 'Кобра', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Filatov & Karas',
                'country': 'Россия',
                'genre': 'EDM',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Filatov+%26+Karas',
                'bio': 'Filatov & Karas — российский DJ и продюсерский дуэт.',
                'songs': [
                    {'title': 'Tell It To My Heart', 'year': 2016, 'album': ''},
                    {'title': 'Lirika', 'year': 2017, 'album': ''},
                    {'title': 'Time Won\'t Wait', 'year': 2019, 'album': ''},
                    {'title': 'Мимо меня', 'year': 2020, 'album': ''},
                    {'title': 'I Keep On', 'year': 2022, 'album': ''},
                ]
            },
            {
                'name': 'Макс Барских',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Max_Barskih_2019.jpg/400px-Max_Barskih_2019.jpg',
                'bio': 'Макс Барских — украинский певец, автор песен и композитор.',
                'songs': [
                    {'title': 'Теряю тебя', 'year': 2011, 'album': ''},
                    {'title': 'Глаза-убийцы', 'year': 2013, 'album': ''},
                    {'title': 'Хочу танцевать', 'year': 2015, 'album': ''},
                    {'title': 'Неверная', 'year': 2017, 'album': ''},
                    {'title': 'Полураздета', 'year': 2019, 'album': ''},
                ]
            },
            {
                'name': 'Мот',
                'country': 'Россия',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Mot_2019.jpg/400px-Mot_2019.jpg',
                'bio': 'Мот — российский рэпер и автор песен.',
                'songs': [
                    {'title': 'Капкан', 'year': 2014, 'album': ''},
                    {'title': 'День и ночь', 'year': 2016, 'album': ''},
                    {'title': 'На дне', 'year': 2017, 'album': ''},
                    {'title': 'Понедельник-вторник', 'year': 2019, 'album': ''},
                    {'title': 'Август - это ты', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'HammAli & Navai',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=HammAli+%26+Navai',
                'bio': 'HammAli & Navai — российский музыкальный дуэт.',
                'songs': [
                    {'title': 'Девочка-война', 'year': 2017, 'album': ''},
                    {'title': 'Пустите меня на танцпол', 'year': 2018, 'album': ''},
                    {'title': 'Нтмл', 'year': 2019, 'album': ''},
                    {'title': 'До луны', 'year': 2020, 'album': ''},
                    {'title': 'Птичка', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Galibri & Mavik',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Galibri+%26+Mavik',
                'bio': 'Galibri & Mavik — российский музыкальный дуэт.',
                'songs': [
                    {'title': 'Федерико Феллини', 'year': 2021, 'album': ''},
                    {'title': 'Взгляни на небо', 'year': 2022, 'album': ''},
                    {'title': 'Ромашки', 'year': 2023, 'album': ''},
                    {'title': 'Прятки', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'Моя Мишель',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Моя+Мишель',
                'bio': 'Моя Мишель — российская поп-группа.',
                'songs': [
                    {'title': 'Снегири', 'year': 2019, 'album': ''},
                    {'title': 'Зима в сердце', 'year': 2020, 'album': ''},
                    {'title': 'Ветер меняет направление', 'year': 2021, 'album': ''},
                    {'title': 'Пташка', 'year': 2022, 'album': ''},
                    {'title': 'Снегопад', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'Dabro',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Dabro',
                'bio': 'Dabro — российский музыкальный дуэт братьев Михайловых.',
                'songs': [
                    {'title': 'Мне не страшно', 'year': 2019, 'album': ''},
                    {'title': 'Юность', 'year': 2020, 'album': ''},
                    {'title': 'На часах ноль-ноль', 'year': 2021, 'album': ''},
                    {'title': 'Давай запоём', 'year': 2022, 'album': ''},
                    {'title': 'Мне не смешно', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': '5утра',
                'country': 'Россия',
                'genre': 'Поп-рок',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=5утра',
                'bio': '5утра — российская музыкальная группа.',
                'songs': [
                    {'title': 'Ай красотка', 'year': 2020, 'album': ''},
                    {'title': 'Давай сбежим', 'year': 2021, 'album': ''},
                    {'title': 'Я тебя по голосу найду', 'year': 2022, 'album': ''},
                    {'title': 'Один раз', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'Polina Gagarina',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Polina_Gagarina_2019.jpg/400px-Polina_Gagarina_2019.jpg',
                'bio': 'Полина Сергеевна Гагарина — российская певица, актриса и модель.',
                'songs': [
                    {'title': 'Кукушка', 'year': 2015, 'album': ''},
                    {'title': 'A Million Voices', 'year': 2015, 'album': ''},
                    {'title': 'Обезоружена', 'year': 2017, 'album': ''},
                    {'title': 'Драмы больше нет', 'year': 2019, 'album': ''},
                    {'title': 'Смотри', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Basta',
                'country': 'Россия',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Basta_2019.jpg/400px-Basta_2019.jpg',
                'bio': 'Баста — российский рэпер, певец, актёр и продюсер.',
                'songs': [
                    {'title': 'Моя игра', 'year': 2006, 'album': ''},
                    {'title': 'Сансара', 'year': 2016, 'album': ''},
                    {'title': 'Выпускной', 'year': 2017, 'album': ''},
                    {'title': 'Не пара', 'year': 2019, 'album': ''},
                    {'title': 'Ты была права', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Любэ',
                'country': 'Россия',
                'genre': 'Рок',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Lube_2019.jpg/400px-Lube_2019.jpg',
                'bio': 'Любэ — советская и российская рок-группа.',
                'songs': [
                    {'title': 'Комбат', 'year': 1996, 'album': ''},
                    {'title': 'Там за туманами', 'year': 1997, 'album': ''},
                    {'title': 'Конь', 'year': 1994, 'album': ''},
                    {'title': 'Березы', 'year': 2002, 'album': ''},
                    {'title': 'Давай за...', 'year': 2002, 'album': ''},
                ]
            },
            {
                'name': 'Валерий Меладзе',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Valery_Meladze_2019.jpg/400px-Valery_Meladze_2019.jpg',
                'bio': 'Валерий Меладзе — российский певец и продюсер грузинского происхождения.',
                'songs': [
                    {'title': 'Салют, Вера!', 'year': 1993, 'album': ''},
                    {'title': 'Сэра', 'year': 1996, 'album': ''},
                    {'title': 'Красиво', 'year': 2003, 'album': ''},
                    {'title': 'Небеса', 'year': 2009, 'album': ''},
                    {'title': 'Свеча горела', 'year': 2017, 'album': ''},
                ]
            },
            {
                'name': 'Ирина Аллегрова',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Ирина+Аллегрова',
                'bio': 'Ирина Аллегрова — российская певица и актриса.',
                'songs': [
                    {'title': 'Младший лейтенант', 'year': 1991, 'album': ''},
                    {'title': 'Суженый мой', 'year': 1992, 'album': ''},
                    {'title': 'Угонщица', 'year': 1994, 'album': ''},
                    {'title': 'Я тучи разведу', 'year': 1995, 'album': ''},
                    {'title': 'С днём рождения!', 'year': 1999, 'album': ''},
                ]
            },
            {
                'name': 'Филипп Киркоров',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Philipp_Kirkorov_2019.jpg/400px-Philipp_Kirkorov_2019.jpg',
                'bio': 'Филипп Киркоров — российский певец и актёр болгарского происхождения.',
                'songs': [
                    {'title': 'Атлантида', 'year': 1994, 'album': ''},
                    {'title': 'Единственная моя', 'year': 1996, 'album': ''},
                    {'title': 'Зайка моя', 'year': 1997, 'album': ''},
                    {'title': 'Цвет настроения синий', 'year': 2018, 'album': ''},
                    {'title': 'Робот', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Лолита',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Lolita_2019.jpg/400px-Lolita_2019.jpg',
                'bio': 'Лолита — российская певица, актриса и телеведущая.',
                'songs': [
                    {'title': 'Маленький мальчик', 'year': 1998, 'album': ''},
                    {'title': 'Ориентация север', 'year': 1999, 'album': ''},
                    {'title': 'Пошлю его на...', 'year': 2003, 'album': ''},
                    {'title': 'На скотч', 'year': 2017, 'album': ''},
                    {'title': 'Раневская', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Stas Mikhailov',
                'country': 'Россия',
                'genre': 'Шансон',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Stas_Mikhailov_2019.jpg/400px-Stas_Mikhailov_2019.jpg',
                'bio': 'Стас Михайлов — российский певец и композитор.',
                'songs': [
                    {'title': 'Всё для тебя', 'year': 2004, 'album': ''},
                    {'title': 'Ну вот и всё', 'year': 2005, 'album': ''},
                    {'title': 'Только ты', 'year': 2009, 'album': ''},
                    {'title': 'Дай мне', 'year': 2013, 'album': ''},
                    {'title': 'Берега мечты', 'year': 2017, 'album': ''},
                ]
            },
            {
                'name': 'Nikolai Baskov',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Nikolai_Baskov_2019.jpg/400px-Nikolai_Baskov_2019.jpg',
                'bio': 'Николай Басков — российский оперный и эстрадный певец.',
                'songs': [
                    {'title': 'Тебе одной', 'year': 2001, 'album': ''},
                    {'title': 'Натуральный блондин', 'year': 2004, 'album': ''},
                    {'title': 'Ждать тебя', 'year': 2008, 'album': ''},
                    {'title': 'Николай', 'year': 2015, 'album': ''},
                    {'title': 'Играй, музыкант!', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Леонид Агутин',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Leonid_Agutin_2019.jpg/400px-Leonid_Agutin_2019.jpg',
                'bio': 'Леонид Агутин — российский певец, музыкант и композитор.',
                'songs': [
                    {'title': 'Хоп хей лала лей', 'year': 1993, 'album': ''},
                    {'title': 'Половина сердца', 'year': 1995, 'album': ''},
                    {'title': 'Аэропорты', 'year': 2003, 'album': ''},
                    {'title': 'Я буду всё помнить', 'year': 2012, 'album': ''},
                    {'title': 'На сиреневой луне', 'year': 2019, 'album': ''},
                ]
            },
            {
                'name': 'Валерия',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Valeria_2019.jpg/400px-Valeria_2019.jpg',
                'bio': 'Валерия — российская певица и модель.',
                'songs': [
                    {'title': 'Самолёт', 'year': 1992, 'album': ''},
                    {'title': 'Часики', 'year': 1995, 'album': ''},
                    {'title': 'Метелица', 'year': 2000, 'album': ''},
                    {'title': 'Чёрно-белый цвет', 'year': 2013, 'album': ''},
                    {'title': 'От зари до зари', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Дима Билан',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dima_Bilan_2019.jpg/400px-Dima_Bilan_2019.jpg',
                'bio': 'Дима Билан — российский певец и актёр.',
                'songs': [
                    {'title': 'Невозможное возможно', 'year': 2006, 'album': ''},
                    {'title': 'Believe', 'year': 2008, 'album': ''},
                    {'title': 'Я просто люблю тебя', 'year': 2011, 'album': ''},
                    {'title': 'Неделимые', 'year': 2013, 'album': ''},
                    {'title': 'Молния', 'year': 2017, 'album': ''},
                ]
            },
            {
                'name': 'Сергей Трофимов',
                'country': 'Россия',
                'genre': 'Авторская песня',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Сергей+Трофимов',
                'bio': 'Сергей Трофимов — российский бард и певец.',
                'songs': [
                    {'title': 'Город Сочи', 'year': 2005, 'album': ''},
                    {'title': 'Три белых коня', 'year': 2006, 'album': ''},
                    {'title': 'Родина', 'year': 2008, 'album': ''},
                    {'title': 'Московская песня', 'year': 2010, 'album': ''},
                    {'title': 'Песня о дружбе', 'year': 2015, 'album': ''},
                ]
            },
            {
                'name': 'Григорий Лепс',
                'country': 'Россия',
                'genre': 'Шансон',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Grigory_Leps_2019.jpg/400px-Grigory_Leps_2019.jpg',
                'bio': 'Григорий Лепс — российский певец, музыкант и композитор.',
                'songs': [
                    {'title': 'Раздумья мои...', 'year': 1995, 'album': ''},
                    {'title': 'Я счастливый', 'year': 2001, 'album': ''},
                    {'title': 'Самый лучший день', 'year': 2003, 'album': ''},
                    {'title': 'Я уеду жить в Лондон', 'year': 2012, 'album': ''},
                    {'title': 'Водопадом', 'year': 2018, 'album': ''},
                ]
            },
            {
                'name': 'Ани Лорак',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Ani_Lorak_2019.jpg/400px-Ani_Lorak_2019.jpg',
                'bio': 'Ани Лорак — украинская певица и актриса.',
                'songs': [
                    {'title': 'Зажигай сердце', 'year': 2005, 'album': ''},
                    {'title': 'Солнце', 'year': 2009, 'album': ''},
                    {'title': 'Обними меня крепче', 'year': 2014, 'album': ''},
                    {'title': 'Удержи моё сердце', 'year': 2015, 'album': ''},
                    {'title': 'Сумасшедшая', 'year': 2017, 'album': ''},
                ]
            },
            {
                'name': 'Иван Дорн',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Ivan_Dorn_2019.jpg/400px-Ivan_Dorn_2019.jpg',
                'bio': 'Иван Дорн — украинский певец, DJ и продюсер.',
                'songs': [
                    {'title': 'Стыцамен', 'year': 2011, 'album': ''},
                    {'title': 'Бигуди', 'year': 2012, 'album': ''},
                    {'title': 'Не надо стесняться', 'year': 2013, 'album': ''},
                    {'title': 'Groovy', 'year': 2017, 'album': ''},
                    {'title': ' Beverly ', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'KAZKA',
                'country': 'Украина',
                'genre': 'Поп-фолк',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KAZKA_2019.jpg/400px-KAZKA_2019.jpg',
                'bio': 'KAZKA — украинская музыкальная группа.',
                'songs': [
                    {'title': 'Плакала', 'year': 2018, 'album': ''},
                    {'title': 'Дива', 'year': 2019, 'album': ''},
                    {'title': 'Пісня Сміливих Дівчат', 'year': 2020, 'album': ''},
                    {'title': 'Остров', 'year': 2021, 'album': ''},
                    {'title': 'Май', 'year': 2022, 'album': ''},
                ]
            },
            {
                'name': 'Go_A',
                'country': 'Украина',
                'genre': 'Фолк-электроника',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Go_A_2021.jpg/400px-Go_A_2021.jpg',
                'bio': 'Go_A — украинская фолк-электронная группа.',
                'songs': [
                    {'title': 'Solovey', 'year': 2020, 'album': ''},
                    {'title': 'SHUM', 'year': 2021, 'album': ''},
                    {'title': 'Kalyna', 'year': 2022, 'album': ''},
                    {'title': 'Rusalochki', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'Jerry Heil',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jerry_Heil_2020.jpg/400px-Jerry_Heil_2020.jpg',
                'bio': 'Jerry Heil — украинская певица и автор песен.',
                'songs': [
                    {'title': 'Охрана, отмена', 'year': 2019, 'album': ''},
                    {'title': 'Мрія', 'year': 2020, 'album': ''},
                    {'title': 'Культурна нація', 'year': 2021, 'album': ''},
                    {'title': 'Калина', 'year': 2022, 'album': ''},
                    {'title': 'Козацькому роду', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'alyona alyona',
                'country': 'Украина',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Alyona_alyona_2019.jpg/400px-Alyona_alyona_2019.jpg',
                'bio': 'alyona alyona — украинская рэп-исполнительница.',
                'songs': [
                    {'title': 'Рибки', 'year': 2018, 'album': ''},
                    {'title': 'Відчиняй', 'year': 2019, 'album': ''},
                    {'title': 'Падло', 'year': 2020, 'album': ''},
                    {'title': 'Дикі танці', 'year': 2021, 'album': ''},
                    {'title': 'Порох', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'Jamala',
                'country': 'Украина',
                'genre': 'Поп-джаз',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jamala_2016.jpg/400px-Jamala_2016.jpg',
                'bio': 'Jamala — украинская певица крымскотатарского происхождения.',
                'songs': [
                    {'title': 'Smile', 'year': 2011, 'album': ''},
                    {'title': '1944', 'year': 2016, 'album': ''},
                    {'title': 'I Believe in U', 'year': 2017, 'album': ''},
                    {'title': 'Solo', 'year': 2019, 'album': ''},
                    {'title': 'Жалі', 'year': 2023, 'album': ''},
                ]
            },
            {
                'name': 'Tina Karol',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Tina_Karol_2019.jpg/400px-Tina_Karol_2019.jpg',
                'bio': 'Tina Karol — украинская певица и актриса.',
                'songs': [
                    {'title': 'Пупсик', 'year': 2006, 'album': ''},
                    {'title': 'Ночь', 'year': 2007, 'album': ''},
                    {'title': 'Выше облаков', 'year': 2016, 'album': ''},
                    {'title': 'Сила высоты', 'year': 2019, 'album': ''},
                    {'title': 'Идти', 'year': 2022, 'album': ''},
                ]
            },
            {
                'name': 'Время и Стекло',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Vremya_i_Steklo_2019.jpg/400px-Vremya_i_Steklo_2019.jpg',
                'bio': 'Время и Стекло — украинский поп-дуэт.',
                'songs': [
                    {'title': 'Имя 505', 'year': 2015, 'album': ''},
                    {'title': 'На стиле', 'year': 2016, 'album': ''},
                    {'title': 'Тролль', 'year': 2017, 'album': ''},
                    {'title': 'Дим', 'year': 2018, 'album': ''},
                    {'title': 'Лох', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Mozgi',
                'country': 'Украина',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Mozgi_2019.jpg/400px-Mozgi_2019.jpg',
                'bio': 'Mozgi — украинская музыкальная группа.',
                'songs': [
                    {'title': 'Хала-хала', 'year': 2016, 'album': ''},
                    {'title': 'Полубрат', 'year': 2017, 'album': ''},
                    {'title': 'Аябо', 'year': 2018, 'album': ''},
                    {'title': 'Попа как у Ким', 'year': 2019, 'album': ''},
                    {'title': 'Завтра', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Скриптонит',
                'country': 'Казахстан',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Scriptonite_2019.jpg/400px-Scriptonite_2019.jpg',
                'bio': 'Скриптонит — казахстанский рэпер и продюсер.',
                'songs': [
                    {'title': 'Вечеринка', 'year': 2014, 'album': ''},
                    {'title': 'Танцуй сама', 'year': 2015, 'album': ''},
                    {'title': 'Лёд', 'year': 2016, 'album': ''},
                    {'title': 'Положение', 'year': 2019, 'album': ''},
                    {'title': 'Аутро', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Jah Khalib',
                'country': 'Казахстан',
                'genre': 'Рэп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Jah_Khalib_2019.jpg/400px-Jah_Khalib_2019.jpg',
                'bio': 'Jah Khalib — казахстанский рэпер и певец.',
                'songs': [
                    {'title': 'Созвездие ангела', 'year': 2014, 'album': ''},
                    {'title': 'Твои сонные глаза', 'year': 2015, 'album': ''},
                    {'title': 'Медина', 'year': 2016, 'album': ''},
                    {'title': 'Лейла', 'year': 2018, 'album': ''},
                    {'title': 'Песня о тебе', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Ирина Кайратовна',
                'country': 'Казахстан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Ирина+Кайратовна',
                'bio': 'Ирина Кайратовна — казахстанская певица.',
                'songs': [
                    {'title': 'Кок ту', 'year': 2019, 'album': ''},
                    {'title': 'Айтпай', 'year': 2020, 'album': ''},
                    {'title': 'Казакша', 'year': 2021, 'album': ''},
                    {'title': 'Сен де бар ма?', 'year': 2022, 'album': ''},
                ]
            },
            {
                'name': 'Rauf & Faik',
                'country': 'Россия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Rauf_%26_Faik_2019.jpg/400px-Rauf_%26_Faik_2019.jpg',
                'bio': 'Rauf & Faik — российский музыкальный дуэт братьев-близнецов азербайджанского происхождения.',
                'songs': [
                    {'title': 'Детство', 'year': 2017, 'album': ''},
                    {'title': 'Жизнь в моей голове', 'year': 2018, 'album': ''},
                    {'title': 'Я люблю тебя', 'year': 2019, 'album': ''},
                    {'title': 'Если тебе будет грустно', 'year': 2020, 'album': ''},
                    {'title': 'Никто, кроме нас', 'year': 2022, 'album': ''},
                ]
            },
            {
                'name': 'Miyagi & Andy Panda',
                'country': 'Россия',
                'genre': 'Рэп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Miyagi+%26+Andy+Panda',
                'bio': 'Miyagi & Andy Panda — российский рэп-дуэт.',
                'songs': [
                    {'title': 'I Got Love', 'year': 2016, 'album': ''},
                    {'title': 'Там ревели горы', 'year': 2018, 'album': ''},
                    {'title': 'Фея', 'year': 2019, 'album': ''},
                    {'title': 'Патрон', 'year': 2020, 'album': ''},
                    {'title': 'Тамада', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Тима Белорусских',
                'country': 'Беларусь',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Tima_Belorusskikh_2019.jpg/400px-Tima_Belorusskikh_2019.jpg',
                'bio': 'Тима Белорусских — белорусский певец и автор песен.',
                'songs': [
                    {'title': 'Мокрые кроссы', 'year': 2018, 'album': ''},
                    {'title': 'Незабудка', 'year': 2019, 'album': ''},
                    {'title': 'Алёнка', 'year': 2020, 'album': ''},
                    {'title': 'Витаминка', 'year': 2021, 'album': ''},
                    {'title': 'Потеряли пацана', 'year': 2022, 'album': ''},
                ]
            },
            {
                'name': 'Мария Захарова',
                'country': 'Беларусь',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Мария+Захарова',
                'bio': 'Мария Захарова — белорусская певица.',
                'songs': [
                    {'title': 'Почему?', 'year': 2019, 'album': ''},
                    {'title': 'Ветер', 'year': 2020, 'album': ''},
                    {'title': 'Танцы', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'NAVIBAND',
                'country': 'Беларусь',
                'genre': 'Поп-фолк',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/NAVIBAND_2017.jpg/400px-NAVIBAND_2017.jpg',
                'bio': 'NAVIBAND — белорусская музыкальная группа.',
                'songs': [
                    {'title': 'Гісторыя майго жыцця', 'year': 2013, 'album': ''},
                    {'title': 'Абдыманне', 'year': 2016, 'album': ''},
                    {'title': 'Бяжы', 'year': 2017, 'album': ''},
                    {'title': 'Да відэль', 'year': 2020, 'album': ''},
                ]
            },
            {
                'name': 'Arash',
                'country': 'Азербайджан',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Arash_2019.jpg/400px-Arash_2019.jpg',
                'bio': 'Arash — ирано-азербайджанский певец и продюсер.',
                'songs': [
                    {'title': 'Boro Boro', 'year': 2004, 'album': ''},
                    {'title': 'Temptation', 'year': 2005, 'album': ''},
                    {'title': 'Pure Love', 'year': 2008, 'album': ''},
                    {'title': 'Broken Angel', 'year': 2010, 'album': ''},
                    {'title': 'Se Fue', 'year': 2018, 'album': ''},
                ]
            },
            {
                'name': 'Eldar Gasimov',
                'country': 'Азербайджан',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Eldar_Gasimov_2011.jpg/400px-Eldar_Gasimov_2011.jpg',
                'bio': 'Eldar Gasimov — азербайджанский певец, победитель Евровидения 2011.',
                'songs': [
                    {'title': 'Running Scared', 'year': 2011, 'album': ''},
                    {'title': 'In Your Head', 'year': 2015, 'album': ''},
                    {'title': 'The One', 'year': 2019, 'album': ''},
                ]
            },
            {
                'name': 'Sofi Mkheyan',
                'country': 'Армения',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Sofi+Mkheyan',
                'bio': 'Sofi Mkheyan — армянская певица.',
                'songs': [
                    {'title': 'Hayastan', 'year': 2010, 'album': ''},
                    {'title': '2012', 'year': 2012, 'album': ''},
                    {'title': 'Gisher', 'year': 2015, 'album': ''},
                    {'title': 'Tesilq', 'year': 2018, 'album': ''},
                ]
            },
            {
                'name': 'Sevak Khanagyan',
                'country': 'Армения',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Sevak_Khanagyan_2018.jpg/400px-Sevak_Khanagyan_2018.jpg',
                'bio': 'Sevak Khanagyan — армянский певец и композитор.',
                'songs': [
                    {'title': 'Qami', 'year': 2018, 'album': ''},
                    {'title': 'Amena', 'year': 2019, 'album': ''},
                    {'title': 'Dzerqer', 'year': 2020, 'album': ''},
                    {'title': 'Siro Kino', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Tamta',
                'country': 'Грузия',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Tamta_2019.jpg/400px-Tamta_2019.jpg',
                'bio': 'Tamta — грузинская певица греческого происхождения.',
                'songs': [
                    {'title': 'With Love', 'year': 2017, 'album': ''},
                    {'title': 'Replay', 'year': 2019, 'album': ''},
                    {'title': 'El Diablo', 'year': 2021, 'album': ''},
                ]
            },
            {
                'name': 'Cătălina Toma',
                'country': 'Молдова',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Cătălina+Toma',
                'bio': 'Cătălina Toma — молдавская певица.',
                'songs': [
                    {'title': 'Dragostea', 'year': 2015, 'album': ''},
                    {'title': 'Amor', 'year': 2017, 'album': ''},
                    {'title': 'Vino', 'year': 2019, 'album': ''},
                ]
            },
            {
                'name': 'Lidia Buble',
                'country': 'Молдова',
                'genre': 'Поп',
                'photo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Lidia_Buble_2019.jpg/400px-Lidia_Bubble_2019.jpg',
                'bio': 'Lidia Buble — молдавская певица.',
                'songs': [
                    {'title': 'Le-am spus și fetelor', 'year': 2014, 'album': ''},
                    {'title': 'Kamelia', 'year': 2015, 'album': ''},
                    {'title': 'Asta sunt eu', 'year': 2017, 'album': ''},
                    {'title': 'Sub apa', 'year': 2019, 'album': ''},
                ]
            },
            {
                'name': 'Rayhon',
                'country': 'Узбекистан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Rayhon',
                'bio': 'Rayhon — узбекская певица и актриса.',
                'songs': [
                    {'title': 'Unutaman', 'year': 2004, 'album': ''},
                    {'title': 'Aldading', 'year': 2007, 'album': ''},
                    {'title': 'Sevgi', 'year': 2010, 'album': ''},
                    {'title': 'Yurak', 'year': 2015, 'album': ''},
                ]
            },
            {
                'name': 'Ziyoda',
                'country': 'Узбекистан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Ziyoda',
                'bio': 'Ziyoda — узбекская певица.',
                'songs': [
                    {'title': 'Sevgi', 'year': 2008, 'album': ''},
                    {'title': 'Yomgir', 'year': 2011, 'album': ''},
                    {'title': 'Dona', 'year': 2014, 'album': ''},
                    {'title': 'Qaytmaydi', 'year': 2017, 'album': ''},
                ]
            },
            {
                'name': 'Tahmina Niyazova',
                'country': 'Таджикистан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Tahmina+Niyazova',
                'bio': 'Tahmina Niyazova — таджикская певица.',
                'songs': [
                    {'title': 'Dili Man', 'year': 2014, 'album': ''},
                    {'title': 'Jonam', 'year': 2016, 'album': ''},
                    {'title': 'Oshiqam', 'year': 2018, 'album': ''},
                ]
            },
            {
                'name': 'Gulzhanat Surantaeva',
                'country': 'Кыргызстан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Gulzhanat',
                'bio': 'Gulzhanat Surantaeva — кыргызская певица.',
                'songs': [
                    {'title': 'Kyzdar', 'year': 2015, 'album': ''},
                    {'title': 'Suyum', 'year': 2017, 'album': ''},
                    {'title': 'Janym', 'year': 2019, 'album': ''},
                ]
            },
            {
                'name': 'Lilia',
                'country': 'Туркменистан',
                'genre': 'Поп',
                'photo': 'https://via.placeholder.com/400x400/667eea/ffffff?text=Lilia',
                'bio': 'Lilia — туркменская певица.',
                'songs': [
                    {'title': 'Soygi', 'year': 2016, 'album': ''},
                    {'title': 'Gel', 'year': 2018, 'album': ''},
                    {'title': 'Yaz', 'year': 2020, 'album': ''},
                ]
            },
        ]
        
        # Очищаем существующие данные
        Song.objects.all().delete()
        Artist.objects.all().delete()
        
        # Создаем артистов и их песни
        total_songs = 0
        for artist_data in artists_data:
            songs_data = artist_data.pop('songs')
            artist = Artist.objects.create(**artist_data)
            
            for song_data in songs_data:
                Song.objects.create(artist=artist, **song_data)
                total_songs += 1
            
            self.stdout.write(f'Создан артист: {artist.name} ({len(songs_data)} песен)')
        
        self.stdout.write(self.style.SUCCESS(
            f'\n✅ Успешно создано {len(artists_data)} артистов и {total_songs} песен!'
        ))
