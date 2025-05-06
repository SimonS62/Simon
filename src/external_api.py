import requests
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


def convert_to_rub(amount, currency):
    """
    Конвертирует сумму из указанной валюты в рубли.

    :param amount: Сумма для конвертации.
    :param currency: Код валюты (например, 'USD', 'EUR').
    :return: Сумма в рублях (float).
    """
    if currency == 'RUB':
        return amount

    # Получаем API ключ из переменной окружения
    api_key = os.getenv('API_KEY')

    if not api_key:
        raise ValueError("API ключ не найден. Убедитесь, что он указан в файле .env.")

    url = f'https://apilayer.com/marketplace/exchangerates_data-api={currency}'

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'rates' in data and currency in data['rates']:
            rate = data['rates'][currency]
            return amount / rate  # Конвертация в рубли
        else:
            raise ValueError(f"Курс для {currency} не найден.")
    else:
        raise Exception("Ошибка при обращении к API.")
