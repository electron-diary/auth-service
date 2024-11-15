from typing import Self


class BaseApplicationError(Exception):
    def __init__(self: Self, exception_message: str) -> None:
        super().__init__(exception_message)
