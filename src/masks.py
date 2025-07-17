import logging
from typing import Union

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция прячет номер карты"""
    logger.info("Создаем маску банковской карты")
    if len(card_number) != 16:
        logger.error("Ошибка!")
        raise ValueError("Ошибка! Введите корректный номер карты или счета")
    else:
        logger.info("Создание успешно")
        return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(card_account: Union[str]) -> Union[str]:
    """Функция прячет номер счета"""
    logger.info("Создаем маску номера счета")
    if len(card_account) != 20:
        logger.error("Ошибка!")
        raise ValueError("Ошибка! Введите корректный номер карты или счета")
    else:
        logger.info("Создание успешно")
        return "**" + card_account[-4:]
