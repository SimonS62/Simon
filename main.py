# main.py
from src.widget import get_date, mask_account_card

# Примеры для mask_account_card
print(mask_account_card("Visa Platinum 7000792289606361"))  # Ожидаемый вывод: Visa Platinum ************6361
print(mask_account_card("Счет 73654108430135874305"))      # Ожидаемый вывод: Счет ************4305
print(mask_account_card("Maestro 7000792289606361"))        # Ожидаемый вывод: Maestro ************6361
print(mask_account_card("МИР 1234567890123456"))            # Ожидаемый вывод: МИР ************3456
print(mask_account_card("American Express 1234567890123456"))  # Ожидаемый вывод: American Express ************3456

# Примеры для get_date
print(get_date("2024-03-11T02:26:18.671407"))  # Ожидаемый вывод: 11.03.2024
