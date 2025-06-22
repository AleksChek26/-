def get_mask_card_number(card_num: str) -> str:
    """Функция для маскировки номера карты"""
    card_num = str(card_num)
    return f"{card_num[0:4]}{card_num[4:6]}** ****{card_num[12:16]}"


def get_mask_account(acc_num: str) -> str:
    """Функция для маскировки номера счета"""
    acc_num = str(acc_num)
    return f"**{acc_num[16:]}"
