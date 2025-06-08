import pytest
from unittest.mock import patch, Mock
import pandas as pd

# Импортируем функции из модуля
from src.load_transactions import read_transactions_csv, read_transactions_xlsx


# Тест для функции чтения CSV
@patch('pandas.read_csv')
def test_read_transactions_csv(mock_read_csv):
    # Создаем фиктивный DataFrame
    mock_df = pd.DataFrame([
        {'id': 1, 'amount': 100},
        {'id': 2, 'amount': 200}
    ])
    mock_read_csv.return_value = mock_df

    # Вызов функции
    result = read_transactions_csv('fake_path.csv')

    # Проверка вызова pandas.read_csv с правильным аргументом
    mock_read_csv.assert_called_once_with('fake_path.csv')

    # Проверка результата — список словарей
    assert isinstance(result, list)
    assert result == [
        {'id': 1, 'amount': 100},
        {'id': 2, 'amount': 200}
    ]


# Тест для функции чтения XLSX
@patch('pandas.read_excel')
def test_read_transactions_xlsx(mock_read_excel):
    # Создаем фиктивный DataFrame
    mock_df = pd.DataFrame([
        {'id': 3, 'amount': 300},
        {'id': 4, 'amount': 400}
    ])
    mock_read_excel.return_value = mock_df

    # Вызов функции
    result = read_transactions_xlsx('fake_path.xlsx')

    # Проверка вызова pandas.read_excel с правильным аргументом
    mock_read_excel.assert_called_once_with('fake_path.xlsx')

    # Проверка результата — список словарей
    assert isinstance(result, list)
    assert result == [
        {'id': 3, 'amount': 300},
        {'id': 4, 'amount': 400}
    ]
