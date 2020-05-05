from enum import Enum

token = "603630995:AAE4ipKxCKdRzLjYLV6DwC0YcnIh5grxdas"
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_SEND_PIC = "1"
