import logging

import pandas as pd

logger = logging.getLogger("reader")
file_handler = logging.FileHandler("logs/reader.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_csv_file(path: str) -> list:
    """Обрабатывает CSV-файл и преобразует в список транзакций"""
    logger.info("Запрос на преобразование файла csv")
    try:
        logger.info("Список транзакций успешно создан")
        df = pd.read_csv(path, delimiter=";", encoding="utf-8")
        result = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        logger.error("Ошибка! Файл не найден")
        return []
    except Exception:
        logger.error("Ошибка! Файл пуст")
        return []


def read_xlsx_file(path: str) -> list:
    """Обрабатывает XLSX-файл и преобразует в список транзакций"""
    logger.info("Запрос на преобразование файла xlsx")
    try:
        logger.info("Список транзакций успешно создан")
        df = pd.read_excel(path)
        result = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        logger.error("Ошибка! Файл не найден")
        return []
    except Exception:
        logger.error("Ошибка! Файл пуст")
        return []
