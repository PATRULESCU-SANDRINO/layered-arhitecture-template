from layered_arhitecture_template.domain.exceptions import StoreException


class Entity1ValidatorException(StoreException):
    pass


class Entity2ValidatorException(StoreException):
    pass


class Entity1Validator(object):
    @staticmethod
    def validate(entity1):
        if type(entity1.attribute1) is not int:
            raise Entity1ValidatorException("attribute1 must be an int!")
        if entity1.attribute1 < 0:
            raise Entity1ValidatorException("attribute1 must be greater or equal than 0!")


class Entity2Validator(object):
    @staticmethod
    def validate(entity2):
        if type(entity2.attribute1) is not int:
            raise Entity2ValidatorException("attribute1 must be an int!")
        if entity2.attribute1 < 1:
            raise Entity2ValidatorException("attribute 1 must be greater or equal than 1")
