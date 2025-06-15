import pytest
import re
from src.bank_operations import process_bank_search, process_bank_operations


def test_process_bank_search():
    # Исходные данные
    data = [
        {'date': '01.01.2020', 'description': 'Перевод с карты на карту', 'amount': 1000},
        {'date': '02.01.2020', 'description': 'Оплата коммунальных услуг', 'amount': 500},
        {'date': '03.01.2020', 'description': 'Перевод в другой банк', 'amount': 200},
        {'date': '04.01.2020', 'description': 'Покупка в магазине', 'amount': 300},
        {'date': '05.01.2020', 'description': 'Перевод с карты на карту - бонус', 'amount': 150},
    ]

    # Регулярное выражение для поиска слова "перевод" (игнорируя регистр)
    search_pattern = r'перевод'

    # Вызов функции
    result = process_bank_search(data, search_pattern)

    # Проверка, что возвращаются только записи с описанием, содержащим "перевод"
    expected = [
        {'date': '01.01.2020', 'description': 'Перевод с карты на карту', 'amount': 1000},
        {'date': '03.01.2020', 'description': 'Перевод в другой банк', 'amount': 200},
        {'date': '05.01.2020', 'description': 'Перевод с карты на карту - бонус', 'amount': 150},
    ]

    assert result == expected


def test_process_bank_search_no_matches():
    data = [
        {'date': '01.01.2020', 'description': 'Оплата коммунальных услуг', 'amount': 500},
        {'date': '02.01.2020', 'description': 'Покупка в магазине', 'amount': 300},
    ]
    search_pattern = r'перевод'
    result = process_bank_search(data, search_pattern)
    assert result == []


def test_process_bank_search_empty_data():
    data = []
    search_pattern = r'.*'
    result = process_bank_search(data, search_pattern)
    assert result == []


def test_process_bank_search_case_insensitivity():
    data = [
        {'description': 'Перевод в другой банк'},
        {'description': 'перевод в другой банк'},
        {'description': 'ПЕРЕВОД в другой банк'},
        {'description': 'Оплата услуг'},
    ]
    pattern = r'перевод'
    result = process_bank_search(data, pattern)
    assert len(result) == 3


def test_process_bank_operations_basic():
    data = [
        {'description': 'Оплата коммунальных услуг'},
        {'description': 'Покупка в магазине'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Оплата коммунальных услуг за квартиру'},
        {'description': 'Покупка в магазине электроники'},
    ]
    categories = ['оплата', 'покупка', 'перевод']

    result = process_bank_operations(data, categories)

    expected = {
        'оплата': 2,
        'покупка': 2,
        'перевод': 1,
    }

    assert result == expected


def test_process_bank_operations_no_matches():
    data = [
        {'description': 'Зарплата за месяц'},
        {'description': 'Дивиденды'},
    ]
    categories = ['оплата', 'покупка']
    result = process_bank_operations(data, categories)
    expected = {
        'оплата': 0,
        'покупка': 0,
    }
    assert result == expected


def test_process_bank_operations_empty_data():
    data = []
    categories = ['любая']
    result = process_bank_operations(data, categories)
    expected = {'любая': 0}
    assert result == expected


def test_process_bank_operations_case_insensitivity():
    data = [
        {'description': 'ОпЛаТа коммунальных услуг'},
        {'description': 'ПОКУПКА в магазине'},
        {'description': 'Перевод с карты на карту'},
    ]
    categories = ['оплата', 'покупка', 'перевод']

    result = process_bank_operations(data, categories)

    expected = {
        'оплата': 1,
        'покупка': 1,
        'перевод': 1,
    }

    assert result == expected


def test_process_bank_operations_partial_match():
    data = [
        {'description': 'Оплата по кредиту'},
        {'description': 'Купил новую книгу'},
        {'description': 'Перевод денег другу'},
    ]
    categories = ['оплата', 'покупка', 'перевод']

    result = process_bank_operations(data, categories)

    expected = {
        'оплата': 1,
        'покупка': 0,
        'перевод': 1,
    }

    assert result == expected
