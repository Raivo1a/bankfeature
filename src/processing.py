def filter_by_state(operations, state='EXECUTED'):
'''Функция возвращает новый список словарей, содержащий только те словари, у которых ключ EXECUTED'''
    result = []
    for operation in operations:
        if operation['state'] == state:
            result.append(operation)
    return result
