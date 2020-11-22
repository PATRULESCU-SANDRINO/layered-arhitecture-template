

class MainException(Exception):
    """
    General Exception class used for Main problem
    """
    def __init__(self, msg):
        super().__init__(msg)


class StoreException(MainException):
    def __init__(self, msg):
        super().__init__(self, msg)

