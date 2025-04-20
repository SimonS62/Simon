from typing import List, Dict, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> iter:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список транзакций, каждая из которых является словарем.
    :param currency: Валюта для фильтрации транзакций.
    :return: Генератор транзакций, соответствующих заданной валюте.
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions):
    descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

    for description in descriptions:
        yield description


def card_number_generator(start: int, end: int):
    """
    Генератор для создания номеров банковских карт в заданном диапазонe.

    :param start: Начальное значение диапазона (включительно).
    :param end: Конечное значение диапазона (включительно).
    :yield: Номера карт в формате 'XXXX XXXX XXXX XXXX'.

    Примечание: Если start больше end, генератор не выдаст значений.
    """
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"  # Форматируем число с ведущими нулями до 16 цифр
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
