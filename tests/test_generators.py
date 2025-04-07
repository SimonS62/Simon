import pytest
from src.generators import transaction_descriptions, card_number_generator

# Пример данных для тестирования
transactions = [
    {"id": 1, "type": "purchase", "amount": 100, "currency": "USD"},
    {"id": 2, "type": "refund", "amount": 50, "currency": "EUR"},
    {"id": 3, "type": "purchase", "amount": 200, "currency": "USD"},
]


# Тестирование функции transaction_descriptions
def test_transaction_descriptions():
    descriptions = list(transaction_descriptions(transactions))

    assert len(descriptions) == len(transactions)
    assert descriptions[0] == "Transaction ID: 1, Type: purchase, Amount: 100 USD"
    assert descriptions[1] == "Transaction ID: 2, Type: refund, Amount: 50 EUR"
    assert descriptions[2] == "Transaction ID: 3, Type: purchase, Amount: 200 USD"


def test_transaction_descriptions_empty():
    descriptions = list(transaction_descriptions([]))

    assert descriptions == []


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
