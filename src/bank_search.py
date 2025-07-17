import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Поиск в списке операций по заданной строке. Возвращает список операций с подходящим описанием"""
    result = []
    re_pattern = re.compile(search, re.IGNORECASE)
    for operation in data:
        if re_pattern.search(str(operation.get("description", ""))):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция подсчета операций по заданным пользователем категориям.
    Возвращает словарь с названиями категорий и их количеством"""
    count_categories = []
    for operation in data:
        if operation.get("description", "") in categories:
            count_categories.append(operation.get("description", ""))
    return dict(Counter(count_categories))
