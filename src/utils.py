import json
import os


def load_transactions(file_path):
    """
    Загружает транзакции из указанного файла JSON.

    :param file_path: Путь к файлу JSON.
    :return: Список словарей с транзакциями или пустой список.
    """
    if not os.path.exists(file_path):
        return []  # Файл не найден, возвращаем пустой список

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.loads(f.read())
            if isinstance(data, list):
                return data  # Возвращаем данные, если это список
            else:
                return []  # Если данные не являются списком, возвращаем пустой список
    except (json.JSONDecodeError, ValueError):
        return []  # Если произошла ошибка при декодировании JSON или другие ошибки, возвращаем пустой список


# Укажите путь к файлу operations.json
file_path = 'data/operations.json'

# Загрузка транзакций
transactions = load_transactions(file_path)

# Вывод загруженных транзакций
print(transactions)
