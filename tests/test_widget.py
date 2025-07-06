import pytest
from src.widget import mask_account_card

@pytest.mark.parametrize('card_name, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
])

def test_mask_account_card(card_name, expected):
    assert mask_account_card(card_name) == expected