from dataclasses import dataclass


@dataclass
class Entity2:
    __attribute1: int
    attribute2: str
    attribute3: int

    @property
    def attribute1(self):
        return self.__attribute1

    def __str__(self):
        result = "attribute1: " + str(self.__attribute1) + ','
        result = result + " attribute2: " + str(self.attribute2) + ','
        result = result + " attribute3: " + str(self.attribute3)
        return result
