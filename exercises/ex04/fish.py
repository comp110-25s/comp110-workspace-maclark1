"""File to define Fish class."""

__author__: str = "730705563"


class Fish:
    age: int

    def __init__(self):
        self.age: int = 0

    def one_day(self):
        self.age += 1
        return None
