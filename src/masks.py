def mask_card_number(card_number: str) -> str:
    """ Маскирует номер банковской карты. """
    # Проверяем длину номера карты
    if len(card_number) < 16:
        return card_number  # Если номер карты слишком короткий

    # Форматируем номер по шаблону: 1234 56** **** 3456
    masked_number = (
        f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    )
    return masked_number


def mask_account_number(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    # Проверяем длину номера счета
    if len(account_number) < 4:
        return account_number  # Если номер счета слишком короткий

    # Форматируем номер по шаблону: **7890
    masked_account = f"**{account_number[-4:]}"
    return masked_account
