import json
import os
import logging

# Создаем логер для модуля utils
logger_utils = logging.getLogger('utils')

# Настраиваем обработчик файла
file_handler = logging.FileHandler('utils.log', encoding='utf-8')

# Создаем форматер с нужным форматом
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Назначаем форматер обработчику
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логеру
logger_utils.addHandler(file_handler)

# Устанавливаем уровень логирования не ниже DEBUG
logger_utils.setLevel(logging.DEBUG)

# Теперь внутри функций модуля используйте logger_utils для логирования


def some_function():
    try:
        # успешное выполнение функции
        logger_utils.info("Функция some_function выполнена успешно.")
        # код функции...
    except Exception as e:
        # ошибка при выполнении функции
        logger_utils.error(f"Ошибка в some_function: {e}")


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
