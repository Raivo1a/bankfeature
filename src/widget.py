from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Возвращает строку с замаскированным номером"""
    parts = account_card.split()
    card_type = " ".join(parts[:-1])

    if 'счет' in card_type.lower():
        masked_account_number = f'{account_card[:4]} {get_mask_account(account_card[5:])}'
        return masked_account_number
    else:
        masked_card_number = f'{account_card[:-16]}{get_mask_card_number(account_card[-16:])}'
        return masked_card_number


def get_date(date: str) -> str:
    '''Возвращает строку с датой в формате "ДД.ММ.ГГГГ"'''
    current_date = datetime.fromisoformat(date)
    date_formatted = current_date.strftime("%d.%m.%Y")
    return date_formatted
