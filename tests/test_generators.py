import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions_fixture: list) -> None:
    usd_generator = filter_by_currency(transactions_fixture, "USD")
    assert next(usd_generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    with pytest.raises(StopIteration):
        next(usd_generator)


def test_transaction_descriptions(transactions_fixture: list) -> None:
    expected_descriptions = transaction_descriptions(transactions_fixture)
    assert next(expected_descriptions) == "Перевод организации"
    assert next(expected_descriptions) == "Перевод со счета на счет"
    assert next(expected_descriptions) == "Перевод со счета на счет"
    assert next(expected_descriptions) == "Перевод с карты на карту"
    assert next(expected_descriptions) == "Перевод организации"


def test_card_number_generator() -> None:
    _generator = card_number_generator(1, 3)
    assert next(_generator) == "0000 0000 0000 0001"
    assert next(_generator) == "0000 0000 0000 0002"
    assert next(_generator) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(_generator)
