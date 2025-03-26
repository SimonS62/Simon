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

import pytest
from src.masks import mask_card_number, mask_account_number

@pytest.fixture
def card_number_cases():
    return [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("1234-5678-1234-5678", "1234 56** **** 5678"),
        ("1234", "1234"),  # Слишком короткий номер
        ("123456", "123456"),  # Слишком короткий номер
        ("", ""),  # Пустая строка
        ("0000000000000000", "0000 00** **** 0000"),
        ("123456789012345", "123456789012345"),  # Слишком короткий номер
        ("12345678901234567", "1234 56** **** 4567"),
    ]

@pytest.mark.parametrize("card_number, expected", card_number_cases())
def test_mask_card_number(card_number, expected):
    assert mask_card_number(card_number) == expected

@pytest.fixture
def account_number_cases():
    return [
        ("1234567890", "**7890"),
        ("123", "123"),  # Слишком короткий номер
        ("", ""),  # Пустая строка
        ("1234", "**34"),
        ("12345", "**345"),
        ("123456", "**456"),
    ]

@pytest.mark.parametrize("account_number, expected", account_number_cases())
def test_mask_account_number(account_number, expected):
    assert mask_account_number(account_number) == expected

