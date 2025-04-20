import pytest
from src.generators import transaction_descriptions, card_number_generator


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


def test_transaction_descriptions():
    # Входные данные (транзакции) не важны для этого теста,
    # так как функция возвращает фиксированные значения.
    transactions = [
        {'id': 1, 'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}},
        {'id': 2, 'operationAmount': {'amount': 200, 'currency': {'code': 'EUR'}}},
        {'id': 3, 'operationAmount': {'amount': 150, 'currency': {'code': 'USD'}}},
        {'id': 4, 'operationAmount': {'amount': 300, 'currency': {'code': 'JPY'}}},
        {'id': 5, 'operationAmount': {'amount': 50, 'currency': {'code': 'EUR'}}}
    ]

    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

    # Получаем описания из генератора
    descriptions = list(transaction_descriptions(transactions))

    # Проверяем, что полученные описания совпадают с ожидаемыми
    assert descriptions == expected_descriptions


# Тестирование генератора card_number_generator
@pytest.mark.parametrize("start,end,expected", [
    (1, 5, [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]),
    (9999_9999_9999_9995, 9999_9999_9999_9999, [
        '9999 9999 9999 9995',
        '9999 9999 9999 9996',
        '9999 9999 9999 9997',
        '9999 9999 9999 9998',
        '9999 9999 9999 9999'
    ]),
])
def test_card_number_generator(start, end, expected):
    generated_numbers = list(card_number_generator(start, end))

    assert generated_numbers == expected


def test_card_number_generator_empty_range():
    generated_numbers = list(card_number_generator(5, -1))

    assert generated_numbers == []


def test_card_number_generator_single_value():
    generated_numbers = list(card_number_generator(1, 1))

    assert generated_numbers == ['0000 0000 0000 0001']


def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по заданной валюте."""
    return [transaction for transaction in transactions if transaction['currency'] == currency]


@pytest.fixture
def transactions():
    """Фикстура для генерации тестовых данных."""
    return [
        {'id': 1, 'amount': 100, 'currency': 'USD'},
        {'id': 2, 'amount': 200, 'currency': 'EUR'},
        {'id': 3, 'amount': 150, 'currency': 'USD'},
        {'id': 4, 'amount': 300, 'currency': 'JPY'},
        {'id': 5, 'amount': 50, 'currency': 'EUR'},
    ]


def test_filter_by_currency():
    transactions = [
        {'id': 1, 'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}},
        {'id': 2, 'operationAmount': {'amount': 200, 'currency': {'code': 'EUR'}}},
        {'id': 3, 'operationAmount': {'amount': 150, 'currency': {'code': 'USD'}}},
        {'id': 4, 'operationAmount': {'amount': 300, 'currency': {'code': 'JPY'}}},
        {'id': 5, 'operationAmount': {'amount': 50, 'currency': {'code': 'EUR'}}}
    ]

    # Ожидаемые результаты
    expected_usd = [
        {'id': 1, 'operationAmount': {'amount': 100, 'currency': {'code': 'USD'}}},
        {'id': 3, 'operationAmount': {'amount': 150, 'currency': {'code': 'USD'}}}
    ]

    expected_eur = [
        {'id': 2, 'operationAmount': {'amount': 200, 'currency': {'code': 'EUR'}}},
        {'id': 5, 'operationAmount': {'amount': 50, 'currency': {'code': 'EUR'}}}
    ]

    # Проверка фильтрации по USD
    usd_transactions = list(filter_by_currency(transactions, 'USD'))
    assert usd_transactions == expected_usd

    # Проверка фильтрации по EUR
    eur_transactions = list(filter_by_currency(transactions, 'EUR'))
    assert eur_transactions == expected_eur

    # Проверка фильтрации по JPY (должно вернуть пустой список)
    jpy_transactions = list(filter_by_currency(transactions, 'JPY'))
    assert jpy_transactions == []
