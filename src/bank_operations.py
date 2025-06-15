import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Ищет в списке операций те, у которых в поле 'description' есть совпадение с регулярным выражением search.

    Args:
        data (list[dict]): список словарей с данными о банковских операциях.
        search (str): строка с регулярным выражением для поиска.

    Returns:
        list[dict]: список словарей, у которых есть совпадение в описании.
    """
    pattern = re.compile(search, re.IGNORECASE)
    result = []

    for record in data:
        description = record.get('description', '')
        if pattern.search(description):
            result.append(record)

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций для каждой категории.

    Args:
        data (list[dict]): список словарей с данными о банковских операциях.
        categories (list): список названий категорий.

    Returns:
        dict: словарь, где ключи — названия категорий, значения — количество операций.
    """
    # Инициализируем словарь с нулями для каждой категории
    category_counts = {category: 0 for category in categories}

    for record in data:
        description = record.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
                break  # Предполагается, что одна операция относится к одной категории

    return category_counts
