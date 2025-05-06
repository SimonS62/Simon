import pytest
from unittest.mock import patch
from external_api import convert_to_rub


def test_convert_to_rub():
    amount = 100
    currency = 'USD'

    # Используем patch для замены requests.get
    with patch('external_api.requests.get') as mock_get:
        # Настраиваем mock-объект, чтобы он возвращал нужный ответ
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {
                'USD': 75.0  # Предположим, что курс USD к RUB равен 75
            }
        }

        result = convert_to_rub(amount, currency)

        assert result == amount / 75.0  # Проверяем правильность конвертации


def test_convert_to_rub_invalid_currency():
    amount = 100
    currency = 'INVALID'

    with patch('external_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'rates': {}
        }

        with pytest.raises(ValueError) as excinfo:
            convert_to_rub(amount, currency)

        assert str(excinfo.value) == "Курс для INVALID не найден."
