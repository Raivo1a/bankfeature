from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

account_card = input("Введите номер: ")
date = input("Введите дату: ")

print(mask_account_card(account_card))

print(get_date(date))
