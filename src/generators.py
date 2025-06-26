from typing import Any, Generator, Iterator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта соответствует заданной"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    """Функция возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    for i in range(start, end + 1):
        card_number = []
        num = str(i).zfill(16)
        for j in range(0, 16, 4):
            card_number.append(num[j : j + 4])
        yield " ".join(card_number)
