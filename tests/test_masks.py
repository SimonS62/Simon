import pytest
from src.masks import mask_card_number, mask_account_number


def test_mask_card_number():
    # Тестирование стандартного случая
    assert mask_card_number("1234567812345678") == "1234 56** **** 5678"

    # Тестирование с пробелами
    assert mask_card_number("1234 5678 1234 5678") == "1234 56** **** 5678"

    # Тестирование с символами
    assert mask_card_number("1234-5678-1234-5678") == "1234 56** **** 5678"

    # Тестирование с коротким номером карты
    assert mask_card_number("1234") == "1234"  # Слишком короткий номер
    assert mask_card_number("123456") == "123456"  # Слишком короткий номер

    # Тестирование с пустой строкой
    assert mask_card_number("") == ""  # Пустая строка

    # Тестирование с номером карты, состоящим из 16 цифр
    assert mask_card_number("0000000000000000") == "0000 00** **** 0000"

    # Тестирование с номером карты, состоящим из менее 16 цифр
    assert mask_card_number("123456789012345") == "123456789012345"  # Слишком короткий номер

    # Тестирование с номером карты, состоящим из 17 цифр
    assert mask_card_number("12345678901234567") == "1234 56** **** 4567"


def test_mask_account_number():
    # Тестирование стандартного случая
    assert mask_account_number("1234567890") == "**7890"

    # Тестирование с коротким номером счета
    assert mask_account_number("123") == "123"  # Слишком короткий номер

    # Тестирование с пустой строкой
    assert mask_account_number("") == ""  # Пустая строка

    # Тестирование с номером счета, состоящим из 4 цифр
    assert mask_account_number("1234") == "**34"

    # Тестирование с номером счета, состоящим из 5 цифр
    assert mask_account_number("12345") == "**345"

    # Тестирование с номером счета, состоящим из 6 цифр
    assert mask_account_number("123456") == "**456"


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


def test_mask_card_number(card_numbers):
    """ Тестирование функции маскировки номера карты. """
    assert mask_card_number(card_numbers["valid_card"]) == "1234 56** **** 5678"
    assert mask_card_number(card_numbers["valid_card_with_spaces"]) == "1234 56** **** 5678"
    assert mask_card_number(card_numbers["valid_card_with_dashes"]) == "1234 56** **** 5678"
    assert mask_card_number(card_numbers["short_card"]) == "123456"
    assert mask_card_number(card_numbers["long_card"]) == "1234 56** **** 5678"
    assert mask_card_number(card_numbers["empty_card"]) == ""


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


def test_mask_account_number(account_numbers):
    """Тестирование функции маскировки номера счета."""
    assert mask_account_number(account_numbers["valid_account"]) == "**7890"
    assert mask_account_number(account_numbers["exactly_four_digits"]) == "**34"
    assert mask_account_number(account_numbers["short_account"]) == "12"
    assert mask_account_number(account_numbers["long_account"]) == "**3456"
    assert mask_account_number(account_numbers["account_with_dashes"]) == "**5678"
    assert mask_account_number(account_numbers["empty_account"]) == ""
