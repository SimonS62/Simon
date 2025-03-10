def filter_by_state(data, state='EXECUTED'):
    """
    Функция фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей для фильтрации
    :param state: Значение ключа 'state' (по умолчанию 'EXECUTED')
    :return: Новый список словарей, соответствующих указанному значению state
    """
    return [item for item in data if item.get('state') == state]
