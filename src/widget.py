# src/widget.py
from datetime import datetime

from src.masks import mask_account_number, mask_card_number


def mask_account_card(card_info: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа."""
    parts = card_info.split()
    card_type = " ".join(parts[:-1])  # Все, кроме последнего элемента
    number = parts[-1]  # Последний элемент - номер

    # Список типов карт
    card_types = ["visa", "mastercard", "maestro", "мир", "american express"]

    if card_type.lower() in card_types:  # Если это карта
        masked_number = mask_card_number(number)  # Используем функцию маскировки карты
        return f"{card_type} {masked_number}"
    elif card_type.lower() == "счет":  # Если это счет
        masked_number = mask_account_number(number)  # Используем функцию маскировки счета
        return f"{card_type} {masked_number}"
    else:
        return card_info  # Если тип не распознан, возвращаем оригинал


def get_date(date_str: str) -> str:
    """Преобразует строку с датой в формате 'YYYY-MM-DDTHH:MM:SS' в 'DD.MM.YYYY'."""
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")

