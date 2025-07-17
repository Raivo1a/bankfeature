from src.bank_search import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reader import read_csv_file, read_xlsx_file
from src.utils import get_operations_data
from src.widget import get_date, mask_account_card


def main():
    """Общая функция по сборке всего проекта"""
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print(
            """
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
        )
        user_input = input("Введите номер пункта меню: ")
        if user_input == "1":
            transactions_data = get_operations_data("data/operations.json")
            print("Для обработки выбран JSON-файл.")
            break
        elif user_input == "2":
            transactions_data = read_csv_file("data/transactions.csv")
            print("Для обработки выбран CSV-файл.")
            break
        elif user_input == "3":
            transactions_data = read_xlsx_file("data/transactions_excel.xlsx")
            print("Для обработки выбран EXCEL-файл.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3")

    while True:
        print(
            """
Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING)
"""
        )
        user_state = input("Введите фильтровку: ").upper()
        transactions_data = filter_by_state(transactions_data, state=user_state)
        if user_state == "EXECUTED" or user_state == "CANCELED" or user_state == "PENDING":
            print(f"Для фильтровки выбран статус {user_state}.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите EXECUTED, CANCELED или PENDING")

    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет")
        _sort = input().lower()
        if _sort == "да":
            print("Программа: Отсортировать по возрастанию или по убыванию?")
            _sort = input().lower()
            if _sort == "по возрастанию":
                transactions_data = sort_by_date(transactions_data, False)
                print(f"Для сортировки выбран статус {_sort}")
                break
            elif _sort == "по убыванию":
                transactions_data = sort_by_date(transactions_data, True)
                print(f"Для сортировки выбран статус {_sort}")
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите 'по возрастанию' или 'по убыванию'")
        elif _sort == "нет":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 'да' или 'нет'")

    while True:
        print("Программа: Выводить только рублевые транзакции? Да/Нет")
        rubles = input().lower()
        if rubles == "да":
            transactions_data = filter_by_currency(transactions_data, "RUB")
            break
        elif rubles == "нет":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 'да' или 'нет'")

    while True:
        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        filter = input().lower()
        if filter == "да":
            search = input("Введите строку для поиска: ")
            transactions_data = process_bank_search(transactions_data, search)
            break
        elif filter == "нет":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 'да' или 'нет'")

    print("Программа: Распечатываю итоговый список транзакций...")

    counter = 0
    for transaction in transactions_data:
        counter += 1
        date = get_date(transaction.get("date"))
        description = transaction.get("description")
        print(f"{date} {description}")

        if transaction.get("description") == "Открытие вклада":
            print(mask_account_card(transaction["to"]))
            if user_input == "1":
                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["name"]
            elif user_input == "2" or user_input == "3":
                amount = transaction["amount"]
                currency = transaction["currency_code"]
            print(f"Сумма: {amount} {currency}")
        else:
            account_from = mask_account_card(transaction["from"])
            account_to = mask_account_card(transaction["to"])
            print(f"{account_from} -> {account_to}")
            if user_input == "1":
                amount = transaction["operationAmount"]["amount"]
                currency = transaction["operationAmount"]["currency"]["name"]
            elif user_input == "2" or user_input == "3":
                amount = transaction["amount"]
                currency = transaction["currency_code"]
            print(f"Сумма: {amount} {currency}")

    if counter > 0:
        print(f"Программа: Всего банковских операций в выборке: {counter}")
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


print(main())
