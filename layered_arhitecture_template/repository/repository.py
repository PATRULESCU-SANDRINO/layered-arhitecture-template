from layered_arhitecture_template.domain.exceptions import MainException, StoreException


class RepositoryException(StoreException):
    pass


class Repository(object):
    def __init__(self, validator_class):
        self._data = []
        self._validator_class = validator_class

    def find(self, attribute1_):
        """
        Find item having given attribute
        """
        for index in range(len(self._data)):
            if self._data[index].attribute1 == attribute1_:
                return index
        return -1

    def store(self, item):
        """
        Store a new item into the repository
        """
        if self.find(item.attribute1) != -1:
            raise RepositoryException("Item with attribute1=" + str(item.attribute1) + "already in the repo.")
        self._validator_class.validate(item)
        self._data.append(item)

    def delete(self, attribute1_):
        """
        Delete item with given attribute from repository
        """
        index = self.find(attribute1_)
        if index == -1:
            raise RepositoryException("Item with attribute1=" + str(attribute1_) + "not in the repo.")
        del self._data[index]

    def __getitem__(self, attribute1_):
        for item in self._data:
            if item.attribute1 == attribute1_:
                return item
        raise RepositoryException("Item with attribute1=" + str(attribute1_) + "not in the repo.")

    def update(self, attribute1, item):
        """
        Update an item from repository
        """
        index = self.find(attribute1)
        if index == -1:
            raise RepositoryException("Item with attribute1=" + str(attribute1) + "not in the repo.")
        self._validator_class.validate(item)
        self._data[index] = item
