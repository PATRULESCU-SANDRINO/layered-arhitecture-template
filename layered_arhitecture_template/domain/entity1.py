

class Entity1:

    def __init__(self, attribute1, attribute2, attribute3):
        self.__attribute1 = attribute1
        self.__attribute2 = attribute2
        self.__attribute3 = attribute3

    @property
    def attribute1(self):
        return self.__attribute1

    @property
    def attribute2(self):
        return self.__attribute2

    @property
    def attribute3(self):
        return self.__attribute3

    @attribute3.setter
    def attribute3(self, new_value):
        self.__attribute3 = new_value

    def __str__(self):
        result = "attribute1: " + str(self.__attribute1) + ','
        result = result + " attribute2: " + str(self.__attribute2) + ','
        result = result + " attribute3: " + str(self.__attribute3)
        return result

