def mask_card_number(card_number: str) -> str:
    """ Маскирует номер банковской карты. """
    # Удаляем все пробелы из номера карты
    card_number = card_number.replace(" ", "")

    # Проверяем длину номера карты
    if len(card_number) < 16:
        return card_number  # Если номер карты слишком короткий

    # Форматируем номер по шаблону: 1234 56** **** 3456
    masked_number = (
        f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    )
    return masked_number


def mask_account_number(account_number: str) -> str:
    """ Маскирует номер банковского счета. """
    # Проверяем длину номера счета
    if len(account_number) < 4:
        return account_number  # Если номер счета слишком короткий

    # Если длина номера больше или равна 4, маскируем все, кроме последних 4 цифр
    masked_number = '*' * (len(account_number) - 4) + account_number[-4:]

    # Если длина номера ровно 4, возвращаем '**' + последние 2 цифры
    if len(account_number) == 4:
        masked_number = '**' + account_number[-2:]

    return masked_number
