import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_operations_data(path: str) -> list:
    """Обрабатывает JSON-файл и преобразует в список транзакций"""
    logger.info("Запрос на преобразование файла json")
    with open(path, "r", encoding="utf-8") as f:
        try:
            logger.info("Список транзакций успешно создан")
            return json.load(f)
        except json.JSONDecodeError:
            logger.error("Ошибка декодирования JSON-файла")
            return []
        except Exception:
            logger.error("Ошибка! Файл пуст")
            return []
