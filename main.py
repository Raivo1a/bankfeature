from src.widget import get_date, mask_account_card

account_card = input("Введите номер: ")
date = input("Введите дату: ")

print(mask_account_card(account_card))

print(get_date(date))
