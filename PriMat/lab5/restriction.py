import numpy as np

from enum import Enum


class RestrictionType(Enum):
    EQUAL = "="
    GREATER = ">="
    LESS = "<="


class Restriction:
    def __init__(self,
                 coefficients: np.array,
                 restriction_type: RestrictionType,
                 value: float):

        self.coefficients = coefficients
        self.restriction_type = restriction_type
        self.value = value

    def __str__(self):
        return f"{self.coefficients} {self.restriction_type.value} {self.value}"

    def to_canonical(self) -> None:
        if self.value < 0:
            self.coefficients *= -1
            self.value *= -1
            if self.restriction_type == RestrictionType.GREATER:
                self.restriction_type = RestrictionType.LESS
            elif self.restriction_type == RestrictionType.LESS:
                self.restriction_type = RestrictionType.GREATER


if __name__ == '__main__':
    pass