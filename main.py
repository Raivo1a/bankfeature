from src.masks import get_mask_account, get_mask_card_number

card = input("Введите номер карты: ")
account = input("Введите номер счета: ")

print(get_mask_card_number(card))

print(get_mask_account(account))
