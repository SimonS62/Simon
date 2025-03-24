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
