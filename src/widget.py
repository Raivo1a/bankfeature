def mask_account_card(account_card):
    '''Возвращает строку с замаскированным номером'''
    parts = account_card.split()
    card_type = " ".join(parts[:-1])
    number = parts[-1]

    if 'счет' in card_type.lower():
        masked_number = '**' + number[-4:]
    else:
        masked_number = number[:4] + ' ' + number[4:6] + '** ****' + number[-4:]

    return f'{card_type} {masked_number}'