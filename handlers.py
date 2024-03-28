from googletrans import Translator  # pip install googletrans==4.0.0-rc1
from requests import get, codes  # pip install requests
from webbrowser import open
from random import randint
from time import sleep
import datetime

from config import WEATHER_KEY, CRYPTO_KEY


# функция для выполнения математических вычислений
def calculate_expression(cmd):
    if '?' in cmd:
        expression = cmd[:cmd.find('?')].replace("сколько будет", "")
    else:
        expression = cmd.replace("сколько будет", "")
    try:
        result = eval(expression)
        return print(f"🤖: Результат: {result}")
    except SyntaxError:
        return "🤖: Ошибка в синтаксисе выражения."
    except ZeroDivisionError:
        return "🤖: Делить на ноль нельзя."
    except Exception as e:
        return f"🤖: Произошла ошибка: {str(e)}."


# функция для получения текущей даты
def get_current_date():
    date = [el for el in map(int, datetime.datetime.now().strftime("%d.%m.%Y").split('.'))]
    months = {
        1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля',
        8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
    }
    current_date = f'{date[0]} {months[date[1]]} {date[-1]} г.'

    return print(f"🤖: Сегодня {current_date}")


# функция для получения подходящего под погоду emoji
# используется в get_weather()
def get_emoji(weather_des):
    if 'clouds' in weather_des:
        return '☁️ '
    elif 'rain' in weather_des:
        return '🌧️ '
    elif 'snow' in weather_des:
        return '🌨️ '
    elif 'clear' in weather_des:
        return '☀️ '
    else:
        return ''


# функция для получения погоды
def get_weather():
    print('🤖: Погода в каком городе вас интересует?')
    city = input('⚪: ').strip().lower()
    api = WEATHER_KEY
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'

    try:
        res = get(api_url)
        data = res.json()
        weather_description = data['weather'][0]['description']
        translator = Translator()
        translated_description = translator.translate(weather_description, dest='ru').text
        temperature = data['main']['temp']
        emoji = get_emoji(weather_description)
        response_text = (f"🤖: В городе {city.capitalize()} сейчас {emoji}{translated_description}. "
                         f"Температура: {temperature}°C.")
        return print(response_text)
    except Exception as e:
        error_message = f"Произошла ошибка: {e}"
        if error_message != "Произошла ошибка: 'weather'":
            return print(f"🤖: Произошла ошибка: {e}.")
        else:
            print('🤖: Город введен неверно. Название должно быть в И.п. и без предлогов.')
            return get_weather()


# функция для получения количества дней до лета
def days_until_summer():
    today = datetime.datetime.today()
    current_month = today.month

    if 6 <= current_month <= 9:
        # Уже лето!
        return print('🤖: Уже лето! 😎')
    elif current_month < 6:
        # Рассчитываем количество дней до начала лета
        summer_start = datetime.datetime(today.year, 6, 1)
        days = (summer_start - today).days + 1
        return print(f'🤖: До лета {days} дней.')
    else:
        # Рассчитываем количество дней до следующего лета
        next_year = today.year + 1
        summer_start = datetime.datetime(next_year, 6, 1)
        days = (summer_start - today).days
        return print(f'🤖: До лета {days} дней.')


# функция для получения количества дней до нового года
def days_until_new_year():
    today = datetime.date.today()
    new_year = datetime.date(today.year + 1, 1, 1)

    if today.month == 12 and today.day == 31:
        # уже Новый год!
        return print('🤖: Уже Новый год! 🎉')
    else:
        # считаем сколько дней до лета
        days = (new_year - today).days
        return print(f'🤖: До Нового года {days} дней.')


# функция для получения текущего времени
def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return print(f'🤖: Сейчас {current_time}.')


def get_translate(cmd):
    translator = Translator()
    parts = cmd.split("на")

    if len(parts) != 2:
        return "Некорректный формат команды. Используйте формат: 'Переведи {фраза} на {язык}'"

    phrase = parts[0].strip()[10:-1]  # Вытаскиваем фразу из команды
    language = parts[1].strip()  # Вытаскиваем язык

    language_codes = {
        "английский": "en",
        "испанский": "es",
        "французский": "fr",
        "немецкий": "de",
        "русский": "ru",
        "итальянский": "it",
        "португальский": "pt",
        "китайский": "zh",
        "японский": "ja",
        "арабский": "ar",
        "украинский": "uk",
        "белорусский": "be",
        "казахский": "kk",
        "киргизский": "ky",
        "таджикский": "tg",
        "туркменский": "tk",
        "узбекский": "uz",
        "армянский": "hy",
        "азербайджанский": "az",
        "грузинский": "ka",
        "молдавский": "mo",
        "татарский": "tt",
        "эстонский": "et"
    }

    if language in language_codes.keys():
        translate = translator.translate(phrase, dest=language_codes[language]).text
        return print(f'🤖: "{phrase.capitalize()}" на {language.capitalize()} язык переводится как "{translate}".')
    else:
        print(f'🤖: К сожалению я не поддерживаю {language} язык.')
        print(f'🤖: Вот список языков, которые я поддерживаю:', end=' ')
        return print(*(language_codes.keys()), sep=', ', end='.\n')


# функция для получения курса криптовалюты
def get_crypto_price(cmd):
    if '?' in cmd:
        crypto = (cmd.split())[-1][:-1]
    else:
        crypto = (cmd.split())[-1]
    crypto_codes = {
        "bitcoin": "btc",
        "ethereum": "eth",
        "binance coin": "bnb",
        "solana": "sol",
        "cardano": "ada",
        "xrp": "xrp",
        "polkadot": "dot",
        "avalanche": "avax",
        "dogecoin": "doge",
        "chainlink": "link",
        "litecoin": "ltc",
        "algorand": "algo",
        "cosmos": "atom",
        "bitcoin cash": "bch",
        "stellar": "xlm"
    }
    if crypto in crypto_codes.keys():
        symbol = f'{crypto_codes[crypto].upper()}USDT'
    elif crypto in crypto_codes.values():
        symbol = f'{crypto.upper()}USDT'
    else:
        print('🤖: К сожалению я не поддерживаю курс данной криптовалюты')
        print('🤖: Вот список криптовалют, курсы которых я поддерживаю:', end=' ')
        return print(*crypto_codes, sep=', ')
    api_url = 'https://api.api-ninjas.com/v1/cryptoprice?symbol={}'.format(symbol)
    response = get(api_url, headers={'X-Api-Key': CRYPTO_KEY})
    if response.status_code == codes.ok:
        data = response.json()
        if crypto in crypto_codes.keys():
            return print(f'🤖: Стоимость {crypto.capitalize()}: {round(float(data["price"]))} $')
        elif crypto in crypto_codes.values():
            return print(f'🤖: Стоимость {crypto.upper()}: {round(float(data["price"]))} $')
    else:
        return print("Ошибка:", response.status_code, response.text)


# функция для открытия сайта
def open_site(site):
    if site.startswith('https://'):
        url = site
    elif '.' in site:
        url = f'https://www.{site[:-1]}.com'
    else:
        url = f'https://www.{site}.com'

    print(f'🤖: Открываю {url}.')
    return open(url)


# функция для подбрасывания монетки
def flip_coin():
    print('🤖: Подбрасываю монетку..')
    sleep(3)
    result = randint(0, 1)
    if result == 0:
        return print('🤖: Выпал 🦅 орел.')
    else:
        return print('🤖: Выпала 🪙 решка.')
