# src/widget.py
from datetime import datetime

def mask_account_number(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    if len(account_number) < 4:
        return account_number  # Если номер счета слишком короткий

    masked_account = f"**{account_number[-4:]}"
    return masked_account

def mask_account_card(card_info: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа."""
    parts = card_info.split()
    card_type = " ".join(parts[:-1])  # Все, кроме последнего элемента
    number = parts[-1]  # Последний элемент - номер

    if card_type.lower() in ["visa", "mastercard", "maestro"]:  # Если это карта
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        return f"{card_type} {masked_number}"
    elif card_type.lower() == "счет":  # Если это счет
        masked_number = f"**{number[-4:]}"
        return f"{card_type} {masked_number}"
    else:
        return card_info  # Если тип не распознан, возвращаем оригинал

def get_date(date_str: str) -> str:
    """Преобразует строку с датой в формате 'YYYY-MM-DDTHH:MM:SS' в 'DD.MM.YYYY'."""
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
