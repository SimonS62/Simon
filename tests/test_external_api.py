import unittest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub


    def test_convert_to_rub(self, mock_getenv, mock_get):
        # Настройка mock для переменной окружения API_KEY
        mock_getenv.return_value = 'fake_api_key'

        # Настройка mock для ответа API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {
                'USD': 75.0,
                'EUR': 85.0
            }
        }
        mock_get.return_value = mock_response

        # Тестирование конвертации из USD в RUB
        amount_in_rub = convert_to_rub(100, 'USD')
        self.assertAlmostEqual(amount_in_rub, 7500.0)  # 100 * 75.0


    def test_convert_to_rub_api_key_not_found(self, mock_getenv, mock_get):
        # Настройка mock для отсутствия API_KEY
        mock_getenv.return_value = None

        with self.assertRaises(ValueError) as context:
            convert_to_rub(100, 'USD')

        self.assertEqual(str(context.exception), "API ключ не найден. Убедитесь, что он указан в файле .env.")


    def test_convert_to_rub_invalid_currency(self, mock_getenv, mock_get):
        # Настройка mock для переменной окружения API_KEY
        mock_getenv.return_value = 'fake_api_key'

        # Настройка mock для ответа API с отсутствующим курсом валюты
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {}
        }
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            convert_to_rub(100, 'GBP')  # GBP не существует в rates

        self.assertEqual(str(context.exception), "Курс для GBP не найден.")


    def test_convert_to_rub_api_error(self, mock_getenv, mock_get):
        # Настройка mock для переменной окружения API_KEY
        mock_getenv.return_value = 'fake_api_key'

        # Настройка mock для ошибки API (например, статус код не 200)
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            convert_to_rub(100, 'USD')

        self.assertEqual(str(context.exception), "Ошибка при обращении к API.")


if __name__ == '__main__':
    unittest.main()
