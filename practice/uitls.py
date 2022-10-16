from enum import Enum


class parcticestudentMainGradeEnumTypes(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
