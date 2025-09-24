from typing import Literal
from pyPRUF import FSet


class FuzzySort:
    def __init__(
        self,
        f_set: FSet,
        column: str,
        direction: Literal["asc", "desc"] = "asc"
    ):
        self.f_set = f_set
        self.column = column
        self.direction = direction

    def convert_direction(self):
        return self.direction == "asc"