from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция прячет номер карты"""
    if len(card_number) != 16:
        raise ValueError('Ошибка! Введите корректный номер карты или счета')
    else:
        return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(card_account: Union[str]) -> Union[str]:
    """Функция прячет номер счета"""
    if len(card_account) != 20:
        raise ValueError('Ошибка! Введите корректный номер карты или счета')
    else:
        return "**" + card_account[-4:]
