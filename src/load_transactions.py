import pandas as pd


def read_transactions_csv(file_path):
    """
    Читает транзакции из CSV файла и возвращает список словарей.
    :param file_path: путь к файлу .csv
    :return: список словарей с транзакциями
    """
    try:
        df = pd.read_csv(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")
        return []


def read_transactions_xlsx(file_path):
    """
    Читает транзакции из Excel файла и возвращает список словарей.
    :param file_path: путь к файлу .xlsx
    :return: список словарей с транзакциями
    """
    try:
        df = pd.read_excel(file_path)
        # Преобразуем DataFrame в список словарей
        transactions = df.to_dict(orient='records')
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении Excel файла: {e}")
        return []
