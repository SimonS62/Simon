import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub, process_transaction


class TestExternalAPI(unittest.TestCase):

    @patch('external_api.requests.get')
    def test_convert_to_rub_success(self, mock_get):
        # Настройка мок-ответа
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": 7500.0
        }

        result = convert_to_rub(100, 'USD')
        self.assertEqual(result, 7500.0)

    @patch('external_api.requests.get')
    def test_convert_to_rub_invalid_currency(self, mock_get):
        # Настройка мок-ответа для случая с некорректной валютой
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}

        result = convert_to_rub(100, 'INVALID')
        self.assertIsNone(result)

    @patch('external_api.requests.get')
    def test_convert_to_rub_api_error(self, mock_get):
        # Настройка мок-ответа для ошибки API
        mock_get.side_effect = Exception("API Error")

        result = convert_to_rub(100, 'USD')
        self.assertIsNone(result)

    @patch('external_api.convert_to_rub')
    def test_process_transaction_usd(self, mock_convert):
        mock_convert.return_value = 7500.0

        transaction = {'amount': 100, 'currency': 'USD'}
        result = process_transaction(transaction)

        self.assertEqual(result, 7500.0)

    @patch('external_api.convert_to_rub')
    def test_process_transaction_eur(self, mock_convert):
        mock_convert.return_value = 8500.0

        transaction = {'amount': 100, 'currency': 'EUR'}
        result = process_transaction(transaction)

        self.assertEqual(result, 8500.0)

    def test_process_transaction_rub(self):
        transaction = {'amount': 5000, 'currency': 'RUB'}
        result = process_transaction(transaction)

        self.assertEqual(result, 5000.0)


if __name__ == '__main__':
    unittest.main()