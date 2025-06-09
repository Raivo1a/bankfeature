import pytest

from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize('card_number, expected',
    [(1596837868705199, '1596 83** **** 5199'),
    (7158300734726758, '7158 30** **** 6758'),
    (6831982476737658, '6831 98** **** 7658')])

def test_get_mask_card_number(card_number: str, expected: str):
    assert get_mask_card_number(str(card_number)) == expected

@pytest.mark.parametrize('card_number', [
    '2345346453456755475', # слишком длинный номер
    '124', # слишком короткий номер
    'abc', # содержит буквы
])

def test_get_mask_invalid_card_number(card_number):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
    assert str(exc_info.value) == 'Ошибка! Введите корректный номер карты или счета'


@pytest.mark.parametrize('card_account, expected',
    [(64686473678894779589, '**9589'),
     (35383033474447895560, '**5560'),
     (73654108430135874305, '**4305')])

def test_get_mask_account(card_account: str, expected: str):
    assert get_mask_account(str(card_account)) == expected

@pytest.mark.parametrize("card_account", [
    '23453464534567554752346426', # слишком длинный номер
    '124', # слишком короткий номер
    'abc', # содержит буквы
])

def test_get_mask_invalid_account(card_account):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(card_account)
    assert str(exc_info.value) == 'Ошибка! Введите корректный номер карты или счета'
