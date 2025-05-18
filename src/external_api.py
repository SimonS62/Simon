import requests
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

def convert_to_rub(amount, currency):
    """
    Конвертирует указанную сумму из заданной валюты в рубли (RUB).

    :param amount: Сумма для конвертации.
    :param currency: Код валюты (например, 'USD', 'EUR').
    :return: Конвертированная сумма в рублях или None в случае ошибки.
    """
    api_key = os.getenv('API_KEY')  # Получаем API-ключ из переменной окружения
    url = f"https://apilayer.com/marketplace/exchangerates_data-api/convert?to=RUB&from={currency}&amount={amount}"

    headers = {
        "apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()

        if 'result' in data:
            return float(data['result'])  # Возвращаем сумму в рублях
        else:
            print("Ошибка: Не удалось получить результат конвертации.")
            return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def process_transaction(transaction):
    """
    Обрабатывает транзакцию и возвращает сумму в рублях.

    :param transaction: Словарь с данными о транзакции, должен содержать ключи 'amount' и 'currency'.
    :return: Сумма транзакции в рублях или None в случае ошибки.
    """
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency in ['USD', 'EUR']:
        return convert_to_rub(amount, currency)

    # Если валюта уже RUB, просто возвращаем сумму
    if currency == 'RUB':
        return float(amount)

    print("Ошибка: Неподдерживаемая валюта.")
    return None
