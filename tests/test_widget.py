import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card():
    # Тестирование маскировки номера карты
    assert mask_account_card("Visa 1234567812345678") == "visa 1234 56** **** 5678"
    assert mask_account_card("MasterCard 1234567812345678") == "mastercard 1234 56** **** 5678"
    assert mask_account_card("Maestro 1234567812345678") == "maestro 1234 56** **** 5678"
    assert mask_account_card("Мир 1234567812345678") == "мир 1234 56** **** 5678"
    assert mask_account_card("American Express 1234567812345678") == "american express 1234 56** **** 5678"

    # Тестирование маскировки номера счета
    assert mask_account_card("Счет 1234567890") == "счет **7890"

    # Тестирование с нераспознанным типом
    assert mask_account_card("UnknownType 1234567890") == "UnknownType 1234567890"

    # Тестирование с неправильным форматом
    assert mask_account_card("Visa") == "Visa"  # Нет номера
    assert mask_account_card("Счет") == "Счет"  # Нет номера


def test_get_date():
    # Тестирование преобразования даты
    assert get_date("2023-10-01T12:30:00") == "01.10.2023"
    assert get_date("2020-01-15T08:45:00") == "15.01.2020"
    assert get_date("1999-12-31T23:59:59") == "31.12.1999"

    # Тестирование с некорректной датой (должно вызвать ошибку)
    with pytest.raises(ValueError):
        get_date("invalid-date")
