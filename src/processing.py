import typing


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    result = []
    for operation in operations:
        if operation["state"] == state:
            result.append(operation)
    return result


def sort_by_date(data: list[dict[str, typing.Any]], descending: bool = True) -> list[dict[str, typing.Any]]:
    """Функция принимает список словарей и необязательный параметр, задающий
    порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)"""
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=descending)
    return sorted_list
