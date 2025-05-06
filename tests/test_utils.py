import json
from unittest.mock import mock_open, patch
from src.utils import load_transactions


def test_load_transactions():
    mock_data = json.dumps([
        {"amount": 100, "currency": "USD", "description": "Транзакция 1"},
        {"amount": 200, "currency": "EUR", "description": "Транзакция 2"}
    ])

    with patch('builtins.open', mock_open(read_data=mock_data)):
        transactions = load_transactions('fake_path.json')

        assert len(transactions) == 2
        assert transactions[0]['amount'] == 100
        assert transactions[1]['currency'] == 'EUR'
