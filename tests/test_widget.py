import pytest

from src.widget import get_date, mask_account_card

@pytest.mark.parametrize('account_card, expected',
    [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
     ('Счет 64686473678894779589', 'Счет **9589'),
     ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229')])

def test_mask_account_card(account_card: str, expected: str):
    assert mask_account_card(account_card) == expected

@pytest.mark.parametrize('date, result',
    [('2018-01-01T20:14:21.372307', '01.01.2018'),
    ('2025-06-05T18:15:10.512454', '05.06.2025'),
    ('2020-06-29T02:17:08.235653', '29.06.2020')])

def test_get_date(date: str, result: str):
    assert get_date(date) == result
