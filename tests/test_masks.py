import pytest
from src.masks import mask_card_number, mask_account_number


def test_mask_card_number():
    # Тестирование стандартного случая
    assert mask_card_number("1234567890123456") == "1234 56** **** 3456"

    # Тестирование случая с коротким номером
    assert mask_card_number("12345") == "12345"  # Возвращает без изменений

    # Тестирование случая с номером, который не является картой
    assert mask_card_number("123456789012") == "123456789012"  # Возвращает без изменений

    # Тестирование случая с пустой строкой
    assert mask_card_number("") == ""  # Возвращает пустую строку

    # Тестирование случая с пробелами в номере карты
    assert mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"


def test_mask_account_number():
    # Тестирование стандартного случая
    assert mask_account_number("1234567890") == "******7890"

    # Тестирование с коротким номером счета
    assert mask_account_number("123") == "123"  # Слишком короткий номер

    # Тестирование с пустой строкой
    assert mask_account_number("") == ""  # Пустая строка

    # Тестирование с номером счета, состоящим из 4 цифр
    assert mask_account_number("1234") == "**34"

    # Тестирование с номером счета, состоящим из 5 цифр
    assert mask_account_number("12345") == "*2345"

    # Тестирование с номером счета, состоящим из 6 цифр
    assert mask_account_number("123456") == "**3456"

    # Тестирование с номером счета, состоящим из 10 цифр
    assert mask_account_number("9876543210") == "******3210"


@pytest.fixture
def card_numbers():
    """ Фикстура для тестирования различных номеров карт. """
    return {
        "valid_card": "1234567812345678",
        "valid_card_with_spaces": "1234 5678 1234 5678",
        "valid_card_with_dashes": "1234-5678-1234-5678",
        "short_card": "123456",
        "long_card": "123456781234567890",
        "empty_card": "",
    }


@pytest.fixture
def account_numbers():
    """Фикстура для тестирования различных номеров счетов."""
    return {
        "valid_account": "1234567890",
        "exactly_four_digits": "1234",
        "short_account": "12",
        "long_account": "123456",
        "account_with_dashes": "1234-5678",
        "empty_account": "",
    }
