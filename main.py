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


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ").strip()

    # В зависимости от выбора, запрашиваем путь к файлу
    if choice == '1':
        print("Программа: Для обработки выбран JSON-файл.")
        filename = input("Введите путь к JSON-файлу: ")
        # Здесь должна быть логика загрузки данных из файла
        # transactions = load_json(filename)
        transactions = []  # Заглушка
    elif choice == '2':
        print("Программа: Для обработки выбран CSV-файл.")
        filename = input("Введите путь к CSV-файлу: ")
        # transactions = load_csv(filename)
        transactions = []  # Заглушка
    elif choice == '3':
        print("Программа: Для обработки выбран XLSX-файл.")
        filename = input("Введите путь к XLSX-файлу: ")
        # transactions = load_xlsx(filename)
        transactions = []  # Заглушка
    else:
        print("Некорректный выбор. Завершение программы.")
        return

    # Временно используем пример данных для демонстрации
    transactions = [
        {'date': '08.12.2019', 'description': 'Открытие вклада', 'details': 'Счет **4321', 'amount': 40542,
         'currency': 'руб.'},
        {'date': '12.11.2019', 'description': 'Перевод с карты на карту', 'details': 'MasterCard 7771 ...',
         'amount': 130, 'currency': 'USD'},
        {'date': '18.07.2018', 'description': 'Перевод организации', 'details': 'Visa Platinum ...', 'amount': 8390,
         'currency': 'руб.'},
        {'date': '03.06.2018', 'description': 'Перевод со счета на счет', 'details': 'Счет **2935 ...', 'amount': 8200,
         'currency': 'EUR'},
    ]

    statuses = ['EXECUTED', 'CANCELED', 'PENDING']

    # Запрос статуса фильтрации
    while True:
        status_input = input(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Пользователь: "
        ).strip()
        status_upper = status_input.upper()
        if status_upper in statuses:
            print(f"Программа: Операции отфильтрованы по статусу \"{status_upper}\"")
            break
        else:
            print(f"Статус операции \"{status_input}\" недоступен.")

    # Предположим, есть функция filter_by_status
    # filtered_transactions = filter_by_status(transactions, status_upper)
    filtered_transactions = transactions  # Заглушка

    # Спрашиваем о сортировке по дате
    sort_choice = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order_input = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        ascending = True if order_input in ['по возрастанию'] else False
        # filtered_transactions = sort_transactions(filtered_transactions, ascending=ascending)

    # Спрашиваем о фильтрации по слову в описании
    keyword_choice = input(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    ).strip().lower()
    if keyword_choice == "да":
        keyword = input("Введите слово или фразу для поиска:\nПользователь: ").strip()
        # filtered_transactions = filter_by_keyword(filtered_transactions, keyword)

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")

    if not filtered_transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    total_operations = len(filtered_transactions)

    for t in filtered_transactions:
        date_str = t.get('date')
        description = t.get('description')
        details = t.get('details')
        amount = t.get('amount')
        currency = t.get('currency')

        print(f"{date_str} {description}")

        if details:
            print(details)

        print(f"Сумма: {amount} {currency}\n")

    print(f"Всего банковских операций в выборке: {total_operations}")


if __name__ == "__main__":
    main()
