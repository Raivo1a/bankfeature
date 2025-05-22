from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция прячет номер карты"""
    if len(card_number) != 16:
        return "Неверный номер карты"
    else:
        return card_number[0:4] + ' ' + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(card_account: Union[str]) -> Union[str]:
    """Функция прячет номер счета"""
    if len(card_account) != 20:
        return "Неверный номер счета"
    else:
        return "**" + card_account[-4:]
