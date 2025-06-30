from typing import List, Dict

def filter_by_state(operation_list: list[dict], state : str = "EXECUTED") -> list[dict] :
    """
    Фильтрует список словарей по значению ключа 'state'
    """
    return [transaction for transaction in operation_list if transaction.get("state") == state]