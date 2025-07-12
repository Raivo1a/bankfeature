import json

def get_operations_data(path: str) -> list:
    """Обрабатывает JSON-файл и преобразует в список транзакций"""
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
        except Exception:
            return []

print(get_operations_data("data/operations.json"))
