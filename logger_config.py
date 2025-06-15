import logging
import os


def setup_module_logger(module_name):
    # формируем путь до logs относительно текущего модуля
    current_dir = os.path.dirname(__file__)
    logs_dir = os.path.join(current_dir, 'logs')

    # Создаем папку logs, если не существует
    os.makedirs(logs_dir, exist_ok=True)

    # Путь к файлу логов для этого модуля
    log_file_path = os.path.join(logs_dir, f'{module_name}.log')

    # Получаем или создаем логгер по имени модуля
    logger = logging.getLogger(module_name)

    # Устанавливаем уровень логирования (например, DEBUG)
    logger.setLevel(logging.DEBUG)

    # Очищаем предыдущие обработчики, чтобы избежать дублирования
    if logger.hasHandlers():
        logger.handlers.clear()

    # Создаем обработчик файла
    file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')

    # Форматтер для логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
