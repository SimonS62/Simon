import json
import unittest
from unittest.mock import mock_open, patch
from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    def test_load_transactions(self):
        mock_data = json.dumps([
            {"amount": 100, "currency": "USD", "description": "Транзакция 1"},
            {"amount": 200, "currency": "EUR", "description": "Транзакция 2"}
        ])

        with patch('builtins.open', mock_open(read_data=mock_data)):
            transactions = load_transactions('fake_path.json')

            assert len(transactions) == 2
            assert transactions[0]['amount'] == 100
            assert transactions[1]['currency'] == 'EUR'

