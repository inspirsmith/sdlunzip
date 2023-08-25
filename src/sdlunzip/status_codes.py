from enum import IntEnum, auto


class Status(IntEnum):
    SUCCESS = auto()
    FAILURE = auto()
    NO_PWD = auto()
    BAD_PWD = auto()
    BAD_ZIP = auto()
    FILE_NOT_FOUND = auto()
