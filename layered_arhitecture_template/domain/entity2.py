from dataclasses import dataclass


@dataclass
class Entity2:
    __attribute1: int
    attribute2: str
    attribute3: int

    @property
    def attribute1(self):
        return self.__attribute1
