import unittest

from layered_arhitecture_template.domain.entity1 import Entity1
from layered_arhitecture_template.domain.validators import Entity1ValidatorException, Entity1Validator
from layered_arhitecture_template.repository.repository import Repository, RepositoryException


class TestRepository(unittest.TestCase):
    def setUp(self):
        """
        Runs before each test method
        """
        self._repo = Repository(Entity1Validator)
        self._repo.store(Entity1(1, "abc", 11))
        self._repo.store(Entity1(2, "efg", 12))
        self._repo.store(Entity1(3, "hij", 13))

    def test_repository_find(self):
        self.assertNotEqual(self._repo.find(3), -1)
        self.assertEqual(self._repo.find(0), -1)

    def test_repository_store(self):
        self.assertEqual(len(self._repo._data), 3)
        self.assertRaises(RepositoryException, self._repo.store, Entity1(2, "hij", 13))

        #self.assertRaises(Entity1ValidatorException, self._repo.store, Entity1(-1, "lll", 17))

    def test_repository_delete(self):
        self._repo.delete(2)
        self.assertEqual(len(self._repo._data), 2)
        self.assertRaises(RepositoryException, self._repo.delete, 0)

    def test_repository_getitem(self):
        item = self._repo.__getitem__(2)
        self.assertEqual(item.attribute1, 2)
        self.assertEqual(item.attribute2, "efg")
        self.assertEqual(item.attribute3, 12)

        self.assertRaises(RepositoryException, self._repo.__getitem__, 0)

    def test_repository_update(self):
        self._repo.update(2, Entity1(6, "zzz", 2))
        self.assertNotEqual(self._repo.find(6), -1)
        item = self._repo.__getitem__(6)
        self.assertEqual(item.attribute1, 6)
        self.assertEqual(item.attribute2, "zzz")
        self.assertEqual(item.attribute3, 2)

        self.assertRaises(RepositoryException, self._repo.update, *[7, Entity1(19, "idk", 0)])

    def tearDown(self):
        print("TORN DOWN")
        """
        Runs after each test method
        """