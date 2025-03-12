def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации
    :param state: Значение ключа 'state' (по умолчанию 'EXECUTED')
    :return: Новый список словарей, соответствующих указанному значению state
    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """
    Функция сортирует список словарей по значению ключа 'date'.

    :param data: Список словарей для фильтрации
    :param descending: Направление сортировки
    :return: Новый отсортированный список словарей
    """
    return sorted(data, key=lambda x: x.get("date"), reverse=descending)