import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_amount(transactions: dict) -> float:
    """Получает данные о транзакции и возвращает сумму в рублях"""
    if transactions["operationAmount"]["currency"]["code"] == "RUB":
        return float(transactions["operationAmount"]["amount"])
    else:
        currency_code = transactions["operationAmount"]["currency"]["code"]
        amount_transaction = transactions["operationAmount"]["amount"]
        amount_convert = exchange(currency_code, amount_transaction)
        return amount_convert


def exchange(currency_code: str, amount: float) -> float:
    """Конвертирует транзакции и возвращает сумму в рублях"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    headers = {"apikey": os.getenv("APILAYER_KEY")}

    response = requests.get(url, headers=headers)
    return round(response.json()["result"], 2)
