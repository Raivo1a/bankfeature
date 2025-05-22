from src.masks import get_mask_account,get_mask_card_number

def mask_account_card(account_card: str) -> str:
    '''Возвращает строку с замаскированным номером'''
    parts = account_card.split()
    card_type = " ".join(parts[:-1])
    number = parts[-1]

    if 'счет' in card_type.lower():
        masked_number = '**' + number[-4:]
    else:
        masked_number = number[:4] + ' ' + number[4:6] + '** ****' + number[-4:]

    return f'{card_type} {masked_number}'


from datetime import datetime

def get_date(date:str) -> str :
    '''возвращает строку с датой в формате "ДД.ММ.ГГГГ"'''
    current_date = datetime.fromisoformat(date)
    date_formatted = current_date.strftime('%d.%m.%Y')
    return date_formatted