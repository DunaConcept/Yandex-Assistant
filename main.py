from handlers import (
    calculate_expression, get_current_date, get_weather, days_until_summer,
    days_until_new_year, get_current_time, get_translate, get_crypto_price, open_site, flip_coin
)


# основная функция, запускающая ассистента
def personal_assistant():
    print('🤖: Здравствуйте! Вот список моих команд:')
    print('\t • “Какая сейчас погода?”' + ' ' * 12 + '• “Переведи "{фраза}" на {язык}”')
    print('\t • “Сколько будет {пример}”' + ' ' * 10 + '• “Какой сейчас курс {криптовалюта}?”')
    print('\t • “Сколько дней до лета?”' + ' ' * 11 + '• “Открой {название сайта или URL}.”')
    print('\t • “Сколько сейчас времени?”' + ' ' * 9 + '• “Сколько дней до нового года?”')
    print('\t • “Какое сегодня число?”' + ' ' * 12 + '• “Подбрось монетку.”')
    print('❗️Для выхода из программы введите "Стоп".')

    while True:
        cmd = input('⚪: ').strip().lower()

        # остановка программы
        if 'стоп' in cmd:
            print('✅: Ассистент остановлен')
            break
        # обработка других комманд
        elif "погода" in cmd:
            get_weather()
        elif "сколько будет" in cmd:
            calculate_expression(cmd)
        elif "какое сегодня число" in cmd:
            get_current_date()
        elif 'сколько дней до лета' in cmd:
            days_until_summer()
        elif 'сколько дней до нового года' in cmd:
            days_until_new_year()
        elif 'сколько сейчас времени' in cmd:
            get_current_time()
        elif 'переведи' in cmd:
            get_translate(cmd)
        elif 'курс' in cmd:
            get_crypto_price(cmd)
        elif 'открой' in cmd:
            open_site((cmd.split())[-1])
        elif 'монетку' in cmd:
            flip_coin()
        elif 'спасибо' in cmd:
            print("🤖: Пожалуйста! Если возникнут еще вопросы, не стесняйтесь обращаться. Я всегда рад помочь!")
        else:
            print("🤖: Извините, я не могу понять ваш запрос. Попробуйте еще раз.")


# запуск программы
if __name__ == "__main__":
    print('✅: Ассистент запущен.')
    personal_assistant()
