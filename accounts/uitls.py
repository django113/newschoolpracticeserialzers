from enum import Enum


class accountsDesignationEnumTypes(Enum):
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"

    @classmethod
    def choices(cls):
        return [(key.value,key.name) for key in cls]
