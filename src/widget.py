

from masks import get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция принимает информацию о карте и маскирует ее номер"""
    card_type_list = []
    card_info_list = card_info.split()

    for string in card_info_list:
        if string.isalpha():
            card_type_list.append(string)
    card_type = " ".join(card_type_list)

    card_number = int(card_info_list[-1])
    return f"{card_type} {get_mask_card_number(card_number)}"

from datetime import datetime


def get_date(iso_date: str) -> str:
    """Преобразует дату в 'ДД.ММ.ГГГГ'"""

    return datetime.fromisoformat(iso_date).strftime("%d.%m.%Y")
