def filter_by_state(operations: list[dict], state:str = 'EXECUTED') -> list[dict]:
    '''Функция возвращает новый список словарей, содержащий только те словари, у которых ключ EXECUTED'''
    result = []
    for operation in operations:
        if operation['state'] == state:
            result.append(operation)
    return result

def sort_by_date(data: list[dict[str]], descending: bool = True) -> list[dict[str]]:
    '''Функция сортировки списка банковских операций по дате'''
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=descending)
    return sorted_list
