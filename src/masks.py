from logger_config import setup_module_logger

# Создаем логер для модуля masks
logger = setup_module_logger('masks')


def mask_card_number(card_number: str) -> str:
    """ Маскирует номер банковской карты. """
    logger.info("Начало маскировки номера карты.")

    card_number_clean = card_number.replace(" ", "")
    logger.debug(f"Очистка пробелов: {card_number_clean}")

    if len(card_number_clean) < 16:
        logger.warning(f"Недостаточная длина номера карты: {len(card_number_clean)}")
        return card_number

    masked_number = (
        f"{card_number_clean[:4]} {card_number_clean[4:6]}** **** {card_number_clean[-4:]}"
    )

    logger.info(f"Маскированный номер карты: {masked_number}")
    return masked_number


def mask_account_number(account_number: str) -> str:
    """ Маскирует номер банковского счета. """
    logger.info("Начало маскировки номера счета.")

    if len(account_number) < 4:
        logger.warning(f"Недостаточная длина номера счета: {len(account_number)}")
        return account_number

    if len(account_number) == 4:
        masked_number = '**' + account_number[-2:]
        logger.debug("Длина номера равна 4, маскирование по особому сценарию.")
        return masked_number

    masked_number = '*' * (len(account_number) - 4) + account_number[-4:]

    logger.info(f"Маскированный номер счета: {masked_number}")
    return masked_number


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
