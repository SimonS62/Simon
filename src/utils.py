import json
import os
from external_api import convert_to_rub


def load_transactions(file_path):
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с данными о транзакциях или пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []


# Укажите путь к файлу operations.json
file_path = 'data/operations.json'

# Загрузка транзакций
transactions = load_transactions(file_path)

# Вывод загруженных транзакций
print(transactions)


def get_transaction_amount_in_rub(transaction):
    """
    Возвращает сумму транзакции в рублях.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях (float).
    """
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB')

    return convert_to_rub(amount, currency)
