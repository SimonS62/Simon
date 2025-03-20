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


if __name__ == "__main__":
    pytest.main()

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

    import pytest
    from src.processing import filter_by_state, sort_by_date

    def test_filter_by_state():
        data = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

        # Тестирование фильтрации по состоянию 'EXECUTED'
        executed = filter_by_state(data)
        assert len(executed) == 2
        assert all(item['state'] == 'EXECUTED' for item in executed)

        # Тестирование фильтрации по состоянию 'CANCELED'
        canceled = filter_by_state(data, 'CANCELED')
        assert len(canceled) == 2
        assert all(item['state'] == 'CANCELED' for item in canceled)

        # Тестирование фильтрации по состоянию, которого нет
        unknown = filter_by_state(data, 'UNKNOWN')
        assert len(unknown) == 0

    def test_sort_by_date():
        data = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

        # Тестирование сортировки по дате по умолчанию (по убыванию)
        sorted_data_desc = sort_by_date(data)
        assert sorted_data_desc[0]['date'] == '2019-07-03T18:35:29.512364'
        assert sorted_data_desc[-1]['date'] == '2018-06-30T02:08:58.425572'

        # Тестирование сортировки по дате по возрастанию
        sorted_data_asc = sort_by_date(data, descending=False)
        assert sorted_data_asc[0]['date'] == '2018-06-30T02:08:58.425572'
        assert sorted_data_asc[-1]['date'] == '2019-07-03T18:35:29.512364'

    if __name__ == '__main__':
        pytest.main()



def test_get_date():
    # Тестирование преобразования даты
    assert get_date("2023-10-01T12:30:00") == "01.10.2023"
    assert get_date("2020-01-15T08:45:00") == "15.01.2020"
    assert get_date("1999-12-31T23:59:59") == "31.12.1999"

    # Тестирование с некорректной датой (должно вызвать ошибку)
    with pytest.raises(ValueError):
        get_date("invalid-date")


if __name__ == "__main__":
    pytest.main()